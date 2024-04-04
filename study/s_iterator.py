lst = [1, 2, 3, 4]
it = iter(lst)
print(type(it))
print(it)

lst = [1, 2, 3, 4]
it = iter(lst)
for x in it:
    print(x, end=" ")

import sys  # 引入 sys 模块

it = iter([1, 2, 3, 4])  # 创建迭代器对象
while True:
    try:
        print(next(it))
    except StopIteration:
        print(StopIteration)
        sys.exit()


# 创建一个迭代器
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)
