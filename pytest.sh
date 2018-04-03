#!/bin/sh

# export DATABASE_TEST_URL="sqlite://:memory:"

autopep8 . --recursive --in-place --pep8-passes 2000 --verbose

pytest -s -v
# pytest -s -v src/tests/test_read_only_query_views.py
# pytest -s -v src/tests/test_user_views.py

# find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
