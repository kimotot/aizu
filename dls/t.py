if __name__ == "__main__":

    def f1(a, b):
        return a + b


    def f2(a, b):
        return a - b

    flist = [f1, f2]

    for f in flist:
        print(f(100, 50))

