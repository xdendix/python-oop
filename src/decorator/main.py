def my_decorator(func):
    def wrapper():
        print("Sebelum fungsi dieksekusi.")
        func()
        print("Setelah fungsi dieksekusi.")

    return wrapper


# Dekorasi fungsi dengan dekorator
@my_decorator
def say_hello():
    print("Hello, World!")


# Memanggil fungsi yang sudah didekorasi
say_hello()
