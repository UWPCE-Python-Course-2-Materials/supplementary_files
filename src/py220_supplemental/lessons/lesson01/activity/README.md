# Calculator

## Instructions

Your assignment is to complete testing and linting on the calculator from the lesson videos.

There's one new addition since the videos: I've separated the unit tests and the integration tests into two separate test files.

## Your Goals

1. `python -m unittest integration-test` should have no failures. Don't edit integration-test.py, edit your code to make it pass.
2. Add unit tests to unit-test.py such that `coverage run --source=calculator -m unittest test_unit; coverage report` shows 100% coverage.
3. All of the tests in unit-test.py should pass.
4. Satisfy the linter such that `pylint calculator` gives no errors and `flake8 calculator` gives no errors. See (PEP257)[https://www.python.org/dev/peps/pep-0257/] if you'd like more information about docstrings. There are quite a few docstrings to add, but for this exercise you don't need to get too creative: """ this method adds two numbers """ is sufficient.

## Bonus goal
One of our specs for calculator says the following:

```
The add, subtract, multiply, and divide methods shall both:
Return the result of the operation
Enter the result of the operation back into the calculator
This makes it possible to perform the following sequences of operations:
  calculator.enter_number(2)
  calculator.enter_number(3)
  calculator.add()                      # Returns 5, and now 5 is now 'in the calculator'
  calculator.enter_number(1)
  calculator.subtract()               # Returns 4 because 5 - 1 = 4
```

This feature is tested by our integration test, but it is not tested in our unit tests. Because this sequencing of operations is a defined feature of calculator, it would definitely be appropriate to test in the unit-test.CalculatorTests. Your bonus goal is to use *MagicMock* to test this method sequencing feature in isolation. Ie: without relying on the correctness of any particular operator we use to initialize our calculator.

