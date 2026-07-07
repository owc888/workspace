import pdfplumber
import os

pdf_dir = r"e:\workspace\code\workspace\做题程序\深圳辅警模拟卷"

for filename in sorted(os.listdir(pdf_dir)):
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(pdf_dir, filename)
        print(f"\n{'='*60}")
        print(f"文件: {filename}")
        print(f"{'='*60}")
        try:
            with pdfplumber.open(pdf_path) as pdf:
                first_page = pdf.pages[0]
                text = first_page.extract_text()
                if text:
                    print("前500字符:")
                    print(repr(text[:500]))
                else:
                    print("无法提取文本")
        except Exception as e:
            print(f"读取失败: {e}")