from pydantic import validator
from pydantic.dataclasses import dataclass

from src.life_insurance.constants import Gender
from src.life_insurance.utils.bmi import calculate_bmi


@dataclass
class Person:
    """
    This data class represents a user entity in the system.
    """

    weight: float
    height: float
    age: int
    gender: Gender

    @validator("weight", "height", "age")
    def check_positive(cls, value):  # noqa: B902
        if value > 0:
            return value
        else:
            raise ValueError(f"{value} is not a positive number!")

    @property
    def bmi(self):
        return calculate_bmi(self.weight, self.height)
