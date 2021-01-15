def deco(func):
    # 일종의 함수를 정의해주는 함수
    # 이 래퍼함수는 인자로서 *args, **kwargs를 받는다고 가정한다.
    def wrapper(*a, **b):
        print("Hello")
        func(*a, **b)

    return wrapper


@deco
def simple_func(name):
    print(f"my name is {name}")


# deco_func=deco(simple_func) #함수를 새로 정의함

simple_func("Jeong")  # deco함수가 wrapper를 리터하므로 wrapper("Jeong")과 같다.
# print(deco_func)
# @deco

# simple_func()
