import pandas as pd

from src.logger import logger


def clean_chess(df: pd.DataFrame) -> pd.DataFrame:

    logger.info("=" * 50)
    logger.info("STARTING CLEANING PIPELINE")
    logger.info("=" * 50)

    
    # STAGE 1: LOAD

    logger.info("Stage 1 - Load")

    df_clean = df.copy()

    # STAGE 2: SHAPE

    logger.info("Stage 2 - Shape")

    before_rows = len(df_clean)

    df_clean = df_clean.drop_duplicates()

    removed = before_rows - len(df_clean)

    logger.info(f"Removed {removed} duplicate rows")


    # STAGE 3: COLUMN NAMES

    logger.info("Stage 3 - Column Names")

    df_clean.columns = (
        df_clean.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )


    # STAGE 4: TYPES

    logger.info("Stage 4 - Types")

    df_clean["winner"] = (
        df_clean["winner"]
        .astype("category")
    )

    df_clean["rated"] = (
        df_clean["rated"]
        .astype("bool")
    )

    df_clean["turns"] = (
        df_clean["turns"]
        .astype("int16")
    )

    df_clean["white_rating"] = (
        df_clean["white_rating"]
        .astype("int16")
    )

    df_clean["black_rating"] = (
        df_clean["black_rating"]
        .astype("int16")
    )


    # STAGE 5: NULLS

    logger.info("Stage 5 - Nulls")

    if "opening_response" in df_clean.columns:

        df_clean = df_clean.drop(
            columns=["opening_response"]
        )

        logger.info(
            "Dropped opening_response "
            "(93.98% null)"
        )

    
    # STAGE 6: INVALID VALUES

    logger.info("Stage 6 - Invalid Values")

    # 2a

    df_clean[
        ["time_base", "time_inc"]
    ] = (
        df_clean["time_increment"]
        .str.split(
            "+",
            expand=True
        )
        .astype(int)
    )

    logger.info(
        "Parsed time_increment"
    )

    # 2b

    df_clean["rating_diff"] = (
        df_clean["white_rating"]
        - df_clean["black_rating"]
    )

    logger.info(
        "Created rating_diff"
    )

    # 2c

    df_clean["opening_family"] = (
        df_clean["opening_fullname"]
        .str.split(":")
        .str[0]
        .str.strip()
    )

    logger.info(
        "Created opening_family"
    )

    # 2e

    df_clean["is_suspicious"] = (
        df_clean["turns"] < 5
    )

    suspicious_count = (
        df_clean["is_suspicious"]
        .sum()
    )

    logger.info(
        f"Flagged {suspicious_count} "
        f"suspicious games"
    )


    # EXTRA FEATURES

    logger.info(
        "Creating extra features"
    )

    df_clean["winner_code"] = (
        df_clean["winner"]
        .map({
            "White": 1,
            "Black": -1,
            "Draw": 0
        })
    )

    df_clean["opening_family"] = (
        df_clean["opening_family"]
        .astype("category")
    )

    df_clean["first_move"] = (
        df_clean["moves"]
        .str.split()
        .str[0]
    )

    df_clean["rating_tier"] = pd.cut(
        df_clean["white_rating"],
        bins=[
            0,
            1200,
            1500,
            1800,
            2100,
            3000
        ],
        labels=[
            "Beginner",
            "Club",
            "Intermediate",
            "Advanced",
            "Expert"
        ]
    )

    logger.info("Cleaning pipeline completed")
    
    return df_clean