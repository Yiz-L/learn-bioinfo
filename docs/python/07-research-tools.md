# 第7章：实战——科研小工具

> 学习目标：用前6章的知识，做出几个真正有用的科研工具！

---

## 🛠️ 项目1：ELISA数据处理助手

ELISA实验会得到一系列OD值，你需要计算标准曲线、反推浓度。

```python
def elisa_analysis():
    """简单的ELISA数据分析"""
    print("=== ELISA数据处理助手 ===")
    print("请输入标准品OD值（用逗号分隔）：")
    std_input = input()
    std_values = [float(x) for x in std_input.split(",")]
    
    std_concs = [0, 10, 50, 100, 500, 1000]  # pg/mL
    
    print("请输入样品OD值（用逗号分隔）：")
    sample_input = input()
    sample_values = [float(x) for x in sample_input.split(",")]
    
    print("\n📊 样品分析结果：")
    for i, od in enumerate(sample_values):
        ratio = od / std_values[-1]
        est_conc = ratio * std_concs[-1]
        print(f"  样品{i+1}: OD={od:.3f}, 估计浓度={est_conc:.1f} pg/mL")

if __name__ == "__main__":
    elisa_analysis()
```

---

## 🛠️ 项目2：文献笔记管理器

读完文献后快速记录要点：

```python
import datetime

def add_paper_note():
    """添加一篇文献笔记"""
    title = input("文献标题：")
    author = input("第一作者：")
    year = input("发表年份：")
    key_finding = input("核心发现：")
    
    with open("文献笔记.md", "a", encoding="utf-8") as f:
        f.write(f"\n## {title} ({year})\n")
        f.write(f"- **作者**：{author}\n")
        f.write(f"- **核心发现**：{key_finding}\n")
        f.write(f"- **记录时间**：{datetime.date.today()}\n")
        f.write("---\n")
    
    print("✅ 文献笔记已保存！")

def list_papers():
    """查看所有文献笔记"""
    try:
        with open("文献笔记.md", "r", encoding="utf-8") as f:
            print(f.read())
    except FileNotFoundError:
        print("还没有文献笔记，开始添加第一篇吧！")

# 主菜单
while True:
    print("\n=== 文献笔记管理器 ===")
    print("1. 添加文献笔记")
    print("2. 查看所有笔记")
    print("3. 退出")
    choice = input("请选择：")
    
    if choice == "1":
        add_paper_note()
    elif choice == "2":
        list_papers()
    elif choice == "3":
        print("再见！")
        break
    else:
        print("无效选择，请重试")
```

---

## 🛠️ 项目3：实验样本追踪系统

```python
# 样本数据库
sample_db = []

def add_sample():
    """添加新样本"""
    sid = input("样本ID：")
    stype = input("样本类型（血清/血浆/组织）：")
    volume = float(input("体积(mL)："))
    location = input("存放位置（如：-80℃冰箱A排3）：")
    
    sample = {
        "id": sid,
        "type": stype,
        "volume": volume,
        "location": location
    }
    sample_db.append(sample)
    print("✅ 样本已添加")

def search_sample():
    """查找样本"""
    keyword = input("输入搜索关键词（ID/类型）：")
    found = [s for s in sample_db if keyword in s["id"] or keyword in s["type"]]
    
    if found:
        print(f"\n找到 {len(found)} 个样本：")
        for s in found:
            print(f"  {s['id']} | {s['type']} | {s['volume']}mL | {s['location']}")
    else:
        print("未找到匹配样本")

def show_summary():
    """显示统计摘要"""
    total = len(sample_db)
    total_vol = sum(s["volume"] for s in sample_db)
    types = {}
    for s in sample_db:
        types[s["type"]] = types.get(s["type"], 0) + 1
    
    print(f"\n📊 样本库摘要")
    print(f"总样本数：{total}")
    print(f"总体积：{total_vol:.1f} mL")
    print("按类型分布：")
    for t, c in types.items():
        print(f"  {t}：{c}个")
```

---

## 💡 每完成一个项目，对照自查

| 项目 | 用到了前几章的哪些知识 |
|------|----------------------|
| ELISA数据处理 | 变量、列表、输入输出、运算 |
| 文献笔记管理器 | 函数、文件读写、while循环、字典 |
| 样本追踪系统 | 列表嵌套字典、循环、函数、条件判断 |

---

## 📋 本章检查清单

- [ ] 我运行了ELISA数据处理助手并测试
- [ ] 我使用文献笔记管理器添加了一篇笔记
- [ ] 我尝试了样本追踪系统的添加和搜索
- [ ] 我能看懂每个项目里每一行代码的作用
- [ ] 我尝试修改了其中一个项目的功能

---

## 🎉 Python基础篇完结！

你已经走完了Python入门的所有核心章节。接下来可以：
- 进入 **R语言学习路径** 继续学习
- 或者在 **学习笔记** 中记录你的踩坑心得
- 更新 **任务管理** 中的学习进度

> **记住：编程是练出来的，不是看出来的。每段代码都亲手敲一遍！**

---

[← 上一章：文件与数据](06-files-data.md) | [📖 返回目录](index.md) | [继续 → R语言学习路径](../r-language/index.md)
