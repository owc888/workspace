with open(r"e:\workspace\code\workspace\做题程序\extracted_text.txt", 'r', encoding='utf-8') as f:
    content = f.read()

xing_ce_section = content.split("文件: 2026年深圳底十四批辅警笔试[行测]模拟卷1.pdf")[1]
xing_ce_section = xing_ce_section.split("文件 2026年深圳底十四批辅警笔试[行测]模拟卷1.pdf 读取完成")[0]

print("=== 前2000字符 ===")
print(repr(xing_ce_section[:2000]))