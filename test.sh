#!/bin/sh 
coverage run test.py
coverage run sacl2.py
coverage report *.py
coverage annotate *.py
cat *cover
