from setuptools import setup, find_packages

setup(
    name="git_llm",  # 包名
    version="0.1.0",  # 版本号
    author="zzszmyf",  # 作者名
    author_email="zzszmyf@outlook.com",  # 作者邮箱
    description="llm echance for git",  # 简短描述
    long_description=open('README.md').read(),  # 详细描述，通常从README文件读取
    long_description_content_type="text/markdown",  # README文件类型，如果使用Markdown
    url="https://github.com/zzszmyf/git-llm",  # 项目主页
    py_modules=["git_commit_generator", "git_branch_name_generator"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],  # 分类信息
    install_requires=[
        "python-dotenv",  # 项目依赖
    ],
    python_requires='>=3.6',  # 最低Python版本要求
    entry_points={  # 添加命令行脚本
        'console_scripts': [
            'git-gen-commit=git_commit_generator:main',
            'git-gen-branch-name=git_branch_name_generator:main'
        ],
    },
)
