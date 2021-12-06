from src.life_insurance.entities import Person, Quote


class BaseQuoteCalculator:
    """
    This is a base interface for Quote Calculators.
    """

    def __call__(self, person: Person) -> Quote:
        """
        This is the abstract method which is responsible
        for calculating a quote based on user's data.

        :param person: a person entity instance
        :return: suggested quote
        """
        raise NotImplementedError
