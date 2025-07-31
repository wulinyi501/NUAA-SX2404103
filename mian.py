def add(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("输入必须是整数")
    return a + b
print(add(2, 3))


