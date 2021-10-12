### Helper functions ###

def is_integer(potential_integer):
    try:
        int(potential_integer)
        return True
    except (ValueError, TypeError):
        return False

def print_aligned(content_before_colon, content_after_colon):
    print(f"{(content_before_colon + ':'):20s} {content_after_colon}")

### Calculation workings ###

operations = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    'x': lambda a, b: a * b,
    '/': lambda a, b: a / b,
    '^': lambda a, b: a ** b,
    '%': lambda a, b: a % b
}

valid_operations = '"' + '", "'.join(operations.keys()) + '"'

class Calculation:
    errors = []

    def __init__(self, calc_string):
        self.calc_elements = calc_string.split()
        self.set_errors()

        if len(self.errors) == 0:
            self.operation = operations[self.calc_elements[1]]
            self.operand_1 = int(self.calc_elements[2])
            self.operand_2 = int(self.calc_elements[3])

    def compute(self):
        if len(self.errors) > 0:
            raise ValueError(' | '.join(self.errors))
        return self.operation(self.operand_1, self.operand_2)

    def set_errors(self):
        if len(self.calc_elements) != 4:
            self.errors.append('Incorrect number of elements in calculation')
        if len(self.calc_elements) > 0 and self.calc_elements[0] != 'calc':
            self.errors.append('First element is not "calc"')
        if len(self.calc_elements) > 1 and self.calc_elements[1] not in operations.keys():
            self.errors.append('Second element is not one of ' + valid_operations)
        if len(self.calc_elements) > 2 and not is_integer(self.calc_elements[2]):
            self.errors.append('Third element is not an integer')
        if len(self.calc_elements) > 3 and not is_integer(self.calc_elements[3]):
            self.errors.append('Fourth element is not an integer')

### Main script ###

file_path = input('Enter path of calculations file, or skip to use default: ').strip() \
    or 'calculations.txt'

with open(file_path, 'r') as file_handler:
    file_lines = file_handler.read().splitlines()

running_total = 0

for line in file_lines:
    calculation = Calculation(line)
    try:
        result = calculation.compute()
        running_total += result
        print_aligned(line, result)
    except ValueError as error:
        print_aligned(line, error)

print()
print_aligned('Final total', running_total)
