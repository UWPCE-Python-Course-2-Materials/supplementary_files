all: great_circle_v1.c great_circle_v2.c great_circle_v3.c great_circle_v1.html great_circle_v2.html great_circle_v3.html

great_circle_v1.c: great_circle_v1.pyx great_circle_setup_v1.py
	python great_circle_setup_v1.py build_ext --inplace

great_circle_v1.html: great_circle_v1.pyx
	cython -a great_circle_v1.pyx

great_circle_v2.c: great_circle_v2.pyx great_circle_setup_v2.py
	python great_circle_setup_v2.py build_ext --inplace

great_circle_v2.html: great_circle_v2.pyx
	cython -a great_circle_v2.pyx

great_circle_v3.c: great_circle_v3.pyx great_circle_setup_v3.py
	python great_circle_setup_v3.py build_ext --inplace

great_circle_v3.html: great_circle_v3.pyx
	cython -a great_circle_v3.pyx
