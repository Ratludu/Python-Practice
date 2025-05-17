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
solution_path = os.path.join(WORKING_DIR, "01_two_sum.py")
student_solution = import_from_working_directory("two_sum", solution_path)

@pytest.mark.parametrize(
    "inputs, expected",
    [
        ((5, 3), 8),          # Positive_1
        ((100, 50), 150),
        ((0.5,1.2), 1.7),
        ((None, None), 0)
    ]
)
def test_two_sum(inputs, expected):
    assert student_solution.two_sum(inputs[0], inputs[1]) == expected
