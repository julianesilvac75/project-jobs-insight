import pytest
from tests.mocks.jobs_by_criteria import (
    jobs_by_date_posted,
    jobs_by_max_salary,
    jobs_by_min_salary,
)
from src.sorting import sort_by


@pytest.fixture
def jobs():
    return [
        {"min_salary": "0", "max_salary": "10", "date_posted": "2020-05-08"},
        {"min_salary": "", "max_salary": "", "date_posted": "2020-05-07"},
        {"min_salary": "50", "max_salary": "500", "date_posted": "2020-05-06"},
        {"min_salary": "10", "max_salary": "100", "date_posted": "2020-05-09"},
    ]


def test_sort_by_criteria(jobs):
    """Testing if the function returns a list with jobs"""
    """sorted by the right criteria. """

    sort_by(jobs, "min_salary")
    assert jobs == jobs_by_min_salary

    sort_by(jobs, "max_salary")
    assert jobs == jobs_by_max_salary

    sort_by(jobs, "date_posted")
    assert jobs == jobs_by_date_posted
