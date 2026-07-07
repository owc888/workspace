with open(r"e:\workspace\code\workspace\做题程序\questions.js", 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('const questions = ', '')
content = content.strip()
if content.endswith(';'):
    content = content[:-1].strip()

print(f"Content length: {len(content)}")
print(f"First 100 chars: {repr(content[:100])}")
print(f"Last 50 chars: {repr(content[-50:])}")

try:
    import json
    data = json.loads(content)
    print(f"\nSuccess! Total questions: {len(data)}")
    exams = {}
    types = {}
    for q in data:
        exams[q['exam']] = exams.get(q['exam'], 0) + 1
        types[q['type']] = types.get(q['type'], 0) + 1
    print("By exam:", exams)
    print("By type:", types)
except json.JSONDecodeError as e:
    print(f"\nJSON decode error: {e}")
    print(f"Error position: line {e.lineno}, column {e.colno}")
    lines = content.split('\n')
    if e.lineno <= len(lines):
        print(f"Problem line: {repr(lines[e.lineno-1])}")
        if e.lineno < len(lines):
            print(f"Next line: {repr(lines[e.lineno])}")