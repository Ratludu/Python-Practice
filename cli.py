from argparse import ArgumentParser
import os
import shutil
import subprocess

EXERCISES_DIR = "problems"
WORKING_DIR = "working_directory"

def list_exercises():
    """List all available exercises."""
    if not os.path.exists(EXERCISES_DIR):
        print("No exercises directory found.")
        return
    exercises = [d for d in os.listdir(EXERCISES_DIR) if os.path.isdir(os.path.join(EXERCISES_DIR, d))]
    if exercises:
        print("Available exercises:")
        for exercise in exercises:
            print(f"- {exercise}")
    else:
        print("No exercises available.")

def start_exercise(exercise_name):
    """Copy the starter code for the specified exercise to the working directory."""
    exercise_path = os.path.join(EXERCISES_DIR, exercise_name)
    if not os.path.exists(exercise_path):
        print(f"Exercise '{exercise_name}' does not exist.")
        return
    starter_file = os.path.join(exercise_path, "solution_template.py")
    if not os.path.exists(starter_file):
        print(f"No starter file found for exercise '{exercise_name}'.")
        return
    os.makedirs(WORKING_DIR, exist_ok=True)
    destination_file = os.path.join(WORKING_DIR, f"{exercise_name}.py")
    shutil.copy(starter_file, destination_file)
    print(f"Starter code for '{exercise_name}' copied to '{destination_file}'.")

def test_exercise(exercise_name):
    """Run the tests for the specified exercise."""
    exercise_path = os.path.join(EXERCISES_DIR, exercise_name)
    if not os.path.exists(exercise_path):
        print(f"Exercise '{exercise_name}' does not exist.")
        return
    test_file = os.path.join(exercise_path, "test_solution.py")
    if not os.path.exists(test_file):
        print(f"No test file found for exercise '{exercise_name}'.")
        return
    result = subprocess.run(["pytest", test_file], capture_output=True, text=True)
    print(result.stdout)

def show_solution(exercise_name):
    """Display the solution for the specified exercise."""
    exercise_path = os.path.join(EXERCISES_DIR, exercise_name)
    if not os.path.exists(exercise_path):
        print(f"Exercise '{exercise_name}' does not exist.")
        return
    solution_file = os.path.join(exercise_path, "solution.py")
    if not os.path.exists(solution_file):
        print(f"No solution file found for exercise '{exercise_name}'.")
        return
    with open(solution_file, "r") as f:
        print(f.read())

def show_description(exercise_name):
    """Display the readme for the specified exercise."""
    exercise_path = os.path.join(EXERCISES_DIR, exercise_name)
    if not os.path.exists(exercise_path):
        print(f"Exercise '{exercise_name}' does not exist.")
        return
    readme = os.path.join(exercise_path, "README.md")
    if not os.path.exists(readme):
        print(f"No description file found for exercise '{exercise_name}'.")
        return
    with open(readme, "r") as f:
        print(f.read())

def main():
    parser = ArgumentParser(description="CLI for managing Python exercises")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # List command
    subparsers.add_parser("list", help="List all available exercises")

    # Start command
    start_parser = subparsers.add_parser("start", help="Start an exercise")
    start_parser.add_argument("exercise_name", help="Name of the exercise to start")

    # Test command
    test_parser = subparsers.add_parser("test", help="Test an exercise")
    test_parser.add_argument("exercise_name", help="Name of the exercise to test")

    # Solution command
    solution_parser = subparsers.add_parser("solution", help="Show the solution for an exercise")
    solution_parser.add_argument("exercise_name", help="Name of the exercise to show the solution for")

    # description command
    desc_parser = subparsers.add_parser("description", help="Show the description for an exercise")
    desc_parser.add_argument("exercise_name", help="Name of the exercise to show the description for")

    args = parser.parse_args()

    if args.command == "list":
        list_exercises()
    elif args.command == "start":
        start_exercise(args.exercise_name)
    elif args.command == "test":
        test_exercise(args.exercise_name)
    elif args.command == "solution":
        show_solution(args.exercise_name)
    elif args.command == "description":
        show_description(args.exercise_name)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
