import pytest

from src.life_insurance.constants import Gender
from src.life_insurance.entities.person import Person


@pytest.mark.parametrize(
    "weight, height, age, gender",
    (
        (66.0, 1.75, 31, Gender.MALE),
        (123.0, 2.11, 48, Gender.FEMALE),
        (0.1, 0.11, 1, Gender.FEMALE),
    ),
)
def test_valid_person_init(weight, height, age, gender):
    assert Person(weight, height, age, gender) is not None


@pytest.mark.xfail(raises=ValueError, strict=True)
@pytest.mark.parametrize(
    "weight, height, age, gender",
    (
        (-66.0, 1.75, 31, Gender.MALE),
        (123.0, -2.11, 48, Gender.FEMALE),
        (123.0, 2.11, -48, Gender.FEMALE),
        (123.0, 2.11, 48, "-----"),
    ),
)
def test_invalid_person_init(weight, height, age, gender):
    assert Person(weight, height, age, gender) is not None
