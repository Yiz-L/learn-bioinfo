# 第5章：函数与模块

> 学习目标：写自己的"代码工具箱"（函数）、用别人的轮子（模块）

---

## 5.1 函数是什么？

函数就是**给一段代码取个名字**，以后可以随时调用。

### 不像函数的函数

```python
# 定义函数
def say_hello():
    print("你好，免疫学！")

# 调用函数
say_hello()
say_hello()  # 想用几次用几次
```

### 带参数的函数

```python
def check_fever(temp):
    if temp > 37.3:
        return "发热"
    else:
        return "正常"

# 使用
result1 = check_fever(38.5)
result2 = check_fever(36.5)
print(result1)  # 发热
print(result2)  # 正常
```

### 医学类比

> 函数就像医院的检验科：
> - 你把血样送进去（参数）
> - 检验科处理（函数体）
> - 得到化验结果（返回值）

---

## 5.2 定义自己的函数库

```python
# temp_utils.py — 体温相关的工具函数

def celsius_to_fahrenheit(c):
    """将摄氏度转换为华氏度"""
    return c * 9 / 5 + 32

def classify_fever(temp):
    """根据体温分类"""
    if temp >= 39.0:
        return "高热"
    elif temp >= 38.0:
        return "中度发热"
    elif temp >= 37.3:
        return "低热"
    else:
        return "正常"

def temp_difference(temp1, temp2):
    """计算体温变化"""
    return round(temp2 - temp1, 1)
```

然后在另一个文件中使用：

```python
from temp_utils import celsius_to_fahrenheit, classify_fever

t = 38.5
print(classify_fever(t))              # 中度发热
print(celsius_to_fahrenheit(t))       # 101.3
```

---

## 5.3 模块：站在巨人的肩膀上

别人已经写好了很多有用的代码库（模块），直接用就好。

```python
# Python自带模块
import math
import random
import statistics

print(math.pi)                    # 3.141592653589793
print(random.randint(1, 100))    # 随机数
print(statistics.mean([1, 2, 3, 4, 5]))  # 平均值
```

### 安装第三方模块

```bash
pip install numpy pandas matplotlib
```

```python
import numpy as np

# 创建一个数组
data = np.array([1.2, 3.4, 5.6, 7.8])
print(np.mean(data))    # 平均值
print(np.std(data))     # 标准差
```

---

## 5.4 动手练习

### 练习：创建一个实验数据处理工具箱

```python
# lab_tools.py
def calc_mean(values):
    """计算平均值"""
    return sum(values) / len(values)

def calc_dilution(concentration, factor):
    """计算稀释后的浓度"""
    return concentration / factor

def check_outlier(value, mean, std):
    """判断是否离群（超过2个标准差）"""
    if abs(value - mean) > 2 * std:
        return True
    return False

# 使用
measurements = [45.2, 46.1, 44.8, 72.3, 45.5]
avg = calc_mean(measurements)
print("平均值：" + str(avg))
for m in measurements:
    if check_outlier(m, avg, 0.8):
        print("发现离群值：" + str(m))
```

---

## 📋 本章检查清单

- [ ] 我会用 `def` 定义函数
- [ ] 我能区分"参数"和"返回值"
- [ ] 我理解函数如何让代码复用
- [ ] 我学会了 `import` 导入模块
- [ ] 我试过用 `pip install` 安装第三方库
- [ ] 我完成了实验数据处理工具箱练习

---

---

[← 上一章：数据结构](04-data-structures.md) | [📖 返回目录](index.md) | [下一章：文件与数据 →](06-files-data.md)
