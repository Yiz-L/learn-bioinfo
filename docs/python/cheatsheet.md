# 📖 Python速查表

> 快速查找常用语法，忘记的时候回来翻翻

---

## 基础语法

```python
# 打印输出
print("hello")

# 注释
# 这是单行注释

"""
这是多行注释
可以写很多行
"""
```

---

## 数据类型

```python
# 数字
age = 25              # int
pi = 3.14             # float

# 字符串
name = "YizL"         # str

# 布尔
is_ok = True          # bool
is_bad = False

# 类型转换
str(42)               # "42"
int("42")             # 42
float("3.14")         # 3.14
```

---

## 字符串操作

```python
s = "hello"
s.upper()             # "HELLO"
s.lower()             # "hello"
len(s)                # 5
s + " world"          # "hello world"
f"{s} world"          # "hello world" (f-string)
```

---

## 列表

```python
lst = [1, 2, 3]
lst.append(4)         # [1,2,3,4]
lst[0]                # 1
len(lst)              # 4
lst[-1]               # 最后一个：4
lst[1:3]              # 切片：[2,3]
for x in lst:         # 遍历
    print(x)
```

---

## 字典

```python
d = {"key": "value", "age": 25}
d["key"]              # "value"
d.get("key")          # "value"
d.keys()              # 所有键
d.values()            # 所有值
d.items()             # 所有键值对
```

---

## 条件判断

```python
if x > 0:
    print("正数")
elif x == 0:
    print("零")
else:
    print("负数")
```

---

## 循环

```python
# for循环
for i in range(5):
    print(i)          # 0,1,2,3,4

for item in lst:
    print(item)

# while循环
while x > 0:
    x -= 1
```

---

## 函数

```python
def add(a, b):
    """返回a+b的结果"""
    return a + b

result = add(3, 5)     # 8
```

---

## 文件操作

```python
# 读文件
with open("file.txt", "r", encoding="utf-8") as f:
    content = f.read()

# 写文件
with open("file.txt", "w", encoding="utf-8") as f:
    f.write("hello")

# 逐行读
with open("file.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
```

---

## pip常用命令

```bash
pip install 包名      # 安装包
pip install 包名==1.0 # 安装指定版本
pip list              # 查看已安装的包
pip uninstall 包名    # 卸载
```
