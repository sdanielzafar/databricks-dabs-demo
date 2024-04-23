import pandas as pd
from pandas.testing import assert_frame_equal
from cicd_demo.StreamingAggNotebook import pandasAggregateByMs

def func(x):
    return x + 1


def test_answer():
    assert func(3) == 4


def test_aggregation():
    data = {
        'timestamp': ['2023-04-01 12:00:00.123', '2023-04-01 12:00:00.153', '2023-04-01 12:00:00.189'],
        'value': [10, 20, 30]
    }
    input_df = pd.DataFrame(data)

    # Expected output DataFrame
    expected_data = {
        'first_millisecond_digit': [3, 9],
        'total_value': [30, 30]
    }
    expected_df = pd.DataFrame(expected_data)
    result_df = pandasAggregateByMs(input_df)

    assert_frame_equal(expected_df, result_df)