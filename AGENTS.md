# 仓库发布边界

以下规则用于工厂源码维护和 GitHub 发布；生成视频时无需增加发布步骤。

本仓库仅维护 `video-replacement-skill-factory`，唯一发布目标是 `https://github.com/10ve10/video-replacement-skill-factory-T8`。原始上游 `https://github.com/T8mars/video-replacement-skill-factory-T8` 仅作为参考/可选同步来源，未经用户明确要求不得推送到上游。其他技能、`r2va-video-*` 专属技能、制作项目和媒体不得混入。

修改前先读 SKILL.md、meta.json、features.json、manifest.json、publish-policy.json、相关配置、源码和测试。README 的账号入口和作者资源链接按用户提供的内容维护。

任何目录下、任何大小写的 ROADMAP.MD 都禁止提交或推送。API Key、令牌、凭据文件、私有账本、运行记录、输入人物图、候选与成片同样禁止。不得因为 .gitignore 存在就认为已跟踪文件安全，不得使用 force push 掩盖泄漏。

同步使用 `tools/sync_skill.py --source <本机工厂技能目录>`，按源 manifest 和仓库明确白名单复制，仅暂存核对过的具体文件。提交前运行 `python tools/verify_publish.py --staged`，推送前再次扫描待发送的所有提交。必须核对 origin 指向上述仓库；不要在其他技能或混合工作区执行推送。

默认沿用 main，保留已有远端提交和用户修改。每次更新完善相关 README，维护源 manifest 文件哈希。本次用户已授权该工厂的后续更新发布到此专属仓库；用户的新指令优先。
