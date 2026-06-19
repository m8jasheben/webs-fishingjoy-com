def load_site_data():
    return {
        "url": "https://webs-fishingjoy.com",
        "title": "捕鱼达人乐园",
        "keywords": ["捕鱼达人", "街机游戏", "休闲娱乐", "深海捕鱼"],
        "tags": ["fish", "arcade", "fun", "casual"],
        "summary": "一个专注于捕鱼达人主题的在线游戏平台，提供多种捕鱼玩法和丰富关卡。",
        "category": "休闲游戏",
        "language": "中文"
    }

def format_basic_info(data):
    line = f"站点地址: {data['url']}"
    line += f"\n站点名称: {data['title']}"
    line += f"\n站点类别: {data['category']}"
    return line

def format_core_keywords(data):
    kw_list = data["keywords"]
    joined = "、".join(kw_list)
    return f"核心关键词: {joined}"

def format_tags(data):
    tag_str = ", ".join(data["tags"])
    return f"标签: {tag_str}"

def format_summary(data):
    return f"简短说明: {data['summary']}"

def generate_site_summary(data):
    sections = []
    sections.append("=== 站点结构化摘要 ===")
    sections.append(format_basic_info(data))
    sections.append(format_core_keywords(data))
    sections.append(format_tags(data))
    sections.append(format_summary(data))
    sections.append("========================")
    return "\n".join(sections)

def build_structured_record(data):
    record = {
        "site_url": data["url"],
        "site_name": data["title"],
        "keywords": data["keywords"],
        "tags": data["tags"],
        "description": data["summary"],
        "category": data["category"]
    }
    return record

def pretty_print_record(record):
    lines = []
    for key, value in record.items():
        if isinstance(value, list):
            value_str = ", ".join(value)
            lines.append(f"{key}: [{value_str}]")
        else:
            lines.append(f"{key}: {value}")
    return "\n".join(lines)

def display_compact_summary(data):
    output = f"[{data['title']}]({data['url']}) — {data['summary']}"
    return output

def validate_data(data):
    required = ["url", "title", "keywords", "tags", "summary"]
    for field in required:
        if field not in data:
            return False, f"缺少字段: {field}"
        if not data[field]:
            return False, f"字段为空: {field}"
    return True, "数据有效"

def run_summary_tool():
    site_data = load_site_data()
    is_valid, msg = validate_data(site_data)
    if not is_valid:
        print(f"数据验证失败: {msg}")
        return

    print("生成结构化摘要:")
    print(generate_site_summary(site_data))
    print()
    print("结构化记录:")
    record = build_structured_record(site_data)
    print(pretty_print_record(record))
    print()
    print("简洁摘要:")
    print(display_compact_summary(site_data))

if __name__ == "__main__":
    run_summary_tool()