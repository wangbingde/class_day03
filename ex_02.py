# 异常——错误类型捕获
# 错误信息的最后一行的第一个单词，就是错误类型

try:
    num = int(input("请输入一个数字："))
    result = 8/num
    print(result)
except ZeroDivisionError:
    print("除0错误")
# except ValueError:
#     print("请输入整数")

# 捕获未知错误
except Exception as result_error:
    print("未知错误 %s" % result_error)

else:
    print("没有异常")

finally:
    print("无论是否有异常，都会执行")

print("-" * 50)