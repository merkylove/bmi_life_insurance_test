from src.life_insurance.constants import Gender
from src.life_insurance.entities import Person, Quote
from src.life_insurance.quotes.base_quote_calculator import BaseQuoteCalculator
from src.life_insurance.utils.quote import calculate_quota

__all__ = ("BMIAgeGenderQuoteCalculator",)


class BMIAgeGenderQuoteCalculator(BaseQuoteCalculator):
    """
    This class is responsible for calculating a quote
    for a given user based on the following user attributes:
    - BMI
    - age
    - gender
    """

    def __init__(self, discount: float = 0.1):
        super().__init__()
        self.discount = discount

    def apply_discount(self, person: Person, base_quote: float) -> float:
        """
        This method applies discount based on user's eligibility.
        If a user is not eligible for a discount - base quote is returned.

        :param person: a person entity instance
        :param base_quote: base quote before applying a discount
        :return: discounted quote if eligible, base quote otherwise
        """

        if person.gender == Gender.FEMALE:
            return base_quote * (1.0 - self.discount)
        else:
            return base_quote

    def __call__(self, person: Person) -> Quote:

        base_price, reason = calculate_quota(person.bmi, person.age)
        discounted_price = self.apply_discount(person, base_price)

        return Quote(discounted_price, reason)
