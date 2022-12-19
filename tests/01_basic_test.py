from other_code.services import DATA_SET_A, DATA_SET_B, DATA_SET_C
import time

def test_example():
    """
    But really, test cases should be callables containing assertions:
    """
    print("\nRunning test_example...")
    assert DATA_SET_A == DATA_SET_B

def test_failing_test():
    assert 1 == 0

