import pdfplumber
import os

pdf_dir = r"e:\workspace\code\workspace\做题程序\深圳辅警模拟卷"
output_file = r"e:\workspace\code\workspace\做题程序\extracted_text.txt"

with open(output_file, 'w', encoding='utf-8') as f:
    for filename in sorted(os.listdir(pdf_dir)):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(pdf_dir, filename)
            f.write(f"\n{'='*80}\n")
            f.write(f"文件: {filename}\n")
            f.write(f"{'='*80}\n")
            
            try:
                with pdfplumber.open(pdf_path) as pdf:
                    for i, page in enumerate(pdf.pages):
                        text = page.extract_text()
                        if text:
                            f.write(f"\n--- 第 {i+1} 页 ---\n")
                            f.write(text)
                            f.write("\n")
                f.write(f"\n{'='*80}\n")
                f.write(f"文件 {filename} 读取完成\n")
                f.write(f"{'='*80}\n")
            except Exception as e:
                f.write(f"读取失败: {e}\n")

print(f"所有内容已保存到 {output_file}")