import pytest 

# from calculator import Calculator 



# def test_add(): 
#  calc = Calculator() 
#  assert calc.add(3, 5) == 8 
#  assert calc.add(-1, 1) == 0 
#  assert calc.add(-1, -1) == -2 
# def test_subtract(): 
#  calc = Calculator() 
#  assert calc.subtract(5, 3) == 2 
#  assert calc.subtract(1, 5) == -4 
#  assert calc.subtract(-5, -3) == -2 
# def test_multiply():
#   calc = Calculator()
#   assert calc.multiply(3, 5) == 15
#   assert calc.multiply(2.0, 3.0) == pytest.approx(6.0)  # because of floating point
# def test_divide():
#     calc = Calculator()
#     assert calc.divide(10, 2) == 5
#     assert calc.divide(5, 2) == 2.5
#     with pytest.raises(ValueError):
#         calc.divide(5, 0)  # This will currently fail because it returns a string





# @pytest.mark.parametrize("a, b, expected", [ 
#  (3, 5, 8), 
#  (-1, 1, 0), 
#  (-1, -1, -2), 
#  (0, 0, 0) 
# ]) 
# def test_add_parameterized(a, b, expected): 
#  calc = Calculator() 
#  assert calc.add(a, b) == expected 

# @pytest.mark.parametrize("a, b, expected", [
#     (5, 3, 2),
#     (1, 5, -4),
#     (-5, -3, -2),
#     (0, 0, 0)
# ])
# def test_subtract_parameterized( a, b, expected):
#     calc = Calculator() 
#     assert calc.subtract(a, b) == expected

# @pytest.mark.parametrize("a, b, expected", [
#     (3, 5, 15),
#     (2, 0, 0),
#     (2.0, 3.0, 6.0),
#     (-2, 4, -8)
# ])
# def test_multiply_parameterized( a, b, expected):
#     calc = Calculator() 
#     assert calc.multiply(a, b) == expected


# @pytest.mark.parametrize("a, b, expected", [
#     (10, 2, 5),
#     (5, 2, 2.5),
#     (7.5, 2.5, 3.0),
# ])
# def test_divide_parameterized(a, b, expected):
#     calc = Calculator()
#     assert calc.divide(a, b) == pytest.approx(expected)

# def test_divide_by_zero():
#     calc = Calculator()
#     with pytest.raises(ValueError):
#         calc.divide(5, 0)

# @pytest.mark.parametrize("a, b, expected", [
#     (2, 3, 8),
#     (3, 2, 9),
#     (2, 0, 1),
#     (2, -2, 0.25),
#     (10, -1, 0.1)
# ])
# def test_power_parameterized(a, b, expected):
#     calc = Calculator()
#     assert calc.power(a, b) == pytest.approx(expected)





from calculator import Calculator
@pytest.fixture
def calculator():
 return Calculator()

@pytest.mark.parametrize("a, b, expected", [
(3, 5, 8),
(-1, 1, 0),
(-1, -1, -2),
(0, 0, 0)
])
def test_add_parameterized(calculator, a, b, expected):
 assert calculator.add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 2),
    (1, 5, -4),
    (-5, -3, -2),
    (0, 0, 0)
])
def test_subtract_parameterized(calculator, a, b, expected):
    assert calculator.subtract(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (3, 5, 15),
    (2, 0, 0),
    (2.0, 3.0, 6.0),
    (-2, 4, -8)
])
def test_multiply_parameterized(calculator, a, b, expected):
    assert calculator.multiply(a, b) == pytest.approx(expected)

@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5),
    (5, 2, 2.5),
    (7.5, 2.5, 3.0),
])
def test_divide_parameterized(calculator, a, b, expected):
    assert calculator.divide(a, b) == pytest.approx(expected)

def test_divide_by_zero(calculator):
    with pytest.raises(ValueError):
        calculator.divide(5, 0)

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 8),
    (3, 2, 9),
    (2, 0, 1),
    (2, -2, 0.25),
    (10, -1, 0.1)
])
def test_power_parameterized(calculator, a, b, expected):
    assert calculator.power(a, b) == pytest.approx(expected)

@pytest.mark.parametrize("n, expected", [
    (0, 1),
    (1, 1),
    (5, 120),
    (7, 5040)
])
def test_factorial(calculator, n, expected):
    assert calculator.factorial(n) == expected

def test_factorial_negative(calculator):
    with pytest.raises(ValueError):
        calculator.factorial(-5)

@pytest.mark.parametrize("n, expected", [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (7, 13)
])
def test_fibonacci(calculator, n, expected):
    assert calculator.fibonacci(n) == expected

def test_fibonacci_negative(calculator):
    with pytest.raises(ValueError):
        calculator.fibonacci(-3)


def test_precise_addition(precise_calculator):
    assert precise_calculator.add(0.3333, 0.3333) == 0.67

@pytest.mark.parametrize("a, b, expected", [
    (5.555, 2.222, 3.33),
    (10.1234, 5.1111, 5.01),
    (0.9999, 0.4444, 0.56),
    (2, 1, 1),  # integer case should work too
])
def test_precise_subtract(precise_calculator, a, b, expected):
    assert precise_calculator.subtract(a, b) == expected

def test_precise_operations(precise_calculator):
    assert precise_calculator.add(0.3333, 0.3333) == 0.67
    assert precise_calculator.subtract(5.555, 2.222) == 3.33
    assert precise_calculator.multiply(1.234, 2.345) == 2.89
    assert precise_calculator.divide(10, 3) == 3.33
