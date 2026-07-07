import re
import json

def parse_gong_an_moni1():
    questions = []
    with open(r"e:\workspace\code\workspace\做题程序\extracted_text.txt", 'r', encoding='utf-8') as f:
        content = f.read()
    
    gong_an_section = content.split("文件: 2026年深圳底十四批辅警笔试[公安]模拟卷1.pdf")[1]
    gong_an_section = gong_an_section.split("文件 2026年深圳底十四批辅警笔试[公安]模拟卷1.pdf 读取完成")[0]
    
    gong_an_answer = content.split("文件: 2026年深圳底十四批辅警笔试[公安]模拟卷1-答案.pdf")[1]
    gong_an_answer = gong_an_answer.split("文件 2026年深圳底十四批辅警笔试[公安]模拟卷1-答案.pdf 读取完成")[0]

    single_section = gong_an_section.split("二、多项选择题")[0]
    single_pattern = r'(\d+)．([\s\S]*?)(?=\n\d+．|\n二、多项选择题|$)'
    
    for m in re.finditer(single_pattern, single_section):
        q_num = int(m.group(1))
        if q_num < 1 or q_num > 50:
            continue
        
        full_text = m.group(2).strip()
        
        option_start = -1
        for opt in ['A.', 'B.', 'C.', 'D.']:
            idx = full_text.find(opt)
            if idx != -1:
                option_start = idx
                break
        
        if option_start == -1:
            continue
        
        stem = full_text[:option_start].strip()
        options_text = full_text[option_start:]
        
        options = {}
        for key in ['A', 'B', 'C', 'D']:
            next_options = [o for o in ['A.', 'B.', 'C.', 'D.'] if o != key + '.']
            pattern = key + r'\.(.*?)(?=' + '|'.join(next_options) + r'|$)'
            match = re.search(pattern, options_text, re.DOTALL)
            if match:
                options[key] = match.group(1).strip()
        
        if not options or len(options) < 2:
            continue
        
        answer_match = re.search(rf'{q_num}\.【答案】([A-Z]+)', gong_an_answer)
        answer = answer_match.group(1) if answer_match else ""
        
        explanation_match = re.search(rf'{q_num}\.【答案】[A-Z]+。解析：([\s\S]*?)(?=\n{q_num+1}\.|$)', gong_an_answer)
        explanation = explanation_match.group(1).strip() if explanation_match else ""
        
        questions.append({
            "id": q_num,
            "type": "single",
            "stem": stem,
            "options": options,
            "answer": answer,
            "explanation": explanation,
            "exam": "公安模拟卷1"
        })

    multi_section = gong_an_section.split("二、多项选择题")[1].split("三、判断题")[0]
    multi_pattern = r'(\d+)．([\s\S]*?)(?=\n\d+．|\n三、判断题|$)'
    
    for m in re.finditer(multi_pattern, multi_section):
        q_num = int(m.group(1))
        if q_num < 51 or q_num > 70:
            continue
        
        full_text = m.group(2).strip()
        
        option_start = -1
        for opt in ['A.', 'B.', 'C.', 'D.', 'E.']:
            idx = full_text.find(opt)
            if idx != -1:
                option_start = idx
                break
        
        if option_start == -1:
            continue
        
        stem = full_text[:option_start].strip()
        options_text = full_text[option_start:]
        
        options = {}
        for key in ['A', 'B', 'C', 'D', 'E']:
            next_options = [o for o in ['A.', 'B.', 'C.', 'D.', 'E.'] if o != key + '.']
            pattern = key + r'\.(.*?)(?=' + '|'.join(next_options) + r'|$)'
            match = re.search(pattern, options_text, re.DOTALL)
            if match:
                options[key] = match.group(1).strip()
        
        if not options or len(options) < 2:
            continue
        
        answer_match = re.search(rf'{q_num}\.【答案】([A-Z]+)', gong_an_answer)
        answer = answer_match.group(1) if answer_match else ""
        
        explanation_match = re.search(rf'{q_num}\.【答案】[A-Z]+。解析：([\s\S]*?)(?=\n{q_num+1}\.|$)', gong_an_answer)
        explanation = explanation_match.group(1).strip() if explanation_match else ""
        
        questions.append({
            "id": q_num,
            "type": "multiple",
            "stem": stem,
            "options": options,
            "answer": answer,
            "explanation": explanation,
            "exam": "公安模拟卷1"
        })

    judge_section = gong_an_section.split("三、判断题")[1]
    judge_pattern = r'(\d+)．([\s\S]*?)(?=\n\d+．|$)'
    
    for m in re.finditer(judge_pattern, judge_section):
        q_num = int(m.group(1))
        if q_num < 71 or q_num > 90:
            continue
        
        stem = m.group(2).strip()
        
        answer_match = re.search(rf'{q_num}\.【答案】([AB])', gong_an_answer)
        answer = answer_match.group(1) if answer_match else ""
        
        explanation_match = re.search(rf'{q_num}\.【答案】[AB]。解析：([\s\S]*?)(?=\n{q_num+1}\.|$)', gong_an_answer)
        explanation = explanation_match.group(1).strip() if explanation_match else ""
        
        questions.append({
            "id": q_num,
            "type": "judgment",
            "stem": stem,
            "options": {"A": "正确", "B": "错误"},
            "answer": answer,
            "explanation": explanation,
            "exam": "公安模拟卷1"
        })
    
    return questions

