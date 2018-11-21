# 读写操作复制一个小文件

file_read = open("README")
file_write = open("README[复件]","w")

text = file_read.read()
print(text)
file_write.write(text)

file_read.close()
file_write.close()

# 大文件使用 readline 节省内存
file_read = open("README")
file_write = open("README[复件2]","w")

while True:

    text = file_read.readline()
    if not text:
        break
    file_write.write(text)

file_read.close()
file_write.close()