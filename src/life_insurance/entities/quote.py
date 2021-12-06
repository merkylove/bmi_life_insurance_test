from pydantic.dataclasses import dataclass


@dataclass
class Quote:
    """
    This data class represents a quote entity in the system.
    It has a numeric price for the quote and a reason why this price was assigned.
    """

    quote: float
    reason: str
    currency: str = "USD"
