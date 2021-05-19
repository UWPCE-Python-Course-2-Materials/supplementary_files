# really_simple.py
def my_fun():
    for i in range(1, 500):
        123 / (50 - i)

def secret_print(n):
    print("HERE!")
    print(n)

if __name__ == '__main__':
    secret_print(5)
    my_fun()