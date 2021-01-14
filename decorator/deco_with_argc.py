
#None @version
def decorator(func):
    def decorator(*args, **kwargs):
        print("%s %s" % (func.__name__, "before"))
        func(*args, **kwargs)
        print("%s %s" % (func.__name__, "after"))
        return
    return decorator

# @decorator
def func(x,y):
    print(x+y)
    return x+y

func2=decorator(func)
func2(1,2)

#@version
def decorator_at(func):
    def decorator(*args, **kwargs):
        print("%s %s" % (func.__name__, "before"))
        result=func(*args, **kwargs)
        print("%s %s" % (func.__name__, "after"))
        return result
    return decorator

@decorator_at
def func_at(x,y):
    print(x+y)
    return x+y

func_at(1,2)
