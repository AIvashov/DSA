from sorting_algorithms import (
    bubble_sort,
    counting_sort,
    insertion_sort,
    selection_sort
)


def run_sort_algorithms(algorithm_sort):
    print(f'\nStart {algorithm_sort.__name__}')
    case_1 = [4, 2, 5, 1, 3]
    answer_1 = [1, 2, 3, 4, 5]
    case_2 = list(range(10, 20)) + list(range(10))
    answer_2 = list(range(20))
    case_3 = [3, 4, 5, 6, 4, 7]
    answer_3 = [3, 4, 4, 5, 6, 7]
    algorithm_sort(case_1)
    algorithm_sort(case_2)
    algorithm_sort(case_3)
    assert case_1 == answer_1
    assert case_2 == answer_2
    assert case_3 == answer_3
    print(f'Passed {algorithm_sort.__name__}')


def test_quadratic_sorting():
    run_sort_algorithms(insertion_sort)
    run_sort_algorithms(selection_sort)
    run_sort_algorithms(bubble_sort)

