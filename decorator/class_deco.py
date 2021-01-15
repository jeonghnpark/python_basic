# https://jupiny.com/2016/09/25/decorator-class/

class HelloWorld():
    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        print("Hello world")


hw = HelloWorld()
hw()

# decoration for calculation running time

import time


class Timer():
    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        result = self.function(*args, **kwargs)
        end_time = time.time()
        print(f"running time is {end_time - start_time} seconds")
        return result


@Timer
def print_hello(name):
    print("hello, " + name)


print_hello("python")


class Tagify():
    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        tagify_p = self.tagify('p', self.function(*args, **kwargs))
        tagify_b=self.tagify('b', tagify_p)
        tagify_i=self.tagify('i', tagify_b)
        return tagify_i

    def tagify(self, tag, text):
        return f"<{tag}>{text}</{tag}>"


@Tagify
def set_text(text):
    return text


print(set_text("string"))
