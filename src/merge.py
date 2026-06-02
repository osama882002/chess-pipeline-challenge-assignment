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

    if "country" in df.columns:
        df['country'] = df['country'].str.strip().str.title() # تنظيف العمود من الفراغات وتوحيد حالة الأحرف
        df['country'] = df['country'].replace('', None)  # التخلص من أي نصوص فارغة إن وجدت

    country_map = {
            # أمريكا وبريطانيا
            "Us": "United States",
            "Usa": "United States",
            "Uk": "United Kingdom",
            "Gb": "United Kingdom",
            
            # روسيا وأوكرانيا            
            "Rus": "Russia",
            "Russian Federation": "Russia",
            "Ua": "Ukraine",
            
            # ألمانيا
            "De": "Germany",
            "Deutschland": "Germany",
            
            # فرنسا وإسبانيا
            "Fr": "France",
            "Es": "Spain",
            
            # بولندا والبرازيل والهند
            "Pl": "Poland",
            "Bra": "Brazil",
            "In": "India"
        }

    df["country"] = (df["country"].replace(country_map)) # استبدال الصيغ المتعارضة بالأسماء الموحدة
    
    return df