#!/bin/sh 
python test.py
coverage run sacl2.py
coverage annotate sacl2.py
cat sacl2.py,cover
python test.py
coverage report sacl2.py
