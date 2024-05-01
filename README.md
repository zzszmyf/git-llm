# git-llm

## 安装与配置指南
### 步骤 1: 准备环境变量文件
首先，我们需要创建一个环境变量文件来安全地存储你的OpenAI服务配置。这将确保敏感信息如API密钥不会直接暴露在代码中。

```sh
# 创建 .env 文件
touch .env

# 填充环境变量
# 请将下方的 `<your-openai-base-url>`、`<your-openai-api-key>` 和 `<your-openai-model-name>` 替换为实际值
echo "LLM_URL=<your-openai-base-url>" >> .env
echo "LLM_API_KEY=<your-openai-api-key>" >> .env
echo "LLM_MODEL_NAME=<your-openai-model-name>" >> .env
```
注意: 请确保使用自己的OpenAI服务URL、API密钥和所选模型名称进行替换。

### 步骤 2: 安装项目
接下来，我们将使用pip在开发模式下安装项目。这种方式允许你在修改代码后立即看到效果，无需每次都重新安装。
```
# 在本地以可编辑模式安装项目
pip install -e . --use-pep517
```
使用-e标志意味着以“editable”模式安装，允许直接在源代码目录中修改并立即生效。--use-pep517选项确保安装过程中遵循PEP 517规范，这对于基于现代构建系统的项目尤为重要。

完成以上两步后，你的项目应已成功安装，并准备就绪

### 使用案例
#### 自动生成Commit信息
当你对代码进行了修改，并希望通过git diff的输出自动生成一个符合规范的Git commit信息，可以按照以下步骤操作：
```
# 首先，查看你的代码变更
git diff

# 然后，将diff输出直接传递给git-gen-commit脚本以生成并提交commit
git diff | git-gen-commit
```
这个命令组合会读取git diff的输出内容，并使用git-gen-commit工具（基于你之前配置的脚本）分析这些变更，自动生成一个合适的commit信息，并执行提交操作。请确保git-gen-commit已正确安装且配置在你的系统中。
#### 自动生成Branch名称
当你想要基于一个预设的Git commit信息来创建一个新的分支时，可以使用以下命令格式：
```
# 假设你已经有了一条预设的commit信息，比如"Fix typo in README"
echo "Fix typo in README" | git-gen-branch-name
```
或者，如果你是从现有的commit中提取信息来创建分支：
```
# 获取最近一次commit的信息
git_commit_message=$(git log -1 --pretty=%B)

# 使用该信息生成分支名称
echo "${git_commit_message}" | git-gen-branch-name
```
这段脚本首先获取最近一次commit的message，然后将其传递给git-gen-branch-name工具，该工具会基于commit message的内容生成一个适合作为分支名称的字符串。这在你需要基于特定更改快速创建和切换分支时非常有用。

请记得，为了使这两个命令有效，你需要确保git-gen-commit和git-gen-branch-name命令可用，并且它们已经被正确安装和配置在你的系统路径中。

联系我们

如果你有任何疑问、反馈或需要帮助，请随时通过以下方式与我们取得联系：

邮箱: zzszmyf@outlook.com
微信: zzszmyf
我将尽快回复你，确保你的体验顺畅。

