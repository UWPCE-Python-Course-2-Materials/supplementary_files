def loads_of_numbers():
    for number in range(1_000_000, 2_000_000):
        print("before yield")
        yield number
        print("after yield")


generator_number = loads_of_numbers()

print(f"number before next {generator_number}")
print(f"number after next {next(generator_number)}")
print(f"number after next {next(generator_number)}")
