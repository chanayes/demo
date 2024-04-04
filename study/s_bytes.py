x = b"hello"
y = x[1:3]  # 切片操作，得到 b"el"
z = x + b"world"  # 拼接操作，得到 b"helloworld"

x = b"hello"
if x[0] == ord("h"):
    print("The first element is 'h'")

a = "1232323595959"
if (n := len(a)) > 10:
    print(f"List is too long ({n} elements, expected <= 10)")
