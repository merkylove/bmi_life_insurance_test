METRES_IN_FEET = 0.3048
METRES_IN_INCH = 0.0254


def calculate_bmi(weight: float, height: float) -> float:
    """
    This function calculates Body Mass Index (BMI)

    :param weight: person's weight (in kilograms), a positive number
    :param height: person's height (in metres), a positive number
    :return: calculated body mass index (BMI): (weight in kg) / (height in metres) ** 2
    """

    if not (weight > 0 and height > 0):
        raise ValueError(
            "Invalid arguments provided: both `weight` and `height` should be positive numbers."
        )

    return weight / height ** 2


def convert_feet_inch_to_metres(feet: int, inch: int) -> float:
    """
    This function converts

    :param feet:
    :param inch:
    :return:
    """

    if not (feet > 0 and inch > 0):
        raise ValueError(
            "Invalid arguments provided: both `feet` and `inch` should be positive numbers."
        )

    return feet * METRES_IN_FEET + inch * METRES_IN_INCH
