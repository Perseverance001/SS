
# 输入txt文件路径
file_path = 'test.txt'

# 打开文件
with open(file_path,encoding='UTF-8') as f:
    lines = f.readlines()

# 删除空行
lines = [line for line in lines if line.strip()]

# 写入新文件
with open(file_path, 'w') as f:
    f.writelines(lines)

print('删除txt文件中空行完成！')
