# 📊 AI Table Builder

AI表格构建器工具，支持表格设计、数据绑定、交互功能。

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenAI-API-green?logo=openai" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

## ✨ 特性

- 🏗️ 表格设计
- 💻 表格代码生成
- 📗 Excel导出生成
- 📊 数据网格设计
- 📈 透视表生成
- ⚡ 性能优化

## 🚀 快速开始

```bash
pip install openai

python tools.py
```

## 📖 使用

```python
from ai_table_builder import create_tools

tools = create_tools()

# 表格设计
table = tools.design_table("用户列表", ["ID", "姓名", "邮箱"])

# 表格代码
code = tools.generate_table_code(table_config, "react")

# Excel导出
excel = tools.generate_excel_export(data_schema)

# 数据网格
grid = tools.design_data_grid(["排序", "筛选", "分页"])

# 透视表
pivot = tools.generate_pivot_table("销售数据")

# 性能优化
optimized = tools.optimize_table_performance("100万行", ["排序", "筛选"])
```

## 📁 项目结构

```
ai-table-builder/
├── tools.py       # 表格构建器工具核心
└── README.md
```

## 📄 许可证

MIT License
