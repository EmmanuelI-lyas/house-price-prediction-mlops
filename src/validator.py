from src.logger import logger


def validate_dataframe(df, target=None):
    """
    Validate dataset before training.
    """

    logger.info("Running data validation...")

    # Empty dataframe
    if df.empty:
        raise ValueError("Dataset is empty.")

    # Duplicate rows
    duplicates = df.duplicated().sum()

    logger.info(f"Duplicate Rows: {duplicates}")

    # Missing target
    if target is not None:

        if target not in df.columns:
            raise ValueError(f"Target column '{target}' not found.")

        missing_target = df[target].isnull().sum()

        if missing_target > 0:
            raise ValueError(
                f"Target contains {missing_target} missing values."
            )

    # Missing values report
    missing = df.isnull().sum()

    missing = missing[missing > 0]

    if len(missing):

        logger.warning("Columns containing missing values:")

        for column, value in missing.items():
            logger.warning(f"{column}: {value}")

    logger.info("Validation Successful.")

    return True