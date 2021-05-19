#  Function with C type defs

import math

def great_circle(double lon1, double lat1, double lon2, double lat2):
    cdef double a, b, theta, c, x, radius

    radius = 3956  # miles
    x = math.pi / 180.0
    a = (90.0 - lat1) * (x)
    b = (90.0 - lat2) * (x)
    theta = (lon2 - lon1) * (x)
    c = math.acos((math.cos(a) * math.cos(b)) + (math.sin(a) * math.sin(b) * math.cos(theta)))
    return radius * c
