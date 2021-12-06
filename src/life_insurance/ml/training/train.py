import pathlib

import pandas as pd

from src.life_insurance.ml.autoboosting.auto_estimator import LightGBMWrapper
from src.life_insurance.ml.feature_engineering.utils import BMIQuotaFeatureEngineering


def train_model(path: pathlib.Path, filename: str, output_path: pathlib.Path,) -> None:

    path_to_train = path / filename

    df = pd.read_csv(path_to_train, index_col=None)

    feature_builder = BMIQuotaFeatureEngineering(
        bmi_column_name="BMI", quote_column_name="QUOTE"
    )

    # populate dataframe with bmi and quote
    feature_builder(df)

    # TODO: replace hardcoded feature names
    feature_columns = ["Ins_Age", "Ins_Gender", "height", "Wt", "BMI"]
    target_column = "QUOTE"

    model = LightGBMWrapper()
    model.fit(df[feature_columns], df[target_column])

    output_path = output_path / "classifier"
    assert (
        output_path is not None
    )  # assert to avoid unused variable exception from mypy

    # TODO: save model to output path


if __name__ == "__main__":

    # TODO: pass args from Command Line instead of hardcoding

    train_model(
        pathlib.Path("/your/data/path"),
        "your file name.csv",
        pathlib.Path("/your/output/model/path"),
    )
