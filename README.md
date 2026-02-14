# Python Test Project

A simple Python test project for OpenClaw demonstration.

## Features

- Basic calculator functions (add, subtract, multiply, divide, power, modulo)
- Expression calculator
- Unit tests included

## Calculator Functions

```python
from calculator import add, subtract, multiply, divide, power, modulo, calculate

# Basic operations
add(1, 2)           # 3
subtract(5, 3)      # 2
multiply(3, 4)      # 12
divide(10, 2)       # 5
power(2, 3)          # 8
modulo(10, 3)        # 1

# Expression calculator
calculate("1 + 2")   # 3
calculate("10 / 2 - 3")  # 2
```

## Running Tests

```bash
python3 test_calculator.py
```

## Files

```
python-test/
├── calculator.py       # Calculator module
├── test_calculator.py  # Unit tests
├── main.py            # Main program
├── README.md          # This file
├── requirements.txt   # Dependencies
└── .gitignore        # Git ignore rules
```

## Author

- GitHub: [@rlysyy](https://github.com/rlysyy)
