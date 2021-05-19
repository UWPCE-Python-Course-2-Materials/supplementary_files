#  Function with calls to C rather than Python math libraries

cdef extern from "math.h":
    float cosf(float theta)
    float sinf(float theta)
    float acosf(float theta)


def great_circle(double lon1, double lat1, double lon2, double lat2):
    cdef double a, b, theta, c, x, radius
    cdef double pi = 3.141592653589793

    radius = 3956  # miles
    x = pi / 180.0
    a = (90.0 - lat1) * (x)
    b = (90.0 - lat2) * (x)
    theta = (lon2 - lon1) * (x)
    c = acosf((cosf(a) * cosf(b)) + (sinf(a) * sinf(b) * cosf(theta)))
    return radius * c
