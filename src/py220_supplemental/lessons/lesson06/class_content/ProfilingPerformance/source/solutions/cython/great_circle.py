#  great_circle.py
#
#  Import and runs different versions of the great circle function.
#
#    $ /usr/bin/time -p python great_circle.py
#    $ /usr/bin/time --verbose python great_circle.py

# from great_circle_v0 import great_circle
# from great_circle_v1 import great_circle
# from great_circle_v2 import great_circle
from great_circle_v3 import great_circle

lon1, lat1, lon2, lat2 = -72.345, 34.323, -61.823, 54.826

if __name__ == "__main__":

    for i in range(10000000):
        great_circle(lon1, lat1, lon2, lat2)
