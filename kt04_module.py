def myfunction(a: int, b: int) -> int:
    c = a + b
    return c


def myfunc_2(x: int, y: int) -> int:
    d = x - y
    return d


if __name__ == "__main__":
    print(myfunc_2(16, 9))
    print(myfunction(17, 9))
    print("File name: ", __name__)
    print("File path: ", __file__)
else:
    print("File name: ", __name__)
    print("File path: ", __file__)
    print("Function cannot be executed, this line will print if you import this module")
