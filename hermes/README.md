# Hermes support

This directory adds a Hermes-native skill definition for the existing Video Replacement Skill Factory. The media-processing and RunningHub implementation remains in the repository root; this is an orchestration/compatibility layer, not a replacement video model or a claim that new backends already exist.

## Install

Hermes loads skills from `~/.hermes/skills/<skill-name>/SKILL.md`. Because this skill calls scripts and reads assets from the repository root, keep the full checkout beside the skill and link/copy the skill definition into Hermes' skill directory.

### Linux / macOS

```bash
git clone https://github.com/10ve10/video-replacement-skill-factory-T8.git ~/video-replacement-skill-factory-T8
mkdir -p ~/.hermes/skills/video-replacement-skill-factory
cp ~/video-replacement-skill-factory-T8/hermes/SKILL.md ~/.hermes/skills/video-replacement-skill-factory/SKILL.md
python3 -m pip install -r ~/video-replacement-skill-factory-T8/requirements.txt
```

### Windows PowerShell

```powershell
git clone https://github.com/10ve10/video-replacement-skill-factory-T8.git "$HOME\video-replacement-skill-factory-T8"
New-Item -ItemType Directory -Force "$HOME\.hermes\skills\video-replacement-skill-factory" | Out-Null
Copy-Item "$HOME\video-replacement-skill-factory-T8\hermes\SKILL.md" "$HOME\.hermes\skills\video-replacement-skill-factory\SKILL.md"
python -m pip install -r "$HOME\video-replacement-skill-factory-T8\requirements.txt"
```

Install `ffmpeg` and `ffprobe` separately and ensure they are on `PATH`. The skill currently orchestrates the existing repository scripts; it does not yet provide a self-contained package or verified ComfyUI/Kling/Seedance/MiniMax adapters.

## Configure RunningHub

Follow the existing root README and backend documentation. Keep the API key in the documented private local key file outside the repository and production assets. Never paste credentials into chat or commit them. Confirm account permissions and billing before cloud generation.

## First run

1. Restart/reload Hermes if required by your installation.
2. Ask Hermes to use the video replacement skill with a source video and target reference image(s).
3. For a new source/backend combination, require one representative generation and actual review before batching.
4. Inspect the final MP4 and the QC report yourself before treating it as production-ready.

## Current limitations

- Hermes integration is a skill prompt layer; the underlying media scripts remain shared with the original project.
- Cloud generation requires a working RunningHub account, API key, application/model access, and may incur cost.
- Automated technical checks do not prove correct identity, natural motion, or visual continuity.
- Additional backend adapters, batch scheduling, and objective visual scoring should only be advertised as supported after implementation and tests.
