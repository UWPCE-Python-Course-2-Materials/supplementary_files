from mock import patch
from time import sleep


# pretend I am an external function; I am problematic to test
def calculate():
    sleep(10)
    return "y"


# I'm developing this; I use external function
def my_function():
    x = calculate()  # <- how to mock calculate() ?
    return x


def mytest():
    with patch("__main__.calculate") as calculate_mock:
        calculate_mock.return_value = "blah"
        assert my_function() == "blah"


def main():
    print("start running calculate")
    calculate()
    print("calculate done")

    print("now test calculate")
    mytest()
    print("done")


if __name__ == "__main__":
    main()
