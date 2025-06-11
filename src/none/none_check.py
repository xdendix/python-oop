def sayHello(name):
    if name is None:
        print("Nama kosong")
        return
    print(f"hello {name}")


sayHello("Dendi")
sayHello(None)


# pengecekan is not None

def sayHello2(name):
    if name is not None:
        print(f"hello {name}")
    else:
        print("Nama kosong")


sayHello2("Dendi")