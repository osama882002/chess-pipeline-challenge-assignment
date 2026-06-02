import os

import matplotlib.pyplot as plt

from src.logger import logger


PLOTS_DIR = os.path.join("output", "plots")

os.makedirs(
    PLOTS_DIR,
    exist_ok=True
)


def plot_winner_counts(df):

    logger.info("Creating winner counts chart")

    plt.figure(figsize=(8, 5))

    df["winner"].value_counts().plot(
            kind="bar",
            title="Wins by Color",
            color=['#C9A84C', '#1B3A2D', '#7A8C7E'],
            rot=0
        )
    

    plt.xlabel("Winner")
    plt.ylabel("Games")

    plt.tight_layout()

    plt.savefig(
        os.path.join(
            PLOTS_DIR,
            "wins_by_color.png"
        )
    )

    plt.close()


def plot_rating_vs_turns(df):

    logger.info("Creating rating vs turns scatter plot")

    rated_games = (df[df["rated"] == True])

    plt.figure(figsize=(8, 5))

    plt.scatter(
        rated_games["white_rating"],
        rated_games["turns"],
        alpha=0.3,
        edgecolors='black',
        color="#03FB94"
    )

    plt.title("White Rating vs Turns")

    plt.xlabel("White Rating")

    plt.ylabel("Turns")

    plt.tight_layout()

    plt.savefig(
        os.path.join(
            PLOTS_DIR,
            "rating_vs_turns.png"
        )
    )

    plt.close()


def plot_turns_by_victory_status(df):

    logger.info("Creating box plot")

    plt.figure(figsize=(10, 6))

    df.boxplot(
        column="turns",
        by="victory_status"
    )

    plt.title("Turns by Victory Status")

    plt.suptitle("")

    plt.tight_layout()

    plt.savefig(
        os.path.join(
            PLOTS_DIR,
            "turns_by_victory_status.png"
        )
    )

    plt.close()