# 第4章：数据结构

> 学习目标：学会用列表、字典组织数据，为数据分析打基础

---

## 4.1 列表（List）

列表就是**有序的容器**，可以放多个数据。

```python
# 创建一个列表
cytokines = ["IL-2", "IL-6", "TNF-α", "IFN-γ"]

# 访问元素（从0开始数！）
print(cytokines[0])   # 输出: IL-2
print(cytokines[2])   # 输出: TNF-α

# 添加元素
cytokines.append("IL-10")
print(cytokines)      # 输出: ['IL-2', 'IL-6', 'TNF-α', 'IFN-γ', 'IL-10']

# 列表长度
print(len(cytokines)) # 输出: 5

# 循环遍历
for c in cytokines:
    print(c)
```

!!! warning "索引从0开始！"
    电脑世界从0开始数，不是从1。  
    `cytokines[0]` 是第一个，`cytokines[3]` 是第四个。

---

## 4.2 字典（Dict）

字典是**键值对**——像查真实字典一样，给"词"得"义"。

```python
# 创建一个字典
patient = {
    "name": "张三",
    "age": 45,
    "diagnosis": "类风湿关节炎",
    "CRP": 45.6
}

# 访问值
print(patient["name"])     # 输出: 张三
print(patient["CRP"])      # 输出: 45.6

# 修改值
patient["CRP"] = 32.1

# 添加新键
patient["ESR"] = 56       # 血沉

# 遍历字典
for key, value in patient.items():
    print(key + "：" + str(value))
```

### 医学类比

> 字典 = 一份病历
> - 键 = 字段名（姓名、诊断、检查值）
> - 值 = 具体的数值/文字

---

## 4.3 列表 vs 字典 对比

| | 列表 | 字典 |
|--|------|------|
| 访问方式 | 用索引号 `[0]`, `[1]` | 用键名 `["name"]` |
| 适合场景 | 一堆同类数据 | 有标签的数据 |
| 例子 | 所有患者的体温列表 | 一个患者的完整信息 |

```python
# 列表适合：一组数值
all_temps = [36.5, 38.2, 37.1, 39.5]

# 字典适合：多维数据
patient_1 = {
    "temp": 38.2,
    "CRP": 45.6,
    "WBC": 11.2
}
```

---

## 4.4 嵌套结构（很实用！）

真实数据往往是嵌套的：

```python
# 多个患者的信息
patients = [
    {"name": "张三", "temp": 38.2, "diagnosis": "类风湿关节炎"},
    {"name": "李四", "temp": 36.5, "diagnosis": "系统性红斑狼疮"},
    {"name": "王五", "temp": 39.1, "diagnosis": "感染"}
]

# 找出所有发热患者
for p in patients:
    if p["temp"] > 37.3:
        print(p["name"] + "发热，诊断：" + p["diagnosis"])
```

---

## 4.5 动手练习

### 练习：管理你的实验样本

```python
# 创建一个样本库
samples = []

# 添加样本
samples.append({"id": "S001", "type": "血清", "volume": 1.5, "date": "2026-06-01"})
samples.append({"id": "S002", "type": "血浆", "volume": 2.0, "date": "2026-06-01"})
samples.append({"id": "S003", "type": "血清", "volume": 0.8, "date": "2026-06-02"})

# 显示所有样本
for s in samples:
    print(s["id"] + " | " + s["type"] + " | " + str(s["volume"]) + "mL | " + s["date"])

# 统计总量
total_volume = 0
for s in samples:
    total_volume = total_volume + s["volume"]
print("总体积：" + str(total_volume) + " mL")
```

---

## 📋 本章检查清单

- [ ] 我会创建和访问列表（索引从0开始）
- [ ] 我会用 `.append()` 给列表添加元素
- [ ] 我会创建和访问字典
- [ ] 我能区分"列表"和"字典"各自适合的场景
- [ ] 我能在字典中嵌套列表，或列表中嵌套字典
- [ ] 我完成了实验样本管理练习

---

## 🔜 下一章预告

第5章：函数与模块 —— 把常用代码打包，随时复用
