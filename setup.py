from distutils.core import setup

setup(
    name="day_03_message",  # 包名
    version="1.0",  # 版本
    keywords=("send", "receive"),  # 关键字
    description="发送和接受信息模块",  # 描述
    long_description="发送和接受信息模块",  # 详细描述
    license="MIT Licence",

    url="http://test.com",
    author="test",
    author_email="test@gmail.com",
    py_modules=["day_03_message.send_message",
                "day_03_message.receive_message"])
