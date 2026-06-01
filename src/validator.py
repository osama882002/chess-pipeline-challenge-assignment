from src.logger import logger


def validate_no_duplicates(df):

    duplicates = df.duplicated().sum()

    assert duplicates == 0, (f"Dataset contains {duplicates} duplicate rows.")

    logger.info("Validation passed: no duplicates found.")

    return df


def validate_rating_diff(df):

    assert (df["rating_diff"].notna().all()), (
        "Validation failed: rating_diff contains null values.")

    logger.info("Validation passed: rating_diff has no nulls.")

    return df


def validate_required_columns(df):

    required_columns = [
        "time_base",
        "time_inc",
        "rating_diff",
        "opening_family",
        "is_suspicious"
    ]

    missing_columns = [
        col
        for col in required_columns
        if col not in df.columns
    ]

    assert len(missing_columns) == 0, (f"Missing columns: {missing_columns}")

    logger.info("Validation passed: required columns exist.")

    return df


def run_all_validations(df):

    logger.info(
        "=" * 50
    )

    logger.info("STARTING VALIDATION")

    (
        df
        .pipe(validate_no_duplicates)
        .pipe(validate_rating_diff)
        .pipe(validate_required_columns)
    )

    logger.info("ALL VALIDATIONS PASSED")

    return df