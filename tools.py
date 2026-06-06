"""
AI Table Builder - AI表格构建器工具
支持表格设计、数据绑定、交互功能
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class AITableBuilderTools:
    """
    AI表格构建器工具
    支持：设计、数据绑定、交互
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def design_table(self, data_type: str, columns: List[str]) -> Dict:
        """设计表格"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        columns_text = ", ".join(columns)

        prompt = f"""请设计{data_type}表格：

列：{columns_text}

请返回JSON格式：
{{
    "columns": [
        {{"name": "列名", "type": "类型", "width": "宽度", "sortable": true/false}}
    ],
    "features": ["功能"],
    "actions": ["操作"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"table": content}

    def generate_table_code(self, table_config: Dict, framework: str = "react") -> str:
        """生成表格代码"""
        if not self.client:
            return "LLM客户端未配置"

        config_text = json.dumps(table_config, ensure_ascii=False)

        prompt = f"""请生成{framework}表格代码：

配置：{config_text}

要求：
1. TanStack Table
2. 排序、筛选、分页
3. 行选择
4. 导出功能"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=3000
        )

        return response.choices[0].message.content

    def generate_excel_export(self, data_schema: Dict) -> str:
        """生成Excel导出"""
        if not self.client:
            return "LLM客户端未配置"

        schema_text = json.dumps(data_schema, ensure_ascii=False)

        prompt = f"""请生成Excel导出代码：

数据Schema：{schema_text}

要求：
1. openpyxl
2. 样式美化
3. 数据验证
4. 图表支持"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def design_data_grid(self, features: List[str]) -> Dict:
        """设计数据网格"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        features_text = ", ".join(features)

        prompt = f"""请设计数据网格：

功能：{features_text}

请返回JSON格式：
{{
    "components": ["组件"],
    "interactions": ["交互"],
    "performance": "性能优化",
    "tools": ["推荐工具"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"data_grid": content}

    def generate_pivot_table(self, data_description: str) -> str:
        """生成透视表"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请生成透视表代码：

数据：{data_description}

要求：
1. 行列分组
2. 聚合计算
3. 钻取功能
4. 可视化"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def optimize_table_performance(self, data_size: str, features: List[str]) -> Dict:
        """优化表格性能"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        features_text = ", ".join(features)

        prompt = f"""请优化表格性能：

数据量：{data_size}
功能：{features_text}

请返回JSON格式：
{{
    "techniques": ["优化技术"],
    "virtualization": "虚拟滚动",
    "lazy_loading": "懒加载",
    "caching": "缓存策略"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"optimization": content}


def create_tools(**kwargs) -> AITableBuilderTools:
    """创建表格构建器工具"""
    return AITableBuilderTools(**kwargs)


if __name__ == "__main__":
    tools = create_tools()

    print("AI Table Builder Tools")
    print()

    # 测试
    table = tools.design_table("用户列表", ["ID", "姓名", "邮箱", "状态"])
    print(json.dumps(table, ensure_ascii=False, indent=2))
