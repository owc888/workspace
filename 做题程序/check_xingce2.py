import pdfplumber

pdf_path = r"e:\workspace\code\workspace\做题程序\深圳辅警模拟卷\2026年深圳底十四批辅警笔试[行测]模拟卷2.pdf"

with pdfplumber.open(pdf_path) as pdf:
    print(f"页数: {len(pdf.pages)}")
    for i, page in enumerate(pdf.pages[:3]):
        text = page.extract_text()
        if text:
            print(f"\n=== 第 {i+1} 页前1000字符 ===")
            print(repr(text[:1000]))
        else:
            print(f"\n=== 第 {i+1} 页 ===")
            print("无法提取文本")