# 第1章：从Python到R

> 学习目标：用你已经会的Python知识，快速理解R的语法

---

## 1.1 思维迁移

你已经学会了编程思维，现在只是换一门"方言"：

```python
# Python
name = "YizL"
print(f"你好，{name}")
```

```r
# R
name <- "YizL"
cat("你好，", name, "\n")
```

### 核心差异速览

| 概念 | Python | R |
|------|--------|---|
| 赋值 | `x = 10` | `x <- 10` 或 `x = 10` |
| 打印 | `print(x)` | `print(x)` 或 `cat(x)` |
| 注释 | `# 注释` | `# 注释` |
| 索引 | 从0开始 | 从1开始 |
| 包管理 | `pip install` | `install.packages()` |
| 帮助 | `help()` | `?函数名` |

---

## 1.2 安装R和RStudio

```bash
# 1. 下载R：https://cran.r-project.org/
# 2. 下载RStudio：https://posit.co/download/rstudio/
# 3. 安装包：
install.packages("tidyverse")  # 数据分析全家桶
install.packages("ggplot2")    # 可视化
```

---

## 📋 本章只是过渡

> 这一章的核心是建立心理模型：**你不是在重新学编程，只是在学一门新方言。**
> 具体语法将在第2章展开。
