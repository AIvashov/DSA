from search_algorithms import binary_search


def test_binary_search():
    case_1 = list(range(10, 25))
    case_2 = list(range(-5, 5))
    assert binary_search(case_1, 10) == 0
    assert binary_search(case_1, 24) == 14
    assert binary_search(case_1, 17) == 7
    assert binary_search(case_1, 11) == 1
    assert binary_search(case_1, 22) == 12
    assert binary_search(case_1, 202) is None
    assert binary_search(case_2, -5) == 0
    assert binary_search(case_2, 0) == 5
    assert binary_search(case_2, 4) == 9
    assert binary_search(case_2, -1) == 4
    assert binary_search(case_2, 1) == 6
    assert binary_search(case_2, -11) is None
