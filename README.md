# Python Practice

This repository contains a collection of Python exercises designed to help learners practice and improve their programming skills. Each exercise focuses on a specific concept or problem-solving technique, making it ideal for beginners and intermediate Python developers.

---

## Features

- **Structured Exercises**: Each exercise includes a description, starter code, and test cases.
- **Test-Driven Development (TDD)**: Use `pytest` to validate your solutions against predefined test cases.
- **Prompt Generation**: If you're stuck, the CLI tool can generate a detailed prompt to help you seek assistance from an AI agent.
- **Clipboard Integration**: Prompts are automatically copied to your clipboard for convenience.

---

## Repository Structure

```
Python_Practice/
├── cli.py                 # Command-line interface for managing exercises
├── problems/              # Directory containing all exercises
│   ├── 01_two_sum/        # Example exercise: Two Sum
│   │   ├── README.md      # Exercise description
│   │   ├── solution.py    # Example solution
│   │   ├── solution_template.py # Starter code for the exercise
│   │   └── test_solution.py     # Test cases for the exercise
│   ├── 03_sum_odd_digits/ # Example exercise: Sum of Odd Digits
│   │   ├── README.md      # Exercise description
│   │   ├── solution.py    # Example solution
│   │   ├── solution_template.py # Starter code for the exercise
│   │   └── test_solution.py     # Test cases for the exercise
├── working_directory/     # Temporary directory for active exercises
├── requirements.txt       # Python dependencies
└── README.md              # Repository overview
```

---

## Getting Started

### Prerequisites

- Python 3.6 or higher
- `pip` (Python package manager)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/python-practice.git
   cd python-practice
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### CLI Commands

The repository includes a CLI tool (`cli.py`) to manage exercises. Below are the available commands:

1. **List Exercises**:
   ```bash
   python cli.py list
   ```
   Lists all available exercises.

2. **Start an Exercise**:
   ```bash
   python cli.py start <exercise_name>
   ```
   Copies the starter code for the specified exercise to the `working_directory`.

3. **Test an Exercise**:
   ```bash
   python cli.py test <exercise_name>
   ```
   Runs the test cases for the specified exercise using `pytest`.

4. **Show Solution**:
   ```bash
   python cli.py solution <exercise_name>
   ```
   Displays the solution for the specified exercise.

5. **Show Description**:
   ```bash
   python cli.py description <exercise_name>
   ```
   Displays the description of the specified exercise.

6. **Generate Prompt**:
   ```bash
   python cli.py prompt <exercise_name>
   ```
   Generates a detailed prompt for the exercise and copies it to your clipboard. You can then paste it into your preferred LLM.

---

## Contributing

Contributions are welcome! If you have ideas for new exercises or improvements, feel free to open an issue or submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


Happy coding! 🚀
