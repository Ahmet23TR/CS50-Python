def my_decorator(func):
    def wrapper():
        print("Fonksiyondan önce çalışan kod.")
        func()
        print("Fonksiyondan sonra çalışan kod.")
    return wrapper

@my_decorator
def say_hello():
    print("Merhaba!")

say_hello()
