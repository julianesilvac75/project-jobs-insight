from functools import lru_cache
import csv


@lru_cache
def read(path):
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """

    with open(path, encoding="utf-8") as file:
        file_data = csv.DictReader(file, delimiter=",", quotechar='"')

        jobs_list = list(file_data)

    return jobs_list
