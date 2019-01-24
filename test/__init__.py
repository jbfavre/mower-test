#!/usr/bin/env python

import sys
import pytest

try:
    coverage_options = ['--cov=mower', '--cov-report', 'term']
except ImportError:
    coverage_options = []
try:
    import pylint
    pylint_options = ['--pylint ']
    pylint_options = []
except ImportError:
    pylint_options = []

pytest_options = ['-v']
pytest_options += coverage_options
pytest_options += pylint_options

pytest.main(pytest_options)
