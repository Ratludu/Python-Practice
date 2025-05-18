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
solution_path = os.path.join(WORKING_DIR, "06_is_decreasing.py")
student_solution = import_from_working_directory("is_decreasing", solution_path)

@pytest.mark.parametrize(
    "inputs, expected",
    [
        ([2,3,5], False),
        ([2,4,6],False),
        ([5,4,3],True),
        ([],True)
    ]
)
def test_is_increasing(inputs, expected):
    assert student_solution.is_increasing(inputs) == expected
