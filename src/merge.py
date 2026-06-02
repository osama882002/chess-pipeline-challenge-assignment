import pandas as pd

from src.logger import logger


def merge_player_registry(
    chess_df: pd.DataFrame,
    registry_df: pd.DataFrame
) -> pd.DataFrame:

    logger.info("Merging chess games with player registry")

    merged_df = pd.merge(
        # chess_df[['game_id','white_id','white_rating','winner']],
        chess_df,
        registry_df.rename(
            columns={
                "username": "white_id"
            }
        ),
        on="white_id",
        how="left",
    )

    logger.info(f"Merged shape: {merged_df.shape}")

    return merged_df

def standardize_country_names(df):

    logger.info(
        "Standardizing country names"
    )

    country_map = {
        "US": "United States",
        "USA": "United States",
        "united states": "United States",

        "GB": "United Kingdom",
        "UK": "United Kingdom",

        "RUS": "Russia",

        "UA": "Ukraine"
    }

    # df["country"] = (
    #     df["country"]
    #     .replace(country_map)
    # )

    df['country'] = df['country'].map(country_map).fillna(df['country'])
    
    return df