#!/bin/sh 
coverage run test.py
coverage run sacl2.py
coverage repot *.py
coverage annootate *.py
cat *cover
