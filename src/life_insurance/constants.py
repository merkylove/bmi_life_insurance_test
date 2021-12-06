from enum import Enum


class Gender(str, Enum):
    """
    This Enum represents user genders supported in the system.
    """

    MALE: str = "MALE"
    FEMALE: str = "FEMALE"
