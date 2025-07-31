import pytest
import time
from demo19_decorators import execution_time_decorator

def test_execution_time_decorator_prints_execution_time(capsys):

    @execution_time_decorator
    def dummy():
        time.sleep(0.1)
        return "done"

    result = dummy()
    captured = capsys.readouterr()
    assert "Execution time for dummy:" in captured.out
    assert "done" == result

def test_execution_time_decorator_preserves_return_value():

    @execution_time_decorator
    def add(a, b):
        return a + b

    assert add(2, 3) == 5

def test_execution_time_decorator_with_args_kwargs(capsys):

    @execution_time_decorator
    def concat(a, b, sep=" "):
        return f"{a}{sep}{b}"

    result = concat("hello", "world", sep="-")
    captured = capsys.readouterr()
    assert "Execution time for concat:" in captured.out
    assert result == "hello-world"
    
    
# Test for the generic decorator

def test_generic_decorator(capsys):

    @execution_time_decorator
    def sample_function(x, y):
        time.sleep(0.1)
        return x + y

    result = sample_function(5, 10)
    captured = capsys.readouterr()
    assert "Execution time for sample_function:" in captured.out
    assert result == 15

# Write a simple function to calculate area of rectangle
def area_of_rectangle(length, width):
    return length * width