with open(r"e:\workspace\code\workspace\做题程序\extracted_text.txt", 'r', encoding='utf-8') as f:
    content = f.read()

try:
    gong_an_section = content.split("文件: 2026年深圳底十四批辅警笔试[公安]模拟卷2.pdf")[1]
    gong_an_section = gong_an_section.split("文件 2026年深圳底十四批辅警笔试[公安]模拟卷2.pdf 读取完成")[0]
    
    print("=== 模拟卷2前1000字符 ===")
    print(repr(gong_an_section[:1000]))
    
    print("\n=== 查找章节标记 ===")
    print("'二、多选题' in section:", '二、多选题' in gong_an_section)
    print("'二、多项选择题' in section:", '二、多项选择题' in gong_an_section)
    print("'三、判断题' in section:", '三、判断题' in gong_an_section)
    
    print("\n=== 单选题部分 ===")
    single_section = gong_an_section.split("二、多选题")[0] if '二、多选题' in gong_an_section else gong_an_section.split("二、多项选择题")[0] if '二、多项选择题' in gong_an_section else gong_an_section
    print("单选题部分长度:", len(single_section))
    print("前500字符:", repr(single_section[:500]))
    
except IndexError as e:
    print(f"Error: {e}")