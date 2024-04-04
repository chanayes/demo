def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            global result
            for _ in range(n):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator


@repeat(3)
def greet(a, b):
    print(f"Hello, {a + b}!")


greet(1, 2)


class DecoratorClass:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        # 在调用原始函数之前/之后执行的代码
        result = self.func(*args, **kwargs)
        # 在调用原始函数之后执行的代码
        return result


@DecoratorClass
def my_function():
    pass
