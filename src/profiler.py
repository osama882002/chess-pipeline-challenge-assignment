from src.logger import logger
def profile_chess_data(df):

    print("\n" + "=" * 50)
    print("STAGE 1 - PROFILING")
    print("=" * 50)

    q1 = len(df)

    q2 = df.duplicated().sum()

    q3 = df.duplicated(subset=["moves"]).sum()

    q4 = (df["opening_response"].isna().mean()* 100)

    q5 = (df["opening_variation"].isna().mean()* 100)

    min_turns = df["turns"].min()

    suspicious_games = (df["turns"] == min_turns).sum()

    print(f"Q1: Number of records: {q1}")

    print(f"Q2: Exact duplicate rows: {q2}")

    print(f"Q3: Games with duplicate move sequences: {q3}")

    print(f"Q4: Missing opening_response: {q4:.2f}%")

    print(f"Q5: Missing opening_variation:{q5:.2f}%")

    print(f"Q6: Minimum turns = {min_turns}")

    print(f"Suspicious games = {suspicious_games}")

    logger.info("Profiling complete")

