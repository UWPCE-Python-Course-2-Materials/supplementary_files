#  Mastering Python High Performance
#  http://proquest.safaribooksonline.com.ezproxy.spl.org:2048/book/programming/python/9781783989300/pypy/ch06lvl2sec52_html?uicode=spl
#
#  Use timeit to compare pypy vs python performance:
#
#    $ pypy -m timeit -s 'main'
#    $ python -m timeit -s 'main'
#
#  Use /usr/bin/time to compare pypy vs python performance:
#
#    $ /usr/bin/time -p python great_circle.py
#    $ /usr/bin/time -p pypy great_circle.py
#
#    $ /usr/bin/time --verbose python great_circle.py
#    $ /usr/bin/time --verbose pypy great_circle.py
#
#    Note that for this to work you need to code loops / number
#    of trials into the code, probably in __main__

import math
lon1, lat1, lon2, lat2 = -72.345, 34.323, -61.823, 54.826


#  Function with no factorization
def great_circle_raw(lon1, lat1, lon2, lat2):
    radius = 3956  # miles
    x = math.pi / 180.0
    a = (90.0 - lat1) * (x)
    b = (90.0 - lat2) * (x)
    theta = (lon2 - lon1) * (x)
    c = math.acos((math.cos(a) * math.cos(b)) + (math.sin(a) * math.sin(b) * math.cos(theta)))
    return radius * c


#  Function with acos factored out to a function

def calculate_acos(a, b, theta):
    return math.acos((math.cos(a) * math.cos(b)) + (math.sin(a) * math.sin(b) * math.cos(theta)))


def great_circle_acos(lon1, lat1, lon2, lat2):
    radius = 3956  # miles
    x = math.pi / 180.0
    a = (90.0 - lat1) * (x)
    b = (90.0 - lat2) * (x)
    theta = (lon2 - lon1) * (x)
    # c = math.acos((math.cos(a) * math.cos(b)) + (math.sin(a) * math.sin(b) * math.cos(theta)))
    c = calculate_acos(a, b, theta)
    return radius * c


#  Great circle algorithm with most steps factored out as functions

def calculate_x():
    return math.pi / 180.0


def calculate_coordinate(lat, x):
    return (90.0 - lat) * x


def calculate_theta(lon2, lon1, x):
    return (lon2 - lon1) * x


def great_circle_factored(lon1, lat1, lon2, lat2):
    radius = 3956  # miles
    x = calculate_x()
    a = calculate_coordinate(lat1, x)
    b = calculate_coordinate(lat2, x)
    theta = calculate_theta(lon2, lon1, x)
    c = calculate_acos(a, b, theta)
    return radius * c


if __name__ == "__main__":

    # great_circle_raw(lon1, lat1, lon2, lat2)
    # great_circle_acos(lon1, lat1, lon2, lat2)
    # great_circle_factored(lon1, lat1, lon2, lat2)

    #  For use as follows:
    #    $ /usr/bin/time -p python great_circle.py
    #    $ /usr/bin/time -p pypy great_circle.py

    for i in range(10000000):
        # great_circle_raw(lon1, lat1, lon2, lat2)
        # great_circle_acos(lon1, lat1, lon2, lat2)
        # great_circle_factored(lon1, lat1, lon2, lat2)
