def add(a,b):
    return a+b
def greet(name,greeting="你好"):
    return greeting+","+name
print(add(1,2))
print(greet("张三"))
print(greet("李四","早上好"))

def safe_divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "不能除以0"
print(safe_divide(1,2))
print(safe_divide(2,0))

def get_value(d,key):
    return d.get(key,"不存在")
person={"name":"张三"}
print(get_value(person,"name"))
print(get_value(person,"age"))