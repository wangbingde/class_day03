# 模块导入
import ex_06
from ex_07 import Cat
from ex_07 import say_hello
from ex_06 import say_hello as module1

ex_06.say_hello()
say_hello()
module1()


dog = ex_06.Dog()
cat = Cat()
print(dog)
print(cat)
print(ex_06.__file__)