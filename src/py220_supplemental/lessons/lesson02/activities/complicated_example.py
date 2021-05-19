# complicated_example.py
def main():
    x = 'main'
    one()

def one():
    y = 'one'
    two()

def two():
    z = 'two'
    long_loop()

def long_loop():
    for i in range(2, int(1e03), 5):
        for j in range(3, int(1e03), 7):
            for k in range(12, int(1e03)):

                z = k / (i % k + j % k)
                secret_print(z)

def secret_print(num):
    num

if __name__ == '__main__':
    print(main())
    print("last statement")