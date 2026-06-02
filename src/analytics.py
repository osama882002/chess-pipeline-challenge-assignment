from src.logger import logger


def classify_game_length(turns):

    if turns < 20:
        return "Short"

    elif turns < 60:
        return "Medium"

    return "Long"


def analyze_stage3(df):

    print("\n" + "=" * 55)
    print("STAGE 3 ANALYSIS")
    print("=" * 55)

    logger.info(
        "=" * 50
    )
    logger.info("Starting Stage 3 analysis")

    # ==================================================
    # Q10
    # Win rate
    # ==================================================

    win_rates = (
        df["winner"]
        .value_counts(normalize=True)
        * 100
    )

    print("\n" + "-" * 55)
    print("\nQ10 - Win Rate")

    for result, rate in win_rates.items():
        print(f"     -> {result:<6}: {rate:.2f}%")

    # ==================================================
    # Q11
    # Most common victory status
    # ==================================================

    victory_counts = (
        df["victory_status"]
        .value_counts(normalize=True)
        * 100
    )

    print("\n" + "-" * 55)
    print("\nQ11 - Most Common Victory Status")

    # print(victory_counts.head())
    for status, pct in victory_counts.items():
        print(f"     -> {status:<12}: {pct:.2f}%")

    # ==================================================
    # Q12
    # Highest average turns
    # ==================================================

    avg_turns = (
        df.groupby("victory_status")["turns"]
        .mean()
        .sort_values(ascending=False)
    )

    print("\n" + "-" * 55)
    print("\nQ12 - Average Turns by Victory Status")

    # print(avg_turns)
    for status, turns in avg_turns.items():
        print(f"     -> {status:<12}: {turns:.2f} turns")

    # ==================================================
    # Q13
    # Most popular opening family
    # ==================================================

    white_openings = (
        df[df["winner"] == "White"]
        ["opening_family"]
        .value_counts()
    )

    black_openings = (
        df[df["winner"] == "Black"]
        ["opening_family"]
        .value_counts()
    )

    print("\n" + "-" * 55)
    print("\nQ13 - Most Popular Opening Family")

    print(f"     -> White Wins : {white_openings.index[0]} ({white_openings.iloc[0]} games)")

    print(f"     -> Black Wins : {black_openings.index[0]} ({black_openings.iloc[0]} games)")
    

    # ==================================================
    # Q14
    # Rated vs Unrated
    # ==================================================

    white_win_rate = (
        df.groupby("rated")["winner"]
        .apply(
            lambda x:
            (x == "White").mean() * 100
        )
    )

    print("\n" + "-" * 55)
    print("\nQ14 - White Win Rate")

    # print(white_win_rate)
    print(f"     -> Rated Games: {white_win_rate.get(True, 0):.2f}%")
    print(f"     -> Unrated Games: {white_win_rate.get(False, 0):.2f}%")

    # ==================================================
    # Q15
    # apply()
    # ==================================================
    # print(df["turns"].describe())
    # print(df["turns"].quantile([0.25, 0.50, 0.75]))
    
    df["game_length"] = (
        df["turns"]
        .apply(classify_game_length)
    )

    game_length_dist = (
        df["game_length"]
        .value_counts(normalize=True)
        * 100
    )

    print("\n" + "-" * 55)
    print("\nQ15 - Game Length Distribution")

    # print(game_length_dist)
    for category, pct in game_length_dist.items():
        print(f"     -> {category:<6}: {pct:.2f}%")


    logger.info("Stage 3 analysis completed")
    print("\n" + "-" * 55)

    return df