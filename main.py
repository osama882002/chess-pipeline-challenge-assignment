from src.loader import fetch_drive_data
from src.profiler import profile_chess_data

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

profile_chess_data(df_chess)
