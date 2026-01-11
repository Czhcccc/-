# create_marx_unit1_questions.py
import db

def main():
    db.ensure_tables()
    sample = [
        {
            "subject": "马克思主义原理",
            "unit": 1,
            "stem": "1. （ ）是中国特色社会主义最本质的特征和中国特色社会主义制度的最大优势。",
            "type": "single",
            "options": ["人民民主专政", "中国共产党的领导", "改革开放", "社会主义市场经济体制"],
            "answer": ["B"],
            "analysis": "中国共产党的领导是中国特色社会主义最本质的特征。"
        },
        {
            "subject": "马克思主义原理",
            "unit": 1,
            "stem": "2. 马克思主义的基本观点不包括下列哪项？",
            "type": "single",
            "options": ["唯物史观", "剩余价值学说", "阶级斗争学说", "社会达尔文主义"],
            "answer": ["D"],
            "analysis": "社会达尔文主义不是马克思主义基本观点。"
        },
        {
            "subject": "马克思主义原理",
            "unit": 1,
            "stem": "3. 下列哪些属于马克思主义关于社会发展的基本原理？（多选）",
            "type": "multi",
            "options": ["生产力与生产关系的矛盾运动", "经济基础决定上层建筑", "个人意志决定历史走向", "阶级斗争是历史发展的动力"],
            "answer": ["A","B","D"],
            "analysis": "生产力与生产关系矛盾、经济基础决定上层建筑、阶级斗争推动历史发展。"
        },
        {
            "subject": "马克思主义原理",
            "unit": 1,
            "stem": "4. 简述历史唯物主义的主要观点（简答题）。",
            "type": "text",
            "options": [],
            "answer": [],
            "analysis": "示例：历史唯物主义认为社会存在决定社会意识等。"
        },
        {
            "subject": "马克思主义原理",
            "unit": 1,
            "stem": "5. 下列关于阶级及阶级斗争的表述中，错误的是（ ）。",
            "type": "single",
            "options": ["阶级是以生产资料所有制为基础形成的社会集团", "阶级斗争在资本主义社会中起推动作用", "阶级斗争最终导致无阶级社会的实现", "阶级的存在与人的主观意识无关"],
            "answer": ["D"],
            "analysis": "阶级的形成包括客观经济基础和人的社会实践，不是完全与主观意识无关。"
        },
        {
            "subject": "马克思主义原理",
            "unit": 1,
            "stem": "6. 下列选项中，哪些可以视为无产阶级革命的条件？（多选）",
            "type": "multi",
            "options": ["无产阶级成为社会中的主要阶层", "资产阶级内部发生分裂", "国际环境发生革命浪潮", "工人阶级觉悟和组织程度提高"],
            "answer": ["B","D"],
            "analysis": "B 与 D 为常见的革命条件因素。"
        }
    ]

    n = db.import_questions_from_list(sample)
    print(f"Inserted {len(sample)} test questions into DB (import result: {n}).")
    qs = db.load_questions_filtered(subject="马克思主义原理", unit=1)
    print(f"DB currently has {len(qs)} questions for 马克思主义原理 / 单元1")

if __name__ == "__main__":
    main()
