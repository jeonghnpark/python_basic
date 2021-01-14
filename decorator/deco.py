# https://bluese05.tistory.com/m/30
def trace(func):
    def wrapper():
        print(func.__name__, "function starts")
        func()
        print(func.__name__, "function ends")

    return wrapper  # 함수자체를 리턴함 wrapper() 가아님을 주의


@trace
def hello():
    print("hello")


@trace
def world():
    print("world")


# @를 쓰지 않는 방식
# trace_hello=trace(hello)
# trace_world=trace(world)
#
# trace_hello()
# trace_world()

# @를 쓰는 방식, 데코레이팅을 하는 순간 데코레이팅 없는 버전을 실행할 방법은 없나?
hello()
world()


def decorator1(func):
    def wrapper():
        print('deco1')
        func()

    return wrapper


def decorator2(func):
    def wrapper():
        print('deco2')
        func()

    return wrapper


# decorator 를 여러개 지정하기
@decorator1
@decorator2
def hello_decorated_by_1_2():
    print("hello deco1, deco2")

hello_decorated_by_1_2() #@ 없는 경우 decorator1(decorator2(hello))


#decorator with args, kwargs
