# 文件操作

# read方法读取文件内容
file = open("README")
text = file.read()
print(text)
file.close()
print("-" * 50)

# readline方法按行读取
file = open("README")

while True:

    text= file.readline()
    # 判断是否读取到内容
    if not text:
        break
    print(text)
file.close()