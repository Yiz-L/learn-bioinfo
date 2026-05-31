# 第2章：变量与数据

> 学习目标：理解变量、掌握基本数据类型、学会输入输出

---

## 2.1 什么是变量？

变量就是**带名字的盒子**，你可以把数据放进去，之后通过名字取出来。

```python
# 把数字 5 放进名为 "count" 的盒子
count = 5

# 把文字放进名为 "disease" 的盒子
disease = "类风湿关节炎"

# 取出使用
print(count)     # 输出: 5
print(disease)   # 输出: 类风湿关节炎
```

### 医学类比

> 变量就像病历上的字段名：
> - `patient_name = "张三"`
> - `age = 45`
> - `diagnosis = "SLE"` (系统性红斑狼疮)

---

## 2.2 基本数据类型

Python 中最常用的三种数据类型：

### 数字（int / float）

```python
# 整数 (int)
patient_count = 30
year = 2026

# 小数/浮点数 (float)
temperature = 38.5
cd4_count = 856.3

# 数学运算
total = patient_count + 10   # 加法
ratio = cd4_count / 2        # 除法
print(total, ratio)
```

### 字符串（str）

```python
# 文字就是字符串
name = "白介素-6"
description = '一种重要的炎症因子'

# 字符串拼接
full = name + "：" + description
print(full)   # 输出: 白介素-6：一种重要的炎症因子
```

### 布尔值（bool）

```python
# 只有两种：True 或 False
is_inflamed = True
has_fever = False

print(is_inflamed)  # 输出: True
```

---

## 2.3 获取用户输入

```python
name = input("请输入你的名字：")
print("你好，" + name + "！欢迎来到编程世界！")
```

运行试试：

```
请输入你的名字：YizL
你好，YizL！欢迎来到编程世界！
```

---

## 2.4 动手练习

### 练习1：个人信息卡
```python
# 创建一个"个人信息卡"
name = "你的名字"
age = 你的年龄
major = "临床医学"
interest = "免疫学"

print("姓名：" + name)
print("年龄：" + str(age))
print("专业：" + major)
print("兴趣方向：" + interest)
```

!!! tip "`str()` 是什么？"
    当数字和文字拼接时，需要用 `str()` 把数字转成文字。  
    `print("年龄：" + age)` 会报错，必须写成 `print("年龄：" + str(age))`

### 练习2：BMI计算器

```python
height = float(input("请输入身高(米)："))
weight = float(input("请输入体重(千克)："))

bmi = weight / (height ** 2)

print("你的BMI是：" + str(bmi))
```

---

## 2.5 医学小剧场：记录患者信息

```python
# 记录一个患者的基本信息
patient_id = "P2026001"
age = 35
diagnosis = "桥本甲状腺炎"
anti_tpo = 586.3  # 抗TPO抗体滴度

print("=== 患者信息 ===")
print("ID：" + patient_id)
print("年龄：" + str(age))
print("诊断：" + diagnosis)
print("抗TPO抗体：" + str(anti_tpo) + " IU/mL")
```

---

## 📋 本章检查清单

- [ ] 我理解了"变量就是带名字的盒子"
- [ ] 我能区分 int（整数）、float（小数）、str（字符串）
- [ ] 我会用 `+` 拼接字符串
- [ ] 我会用 `input()` 获取用户输入
- [ ] 我完成了个人信息卡练习
- [ ] 我完成了BMI计算器

---

## 🔜 下一章预告

第3章：条件与循环 —— 让程序做判断、重复做事
