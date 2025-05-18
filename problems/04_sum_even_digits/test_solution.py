import pytest
import importlib.util
import os

# Dynamically import the student's solution from the working directory
def import_from_working_directory(module_name, file_path):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

# Path to the working directory
WORKING_DIR = "working_directory"
solution_path = os.path.join(WORKING_DIR, "04_sum_even_digits.py")
student_solution = import_from_working_directory("sum_even_digits", solution_path)

@pytest.mark.parametrize(
    "inputs, expected",
    [
        ([2,3,5], 2),
        ([2,4,6],12),
        ([-1,5,3],0),
        ([],0)
    ]
)
def test_sum_even(inputs, expected):
    assert student_solution.sum_even_digits(inputs) == expected
