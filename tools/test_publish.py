"""Offline publication guard regressions; fixtures never contain real secrets."""
import hashlib, json, unittest
import verify_publish as guard

def fixture():
    files={'SKILL.md':b'---\nname: video-replacement-skill-factory\n---\n',
           'meta.json':json.dumps({'name':guard.EXPECTED_SKILL,'version':'fixture'}).encode()}
    files['manifest.json']=json.dumps({'name':guard.EXPECTED_SKILL,'version':'fixture',
        'files':{name:hashlib.sha256(data).hexdigest() for name,data in files.items()}}).encode()
    files['publish-policy.json']=json.dumps({'skill':guard.EXPECTED_SKILL,'repository':guard.EXPECTED_REPO,
        'runtime_files':['SKILL.md','meta.json','manifest.json'],
        'repository_files':['publish-policy.json']}).encode()
    return files

class PublishGuard(unittest.TestCase):
    def test_clean_factory_passes(self):
        self.assertEqual(guard.check_tree(fixture()),[])
    def test_roadmap_any_case_and_directory_blocked(self):
        for name in ('ROADMAP.MD','roadmap.md','docs/RoAdMaP.Md'):
            self.assertTrue(guard.check_payload(name,b'planning'))
    def test_key_file_and_embedded_known_value_blocked(self):
        self.assertTrue(guard.check_payload('private/api_key.txt',b'fixture'))
        key=b'OFFLINE_ONLY_'+b'Q'*32
        errors=guard.check_payload('README.md',b'example '+key,[key])
        self.assertTrue(errors)
        self.assertNotIn(key.decode(),' '.join(errors))
    def test_token_assignment_is_detected_without_printing_value(self):
        value=b'Z'*32
        errors=guard.check_payload('README.md',b'api_key = "'+value+b'"')
        self.assertTrue(errors)
        self.assertNotIn(value.decode(),' '.join(errors))
    def test_other_skill_media_and_unknown_file_blocked(self):
        for name in ('r2va-video-fixture/SKILL.md','other/SKILL.md','assets/source.mp4'):
            self.assertTrue(guard.check_payload(name,b'fixture'))
        files=fixture();files['other-project.txt']=b'fixture'
        self.assertTrue(guard.check_tree(files))
    def test_changed_runtime_signature_blocked(self):
        files=fixture();files['SKILL.md']+=b'changed'
        self.assertTrue(guard.check_tree(files))
    def test_wrong_remote_and_identity_blocked(self):
        self.assertFalse(guard.remote_ok('https://github.com/T8mars/other-project'))
        self.assertTrue(guard.remote_ok(guard.EXPECTED_REPO+'.git'))
        files=fixture();files['SKILL.md']=b'name: unrelated-skill\n'
        self.assertTrue(guard.check_tree(files))

if __name__=='__main__':
    unittest.main(verbosity=2)
