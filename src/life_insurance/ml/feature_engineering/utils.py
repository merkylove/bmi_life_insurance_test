import pandas as pd

from src.life_insurance.utils.bmi import calculate_bmi, convert_feet_inch_to_metres
from src.life_insurance.utils.quote import calculate_quota


class BMIQuotaFeatureEngineering:

    """
    TODO: add docstrings
    """

    def __init__(self, bmi_column_name: str, quote_column_name: str):
        self.bmi_column_name = bmi_column_name
        self.quote_column_name = quote_column_name

    def __call__(self, df: pd.DataFrame) -> None:

        # convert height to metres
        df["height"] = df.Ht.apply(
            # the first digit refers to feet
            # the latter digits refer to inches
            lambda x: convert_feet_inch_to_metres(feet=int(x[0]), inch=int(x[1:]))
        )

        # calculate bmi
        df[self.bmi_column_name] = df.apply(
            lambda row: calculate_bmi(row.Wt, row.height), axis=1
        )

        # calculate quote
        df[self.quote_column_name] = df.apply(
            lambda row: calculate_quota(row[self.bmi_column_name], row.Ins_Age), axis=1
        )
