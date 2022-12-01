"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt
import pytest


def test_daily_mean_zeros():
    """Test that mean function works for an array of zeros."""
    from inflammation.models import daily_mean

    test_input = np.array([[0, 0],
                           [0, 0],
                           [0, 0]])
    test_result = np.array([0, 0])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)


def test_daily_mean_integers():
    """Test that mean function works for an array of positive integers."""
    from inflammation.models import daily_mean

    test_input = np.array([[1, 2],
                           [3, 4],
                           [5, 6]])
    test_result = np.array([3, 4])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)

@pytest.mark.parametrize(
    "test, expected",
    [
        ([[0,0], [0,0], [0,0]], [0,0]),
        ([[1,2], [3,4], [5,6]], [3,4]),
    ]
)
def test_daily_mean(test, expected):
    from inflammation.models import daily_mean
    npt.assert_array_equal(daily_mean(np.array(test)), np.array(expected))

def test_daily_max_integers():
    """Test that the max function works for an array of positive integers"""
    from inflammation.models import daily_max

    test_input = np.array([[4,5],
                        [4,6]])
    test_result = np.array([4, 6])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_max(test_input), test_result)

def test_daily_max_single_row():
    """Test that the max function works for an array of positive integers"""
    from inflammation.models import daily_max

    test_input = np.array([[4,5]])
    test_result = np.array([4, 5])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_max(test_input), test_result)
    
def test_daily_min_string():
    """Test for TypeError when passing strings"""
    from inflammation.models import daily_min

    with pytest.raises(TypeError):
        error.expected = daily_min([['Hi','there'], ['General', 'Kenobi']])

@pytest.mark.parametrize(
    'test, expected',
    [
        ([[1,3],[2,4],[5,6]],[5,6]),
        ([[0,0],[0,0],[0,0]],[0,0]),
        ([[-5,0],[0,5],[10,-6]],[10,5]),
    ]
)
def test_daily_max(test, expected):
    from inflammation.models import daily_max
    npt.assert_array_equal(daily_max(np.array(test)), np.array(expected))

@pytest.mark.parametrize(
    "test, expected",
    [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[0.33, 0.67, 1], [0.67, 0.83, 1], [0.78, 0.89, 1]])
    ]
)
def test_patient_normalise(test, expected):
    """Test normalisation work for arrays of one and positive integers.
    Assumption that test accuracy of two decimal places is sufficient."""
    from inflammation.models import patient_normalise
    npt.assert_almost_equal(patient_normalise(np.array(test)), np.array(expected), decimal=2)