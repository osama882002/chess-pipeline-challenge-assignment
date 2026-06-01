from src.logger import logger


def analyze_stage2(df):

    print("\n" + "=" * 55)
    print("STAGE 2 ANALYSIS")
    print("=" * 55)
    logger.info(
        "=" * 50
    )
    logger.info("Starting Stage 2 analysis")

    
    # Q7
    # Higher-rated player win percentage

    non_draw_games = (df[df["winner"] != "Draw"])

    higher_rated_won = (
        (
            (non_draw_games["white_rating"] > non_draw_games["black_rating"])
            &
            (non_draw_games["winner"] == "White")
        )
        |
        (
            (non_draw_games["black_rating"] > non_draw_games["white_rating"])
            &
            (non_draw_games["winner"] == "Black")
        )
    )

    q7 = (higher_rated_won.mean()* 100)

    print(f"Q7: Higher-rated player won {q7:.2f}% of non-draw games")


    # Q8
    # Suspicious games

    q8 = (df["is_suspicious"].sum())

    print(f"Q8: Suspicious games (<5 turns): {q8}")


    # Q9
    # Unique opening families

    q9 = (df["opening_family"].nunique())

    print(f"Q9: Unique opening families: {q9}")

    logger.info(f"Q7={q7:.2f}% | Q8={q8} | Q9={q9}")

    return df