def parse_gong_an_moni2():
    questions = []
    with open(r"e:\workspace\code\workspace\做题程序\extracted_text.txt", 'r', encoding='utf-8') as f:
        content = f.read()
    
    gong_an_section = content.split("文件: 2026年深圳底十四批辅警笔试[公安]模拟卷2-答案.pdf")[1]
    gong_an_section = gong_an_section.split("文件 2026年深圳底十四批辅警笔试[公安]模拟卷2-答案.pdf 读取完成")[0]
    
    gong_an_answer = content.split("文件: 2026年深圳底十四批辅警笔试[公安]模拟卷2.pdf")[1]
    gong_an_answer = gong_an_answer.split("文件 2026年深圳底十四批辅警笔试[公安]模拟卷2.pdf 读取完成")[0]

    single_section = gong_an_section.split("二、多选题")[0]
    single_pattern = r'(\d+)．([\s\S]*?)(?=\n\d+．|\n二、多选题|$)'
    
    for m in re.finditer(single_pattern, single_section):
        q_num = int(m.group(1))
        if q_num < 1 or q_num > 50:
            continue
        
        full_text = m.group(2).strip()
        
        option_start = -1
        for opt in ['A.', 'B.', 'C.', 'D.']:
            idx = full_text.find(opt)
            if idx != -1:
                option_start = idx
                break
        
        if option_start == -1:
            continue
        
        stem = full_text[:option_start].strip()
        options_text = full_text[option_start:]
        
        options = {}
        for key in ['A', 'B', 'C', 'D']:
            next_options = [o for o in ['A.', 'B.', 'C.', 'D.'] if o != key + '.']
            pattern = key + r'\.(.*?)(?=' + '|'.join(next_options) + r'|$)'
            match = re.search(pattern, options_text, re.DOTALL)
            if match:
                options[key] = match.group(1).strip()
        
        if not options or len(options) < 2:
            continue
        
        answer_match = re.search(rf'{q_num}\.【答案】([A-Z]+)', gong_an_answer)
        answer = answer_match.group(1) if answer_match else ""
        
        explanation_match = re.search(rf'{q_num}\.【答案】[A-Z]+。解析：([\s\S]*?)(?=\n{q_num+1}\.|$)', gong_an_answer)
        explanation = explanation_match.group(1).strip() if explanation_match else ""
        
        questions.append({
            "id": q_num + 100,
            "type": "single",
            "stem": stem,
            "options": options,
            "answer": answer,
            "explanation": explanation,
            "exam": "公安模拟卷2"
        })

    multi_section = gong_an_section.split("二、多选题")[1].split("三、判断题")[0]
    multi_pattern = r'(\d+)．([\s\S]*?)(?=\n\d+．|\n三、判断题|$)'
    
    for m in re.finditer(multi_pattern, multi_section):
        q_num = int(m.group(1))
        if q_num < 51 or q_num > 70:
            continue
        
        full_text = m.group(2).strip()
        
        option_start = -1
        for opt in ['A.', 'B.', 'C.', 'D.', 'E.']:
            idx = full_text.find(opt)
            if idx != -1:
                option_start = idx
                break
        
        if option_start == -1:
            continue
        
        stem = full_text[:option_start].strip()
        options_text = full_text[option_start:]
        
        options = {}
        for key in ['A', 'B', 'C', 'D', 'E']:
            next_options = [o for o in ['A.', 'B.', 'C.', 'D.', 'E.'] if o != key + '.']
            pattern = key + r'\.(.*?)(?=' + '|'.join(next_options) + r'|$)'
            match = re.search(pattern, options_text, re.DOTALL)
            if match:
                options[key] = match.group(1).strip()
        
        if not options or len(options) < 2:
            continue
        
        answer_match = re.search(rf'{q_num}\.【答案】([A-Z]+)', gong_an_answer)
        answer = answer_match.group(1) if answer_match else ""
        
        explanation_match = re.search(rf'{q_num}\.【答案】[A-Z]+。解析：([\s\S]*?)(?=\n{q_num+1}\.|$)', gong_an_answer)
        explanation = explanation_match.group(1).strip() if explanation_match else ""
        
        questions.append({
            "id": q_num + 100,
            "type": "multiple",
            "stem": stem,
            "options": options,
            "answer": answer,
            "explanation": explanation,
            "exam": "公安模拟卷2"
        })

    judge_section = gong_an_section.split("三、判断题")[1]
    judge_pattern = r'(\d+)．([\s\S]*?)(?=\n\d+．|$)'
    
    for m in re.finditer(judge_pattern, judge_section):
        q_num = int(m.group(1))
        if q_num < 71 or q_num > 90:
            continue
        
        stem = m.group(2).strip()
        
        answer_match = re.search(rf'{q_num}\.【答案】([AB])', gong_an_answer)
        answer = answer_match.group(1) if answer_match else ""
        
        explanation_match = re.search(rf'{q_num}\.【答案】[AB]。解析：([\s\S]*?)(?=\n{q_num+1}\.|$)', gong_an_answer)
        explanation = explanation_match.group(1).strip() if explanation_match else ""
        
        questions.append({
            "id": q_num + 100,
            "type": "judgment",
            "stem": stem,
            "options": {"A": "正确", "B": "错误"},
            "answer": answer,
            "explanation": explanation,
            "exam": "公安模拟卷2"
        })
    
    return questions

