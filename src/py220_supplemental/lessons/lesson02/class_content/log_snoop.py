# pip install loguru

from loguru import logger
import pysnooper

logger.remove()  # eliminate default to add our own

class Memoize:

    def __init__(self, fn):
        self.fn = fn
        self.memo = {}

    @pysnooper.snoop()
    def __call__(self, *args):
        if args not in self.memo:
            logger.info(f"args not in {args}")
            self.memo[args] = self.fn(*args)
        else:
            logger.info(f"args are in {args}")

        return self.memo[args]


@Memoize
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def main():
    fib(10)
    fib(35)
    fib(20)
    fib(11)


if __name__ == "__main__":
    main()
