from src.loader import fetch_drive_data
from src.profiler import profile_chess_data
from src.clean import clean_chess
from src.validator import run_all_validations
from src.analytics import (
    analyze_stage3, 
    analyze_stage2, 
    analyze_stage4, 
    analyze_visualizations
    )
from src.merge import (
    merge_player_registry, 
    standardize_country_names
    )
from src.visualizer import (
    plot_winner_counts,
    plot_rating_vs_turns,
    plot_turns_by_victory_status
)


URL_CHESS_GAMES = (
"https://drive.google.com/file/d/1eR3NZtwIC6ECN3vhtrynqmx8okG0twA7/view?usp=sharing"
)

URL_PLAYER_REGISTRY = (
"https://drive.google.com/file/d/1wCSAkGagMzWiToedLC3ZGo_lGf_laF-k/view?usp=sharing"
)

df_chess = fetch_drive_data(
URL_CHESS_GAMES,
"chess_games.csv"
)

df_players = fetch_drive_data(
URL_PLAYER_REGISTRY,
"player_registry.csv"
)



def main():

    print("\n=== CHESS PIPELINE STARTED ===\n")

    # Load Data
    df_chess = fetch_drive_data(
        URL_CHESS_GAMES,
        "chess_games.csv"
    )

    df_players = fetch_drive_data(
        URL_PLAYER_REGISTRY,
        "player_registry.csv"
    )

    # Stage 1
    profile_chess_data(df_chess)

    # Stage 2
    df_chess_clean = (
        df_chess
        .pipe(clean_chess)
        .pipe(run_all_validations)
        .pipe(analyze_stage2)
        # Stage 3
        .pipe(analyze_stage3)
    )
    # Stage 4
    merged_df = (
        merge_player_registry(
            df_chess_clean,
            df_players
        )
        .pipe(standardize_country_names)
        .pipe(analyze_stage4)
        
    )

    # Visualization

    plot_winner_counts(df_chess_clean)

    plot_rating_vs_turns(df_chess_clean)

    plot_turns_by_victory_status(df_chess_clean)

    analyze_visualizations(df_chess_clean)

    print("\n[+] Plots saved to output/plots/")


    print(f"\n[+] Clean dataset shape: {df_chess_clean.shape}")

    # Save Output
    df_chess_clean.to_csv(
        "data/processed/chess_clean.csv",
        index=False
    )

    print(
        "\n[+] Cleaned dataset saved to:"
        "\ndata/processed/chess_clean.csv"
    )

    print("\n=== PIPELINE FINISHED ===")


if __name__ == "__main__":
    main()
