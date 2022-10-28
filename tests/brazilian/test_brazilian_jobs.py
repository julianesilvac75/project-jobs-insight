from src.brazilian_jobs import read_brazilian_file
from tests.mocks.translated_jobs import translated_job


def test_brazilian_jobs():
    """Testing if the function returns a dictionary list"""
    """with the translated keys. """
    path = "tests/mocks/brazilians_jobs.csv"

    assert read_brazilian_file(path) == translated_job
