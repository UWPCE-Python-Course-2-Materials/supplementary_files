# Timeit tutorial
# rriehle

from timeit import timeit as timer

my_repititions = 10000
my_range = 10000
my_lower_limit = my_range / 2

my_list = list(range(my_range))


def multiply_by_two(x):
    return x * 2


def greater_than_lower_limit(x):
    return x > my_lower_limit


print("\n\nmap_filter_with_functions")
# map_filter_with_functions = map(multiply_by_two, filter(greater_than_lower_limit, my_list))
# print(*map_filter_with_functions)
print(timer(
    'map_filter_with_functions = map(multiply_by_two, filter(greater_than_lower_limit, my_list))',
    globals=globals(),
    number=my_repititions
))

print("\n\nmap_filter_with_lambdas")
# map_filter_with_lambdas = map(lambda x: x * 2, filter(lambda x: x > my_lower_limit, my_list))
# print(*map_filter_with_lambdas)
print(timer(
    'map_filter_with_lambdas = map(lambda x: x * 2, filter(lambda x: x > my_lower_limit, my_list))',
    globals=globals(),
    number=my_repititions
))

print("\n\ncomprehension")
# comprehension = [x * 2 for x in my_list if x > my_lower_limit]
# print(*comprehension)
print(timer(
    'comprehension = [x * 2 for x in my_list if x > my_lower_limit]',
    globals=globals(),
    number=my_repititions
))

print("\n\ncomprehension_with_functions")
# comprehension_with_functions = [multiply_by_two(x) for x in my_list if greater_than_lower_limit(x)]
# print(*comprehension_with_functions)
print(timer(
    'comprehension_with_functions = [multiply_by_two(x) for x in my_list if greater_than_lower_limit(x)]',
    globals=globals(),
    number=my_repititions
))

print("\n\ncomprehension_with_lambdas")
# comprehension_with_lambdas = [lambda x: x * 2 for x in my_list if lambda x: x > my_lower_limit]
# comprehension_with_lambdas = [(lambda x: x * 2)(x) for x in my_list if (lambda x: x)(x) > my_lower_limit]
# print(*comprehension_with_lambdas)
print(timer(
    'comprehension_with_lambdas = [(lambda x: x * 2)(x) for x in my_list if (lambda x: x)(x) > my_lower_limit]',
    globals=globals(),
    number=my_repititions
))


#  Consider order of operations between the forms.
#  In map_filter_with_functions the filter is applied before the map expression
#  Is that true in the other variatins?
