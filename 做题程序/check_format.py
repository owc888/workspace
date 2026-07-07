with open(r"e:\workspace\code\workspace\做题程序\extracted_text.txt", 'r', encoding='utf-8') as f:
    content = f.read()

gong_an_section = content.split("文件: 2026年深圳底十四批辅警笔试[公安]模拟卷1.pdf")[1]
gong_an_section = gong_an_section.split("文件 2026年深圳底十四批辅警笔试[公安]模拟卷1.pdf 读取完成")[0]

print("=== 前500字符 ===")
print(repr(gong_an_section[:500]))
print("\n=== 前1000字符 ===")
print(repr(gong_an_section[:1000]))