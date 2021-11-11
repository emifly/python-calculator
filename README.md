# Python Calculator

The calculator understands simple calculations in a particular format: the keyword `calc`, a string that's one of `x`, `+`, `-`, `/`, `^` or `%` (the operation), an integer (first operand), and another integer (second operand). It can then compute the result of performing the operation on the two operands.

### Examples of valid calculations and their results
```bash
calc + 1 2      # Returns 3
calc / 5 2      # Returns 2.5
calc x 5 0      # Returns 0
```

## Installation

No packages required currently, only Python itself (version 3.6 or above). Just clone the repo and get started!

## Usage

```bash
# Run the file calculator.py without command line arguments
python calculator.py
```

You will be asked if you would like to specify a path for the file containing your calculations to be run. By default, it is assumed that the calculations are contained in a file called `calculations.txt` in the current directory unless specified otherwise. Each calculation should be on a separate line.
