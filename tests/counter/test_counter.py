from src.counter import count_ocurrences


def test_counter():
    """Testing if the function returns"""
    """the right amount of words when searching for"""
    """Javascript and Python, and if the function is case insensitive"""

    path = "src/jobs.csv"
    python_amount = 1639
    javascript_amount = 122

    assert count_ocurrences(path, "Python") == python_amount
    assert count_ocurrences(path, "python") == python_amount
    assert count_ocurrences(path, "Javascript") == javascript_amount
    assert count_ocurrences(path, "javascript") == javascript_amount
