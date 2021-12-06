from typing import Tuple


def calculate_quota(bmi: float, age: float) -> Tuple[float, str]:

    """
    TODO: add docstring

    :param bmi:
    :param age:
    :return:
    """

    if 18 <= age <= 39 and (bmi < 17.49 or bmi > 38.5):
        return (
            750.0,
            "Age is between 18 to 39 and 'BMI' is either less than 17.49 or greater than 38.5",
        )
    elif 40 <= age <= 59 and (bmi < 18.49 or bmi > 38.5):
        return (
            1000.0,
            "Age is between 40 to 59 and 'BMI' is either less than 18.49 or greater then 38.5",
        )
    elif age >= 60 and (bmi < 18.49 or bmi > 45.5):
        return (
            2000.0,
            "Age is greater than 60 and 'BMI' is either less than 18.49 or greater than 38.5",
        )
    else:
        return 500.0, "BMI is in right range"
