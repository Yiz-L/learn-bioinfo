# 第3章：条件与循环

> 学习目标：让程序做判断、让程序重复做事

---

## 3.1 条件判断：if

程序经常需要"看情况做事"——这就是条件判断。

```python
temperature = 38.5

if temperature > 37.3:
    print("发热")
else:
    print("体温正常")
```

### 医学类比

> 这就是你每天在临床做的诊断逻辑：
> - 如果 血糖 > 7.0 → 糖尿病
> - 否则 → 正常

### elif 多重判断

```python
crp = 45  # C反应蛋白

if crp < 10:
    print("正常")
elif crp < 50:
    print("轻度升高")
elif crp < 100:
    print("中度升高")
else:
    print("显著升高")
```

---

## 3.2 循环：for

当你要重复做一件事情时，用循环。

```python
# 打印5次
for i in range(5):
    print("第" + str(i + 1) + "次：免疫细胞在努力工作！")
```

输出：

```
第1次：免疫细胞在努力工作！
第2次：免疫细胞在努力工作！
第3次：免疫细胞在努力工作！
第4次：免疫细胞在努力工作！
第5次：免疫细胞在努力工作！
```

### 遍历列表

```python
cytokines = ["IL-2", "IL-6", "TNF-α", "IFN-γ"]

for cytokine in cytokines:
    print("检测到细胞因子：" + cytokine)
```

输出：

```
检测到细胞因子：IL-2
检测到细胞因子：IL-6
检测到细胞因子：TNF-α
检测到细胞因子：IFN-γ
```

---

## 3.3 循环：while

当你要"直到某个条件满足才停"时，用 while。

```python
# 发烧降温模拟
temp = 39.0
count = 0

while temp > 37.3:
    count = count + 1
    temp = temp - 0.3
    print("第" + str(count) + "次给药后体温：" + str(round(temp, 1)))

print("体温已恢复正常！")
```

---

## 3.4 动手练习

### 练习1：实验室结果判读

```python
# 根据淋巴细胞计数判断
lymph = float(input("请输入淋巴细胞计数(×10⁹/L)："))

if lymph < 0.8:
    print("淋巴细胞减少")
elif lymph < 1.0:
    print("轻度减少")
elif lymph < 4.0:
    print("正常范围")
else:
    print("淋巴细胞增多")
```

### 练习2：打印乘法表（巩固循环）

```python
for i in range(1, 10):
    for j in range(1, i + 1):
        print(str(j) + "×" + str(i) + "=" + str(i * j), end=" ")
    print()  # 换行
```

---

## 3.5 医学小剧场：批量处理患者数据

```python
patients = ["患者A", "患者B", "患者C", "患者D"]
temps = [36.5, 38.2, 37.1, 39.5]

for i in range(len(patients)):
    name = patients[i]
    t = temps[i]
    if t > 37.3:
        print(name + "：发热（" + str(t) + "℃）")
    else:
        print(name + "：体温正常（" + str(t) + "℃）")
```

---

## 📋 本章检查清单

- [ ] 我理解了 if/elif/else 的判断逻辑
- [ ] 我能用 for 循环遍历一组数据
- [ ] 我能用 while 做条件循环
- [ ] 我完成了实验室结果判读
- [ ] 我理解了循环在批量处理数据上的威力

---

---

[← 上一章：变量与数据](02-variables.md) | [📖 返回目录](index.md) | [下一章：数据结构 →](04-data-structures.md)
