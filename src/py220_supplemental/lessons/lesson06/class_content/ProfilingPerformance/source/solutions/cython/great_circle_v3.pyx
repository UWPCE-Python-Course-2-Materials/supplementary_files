#  Function with calls to C math libraries and with factored functions


cdef extern from "math.h":
    float cosf(float theta)
    float sinf(float theta)
    float acosf(float theta)


cdef double calculate_x():
    cdef double pi = 3.141592653589793
    return pi / 180.0


cdef double calculate_coordinate(double lat, double x):
    return (90.0 - lat) * (x)


cdef double calculate_theta(double lon2, double lon1, double x):
    return (lon2 - lon1) * x


cdef double calculate_acos(double a, double b, double theta):
    return acosf((cosf(a) * cosf(b)) + (sinf(a) * sinf(b) * cosf(theta)))


def great_circle(double lon1, double lat1, double lon2, double lat2):
    cdef double a, b, theta, c, x, radius

    radius = 3956  # miles
    x = calculate_x()
    a = calculate_coordinate(lat1, x)
    b = calculate_coordinate(lat2, x)
    theta = calculate_theta(lon2, lon1, x)
    c = calculate_acos(a, b, theta)
    return radius * c
