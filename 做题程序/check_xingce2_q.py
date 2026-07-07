import pdfplumber

pdf_path = r"e:\workspace\code\workspace\做题程序\深圳辅警模拟卷\2026年深圳底十四批辅警笔试[行测]模拟卷2.pdf"

with pdfplumber.open(pdf_path) as pdf:
    for i, page in enumerate(pdf.pages[4:7]):
        text = page.extract_text()
        if text:
            print(f"\n=== 第 {i+5} 页 ===")
            print(text[:2000])