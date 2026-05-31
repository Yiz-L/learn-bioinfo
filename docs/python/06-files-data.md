# 第6章：文件与数据

> 学习目标：读写文件、处理CSV数据——这是科研数据处理的第一步！

---

## 6.1 为什么文件操作很重要

你的实验数据在哪？在文件里。ELISA读数、流式细胞术数据、临床数据……几乎都是文件。

```python
# 写文件
with open("实验记录.txt", "w", encoding="utf-8") as f:
    f.write("2026-06-01：完成了第一批ELISA实验\n")
    f.write("IL-6浓度：45.2 pg/mL\n")

# 读文件
with open("实验记录.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)
```

### `with open(...) as f:` 详解

| 部分 | 含义 |
|------|------|
| `"w"` | 写入模式（覆盖写） |
| `"r"` | 读取模式 |
| `"a"` | 追加模式（在文末添加） |
| `encoding="utf-8"` | 中文编码 |

---

## 6.2 逐行处理文件

```python
with open("实验记录.txt", "r", encoding="utf-8") as f:
    for line in f:
        print("→ " + line.strip())  # strip()去掉换行符
```

---

## 6.3 CSV数据：科研中最常见的格式

CSV就是"逗号分隔的值"——Excel能打开，Python也能处理。

```python
students = [
    ["name", "score", "grade"],
    ["Alice", 85, "A"],
    ["Bob", 72, "B"],
    ["Charlie", 90, "A"]
]

with open("students.csv", "w", newline="", encoding="utf-8") as f:
    for row in students:
        f.write(",".join(str(item) for item in row) + "\n")

print("CSV写入完成！")
```

---

## 6.4 动手练习

### 练习1：记录每日学习进度

```python
import datetime

def log_study(topic, duration):
    """记录学习日志"""
    with open("学习日志.csv", "a", encoding="utf-8") as f:
        today = datetime.date.today()
        f.write(f"{today},{topic},{duration}分钟\n")

# 使用
log_study("Python变量", 30)
log_study("if条件判断", 45)

print("学习记录已保存！")
```

运行输入：

```
学习记录已保存！
```

查看生成的CSV文件：

```
2026-06-01,Python变量,30分钟
2026-06-01,if条件判断,45分钟
```

---

## 📋 本章检查清单

- [ ] 我能用Python创建并写入文件
- [ ] 我能读取文件内容
- [ ] 我能逐行读取文件
- [ ] 我能用Python创建CSV文件
- [ ] 我完成了学习日志记录练习

---

---

[← 上一章：函数与模块](05-functions-modules.md) | [📖 返回目录](index.md) | [下一章：实战 →](07-research-tools.md)
