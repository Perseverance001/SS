import pyperclip

def process_strings(str1, str2):
    str1 = str1[11:-12]
    str2 = str2[10:-11]
    result = str2 + ',' + str1
    return result

# 示例用法
print("请输入两行字符，用换行符分隔:")
for _ in range(999):
    input_str = ''
    for i in range(2):
        input_str += input() + '\n'

    input_lines = input_str.strip().split('\n')

    if len(input_lines) >= 2:
        output_str = process_strings(input_lines[0], input_lines[1])
        pyperclip.copy(output_str[1:])  # 将结果复制到剪贴板
        print("已将结果复制到剪贴板")
    else:
        print("输入的字符行数不足两行")