def parse_xing_ce_moni1():
    questions = []
    with open(r"e:\workspace\code\workspace\做题程序\extracted_text.txt", 'r', encoding='utf-8') as f:
        content = f.read()
    
    xing_ce_section = content.split("文件: 2026年深圳底十四批辅警笔试[行测]模拟卷1.pdf")[1]
    xing_ce_section = xing_ce_section.split("文件 2026年深圳底十四批辅警笔试[行测]模拟卷1.pdf 读取完成")[0]
    
    xing_ce_answer = content.split("文件: 2026年深圳底十四批辅警笔试[行测]模拟卷1-答案.pdf")[1]
    xing_ce_answer = xing_ce_answer.split("文件 2026年深圳底十四批辅警笔试[行测]模拟卷1-答案.pdf 读取完成")[0]

    xing_ce_section = re.sub(r'_+', ' ', xing_ce_section)
    xing_ce_section = re.sub(r'--- 第 \d+ 页 ---', '', xing_ce_section)
    xing_ce_section = re.sub(r'第\d+页 共\d+页', '', xing_ce_section)
    xing_ce_section = re.sub(r'内部资料\s*免费交流', '', xing_ce_section)
    xing_ce_section = re.sub(r'《行政职业能力测验》', '', xing_ce_section)
    
    xing_ce_section = xing_ce_section.replace('请开始答题：', '')
    
    all_text = ''
    sections = re.split(r'(第[一二三四五六]部分\s+[\u4e00-\u9fa5]+)', xing_ce_section)
    for i in range(0, len(sections), 2):
        if i + 1 < len(sections):
            all_text += sections[i+1] + '\n' + sections[i]
        else:
            all_text += sections[i]
    
    pattern = r'(\d+)．([\s\S]*?)(?=\n\d+．|\Z)'
    
    for m in re.finditer(pattern, all_text):
        try:
            q_num = int(m.group(1))
        except:
            continue
        
        if q_num < 1 or q_num > 100:
            continue
        
        full_text = m.group(2).strip()
        
        option_start = -1
        for opt in ['A.', 'B.', 'C.', 'D.']:
            idx = full_text.find(opt)
            if idx != -1:
                option_start = idx
                break
        
        if option_start == -1:
            continue
        
        stem = full_text[:option_start].strip()
        options_text = full_text[option_start:]
        
        options = {}
        for key in ['A', 'B', 'C', 'D']:
            next_options = [o for o in ['A.', 'B.', 'C.', 'D.'] if o != key + '.']
            opt_pattern = key + r'\.(.*?)(?=' + '|'.join(next_options) + r'|$)'
            match = re.search(opt_pattern, options_text, re.DOTALL)
            if match:
                options[key] = match.group(1).strip()
        
        if not options or len(options) < 2:
            continue
        
        answer_match = re.search(rf'{q_num}\.【答案】([A-Z]+)', xing_ce_answer)
        answer = answer_match.group(1) if answer_match else ""
        
        explanation_match = re.search(rf'{q_num}\.【答案】[A-Z]+。解析：([\s\S]*?)(?=\n{q_num+1}\.|$)', xing_ce_answer)
        explanation = explanation_match.group(1).strip() if explanation_match else ""
        
        questions.append({
            "id": q_num + 200,
            "type": "single",
            "stem": stem,
            "options": options,
            "answer": answer,
            "explanation": explanation,
            "exam": "行测模拟卷1"
        })
    
    return questions

