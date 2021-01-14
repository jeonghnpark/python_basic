import datetime


class datetimedeco:
    def __init__(self, f):
        self.ff = f

    def __call__(self, *args, **kwargs):
        print(datetime.datetime.now())
        result=self.ff(*args, **kwargs)
        print(datetime.datetime.now())
        return result

class MainClass:
    @datetimedeco
    def func(self):
        print("Main function~")

    def sub_func(self):
        print("sub function")


obj = MainClass()

obj.func()
# obj.sub_func()
