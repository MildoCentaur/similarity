from typing import List, Dict


def check_expected_paramaters(expected: List, parameters: Dict) -> bool:
    if parameters is None:
        return False

    for element in expected:
        if element not in parameters.keys():
            return False
    return True