def parse_xing_ce_moni2():
    questions = []
    with open(r"e:\workspace\code\workspace\做题程序\extracted_text.txt", 'r', encoding='utf-8') as f:
        content = f.read()
    
    xing_ce_section = content.split("文件: 2026年深圳底十四批辅警笔试[行测]模拟卷2.pdf")[1]
    xing_ce_section = xing_ce_section.split("文件 2026年深圳底十四批辅警笔试[行测]模拟卷2.pdf 读取完成")[0]
    
    xing_ce_answer = content.split("文件: 2026年深圳底十四批辅警笔试[行测]模拟卷-答案.pdf")[1]
    xing_ce_answer = xing_ce_answer.split("文件 2026年深圳底十四批辅警笔试[行测]模拟卷-答案.pdf 读取完成")[0]

    xing_ce_section = re.sub(r'_+', ' ', xing_ce_section)
    xing_ce_section = re.sub(r'--- 第 \d+ 页 ---', '', xing_ce_section)
    xing_ce_section = re.sub(r'第\d+页 共\d+页', '', xing_ce_section)
    xing_ce_section = re.sub(r'内部资料\s*免费交流', '', xing_ce_section)
    xing_ce_section = re.sub(r'《行政职业能力测验》', '', xing_ce_section)
    
    xing_ce_section = xing_ce_section.replace('请开始答题：', '')
    
    all_text = ''
    sections = re.split(r'(第[一二三四五六]部分\s+[\u4e00-\u9fa5]+)', xing_ce_section)
    for i in range(0, len(sections), 2):
        if i + 1 < len(sections):
            all_text += sections[i+1] + '\n' + sections[i]
        else:
            all_text += sections[i]
    
    pattern = r'(\d+)．([\s\S]*?)(?=\n\d+．|\Z)'
    
    for m in re.finditer(pattern, all_text):
        try:
            q_num = int(m.group(1))
        except:
            continue
        
        if q_num < 1 or q_num > 100:
            continue
        
        full_text = m.group(2).strip()
        
        option_start = -1
        for opt in ['A.', 'B.', 'C.', 'D.']:
            idx = full_text.find(opt)
            if idx != -1:
                option_start = idx
                break
        
        if option_start == -1:
            continue
        
        stem = full_text[:option_start].strip()
        options_text = full_text[option_start:]
        
        options = {}
        for key in ['A', 'B', 'C', 'D']:
            next_options = [o for o in ['A.', 'B.', 'C.', 'D.'] if o != key + '.']
            opt_pattern = key + r'\.(.*?)(?=' + '|'.join(next_options) + r'|$)'
            match = re.search(opt_pattern, options_text, re.DOTALL)
            if match:
                options[key] = match.group(1).strip()
        
        if not options or len(options) < 2:
            continue
        
        answer_match = re.search(rf'{q_num}\.【答案】([A-Z]+)', xing_ce_answer)
        answer = answer_match.group(1) if answer_match else ""
        
        explanation_match = re.search(rf'{q_num}\.【答案】[A-Z]+。解析：([\s\S]*?)(?=\n{q_num+1}\.|$)', xing_ce_answer)
        explanation = explanation_match.group(1).strip() if explanation_match else ""
        
        questions.append({
            "id": q_num + 300,
            "type": "single",
            "stem": stem,
            "options": options,
            "answer": answer,
            "explanation": explanation,
            "exam": "行测模拟卷2"
        })
    
    return questions

def main():
    questions = []
    
    questions.extend(parse_gong_an_moni1())
    questions.extend(parse_gong_an_moni2())
    questions.extend(parse_xing_ce_moni1())
    questions.extend(parse_xing_ce_moni2())
    
    with open(r"e:\workspace\code\workspace\做题程序\questions.js", 'w', encoding='utf-8') as f:
        f.write("const questions = " + json.dumps(questions, ensure_ascii=False, indent=2) + ";\n")
    
    print(f"共生成 {len(questions)} 道题目")
    print("题目数据已保存到 questions.js")

if __name__ == "__main__":
    main()