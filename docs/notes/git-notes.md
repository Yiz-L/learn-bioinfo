# Git版本控制

> 用Git管理代码版本

---

## 基本流程

```bash
# 初始化仓库
git init

# 查看状态
git status

# 添加文件到暂存区
git add .

# 提交到本地仓库
git commit -m "描述这次改了什么"

# 查看提交历史
git log --oneline
```

---

## 常用命令

| 命令 | 作用 |
|------|------|
| `git init` | 初始化仓库 |
| `git add 文件名` | 添加文件 |
| `git commit -m "信息"` | 提交版本 |
| `git status` | 查看状态 |
| `git log` | 查看历史 |
| `git diff` | 查看改动 |

!!! tip "先记住这几个就够了"
    更多的Git命令（分支、远程等）用到时再学。
