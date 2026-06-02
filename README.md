# ♟ Chess Pipeline Challenge

A complete Data Cleaning, Validation, Analysis, and Visualization pipeline built with Pandas following the **7-Stage Cleaning Framework**.

---

# Project Overview

This project processes two datasets:

* `chess_games.csv`
* `player_registry.csv`

The goal is to transform raw and untrusted data into a clean and validated analytical dataset while answering a series of business questions.

---

# Project Structure

```text
chess-pipeline-challenge/

├── data/
│   ├── raw/
│   │   ├── chess_games.csv
│   │   └── player_registry.csv
│   │
│   └── processed/
│       └── chess_clean.csv
│
├── logs/
│   └── pipeline.log
│
├── output/
│   └── plots/
│       ├── wins_by_color.png
│       ├── rating_vs_turns.png
│       └── turns_by_victory_status.png
│
├── src/
│   ├── analytics.py
│   ├── clean.py
│   ├── loader.py
│   ├── logger.py
│   ├── merge.py
│   ├── profiler.py
│   ├── validator.py
│   └── visualizer.py
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

# Datasets

## chess_games.csv

Rows: **20,058**

Columns:

* game_id
* rated
* turns
* victory_status
* winner
* time_increment
* white_id
* white_rating
* black_id
* black_rating
* moves
* opening_code
* opening_moves
* opening_fullname
* opening_shortname
* opening_response
* opening_variation

---

## player_registry.csv

Rows: **215**

Contains player metadata:

* username
* display_name
* country
* registered_year
* rating_registry
* total_games_registry
* account_status
* email_verified
* join_platform

---

# The 7-Stage Cleaning Framework

## Stage 1 — Load

### Decision

Load data directly from Google Drive and cache locally.

### Why

Avoid repeated downloads and ensure reproducibility.

---

## Stage 2 — Shape

### Decision

Remove exact duplicate rows.

### Why

Duplicates distort statistics and analytical results.

Result:

```text
0 exact duplicates
```

---

## Stage 3 — Column Names

### Decision

Validate expected schema before processing.

### Why

Protect the pipeline from unexpected file changes.

---

## Stage 4 — Types

### Decision

Parse time controls.

```python
df[['time_base','time_inc']] = (
    df['time_increment']
    .str.split('+', expand=True)
    .astype(int)
)
```

### Why

Numeric values are easier to analyze than strings.

---

## Stage 5 — Null Handling

### Decision

Drop:

```text
opening_response
```

### Why

Missing in 93.98% of rows.

Keeping it provides little analytical value.

---

## Stage 6 — Invalid Values

### Decision

Flag suspicious games.

```python
df['is_suspicious'] = df['turns'] < 5
```

### Why

Games ending after only a few moves often represent resignations, disconnects, or invalid gameplay.

---

## Stage 7 — Validation

### Checks

```python
assert df['rating_diff'].notna().all()
assert df.duplicated().sum() == 0
```

### Purpose

Guarantee data quality before analysis.

---

# Stage 1 — Profiling Results

## Q1

How many records are in the dataset?

```text
20,058
```

---

## Q2

How many exact duplicate rows exist?

```text
0
```

---

## Q3

How many games have duplicate move sequences?

```text
1,138
```

---

## Q4

What percentage of opening_response is missing?

```text
93.98%
```

---

## Q5

What percentage of opening_variation is missing?

```text
28.22%
```

---

## Q6

What is the minimum number of turns?

```text
1 turn
```

Suspicious games:

```text
18 games
```

Reason:

These games ended almost immediately and may represent resignations or disconnects.

---

# Stage 2 — Cleaning Results

## Q7

What percentage of non-draw games were won by the higher-rated player?

```text
64.64%
```

---

## Q8

How many games were flagged as suspicious (< 5 turns)?

```text
342
```

---

## Q9

How many unique opening families exist?

```text
227
```

---

# Stage 3 — Analysis Results

## Q10

Win Rate

```text
White: 49.86%
Black: 45.40%
Draw: 4.74%
```

---

## Q11

Most common victory status

```text
Resign: 55.57%
Mate: 31.53%
Out of Time: 8.38%
Draw: 4.52%
```

Most games end by resignation.

---

## Q12

Average turns by victory status

```text
Draw: 83.78
Out of Time: 72.74
Mate: 65.42
Resign: 53.91
```

Draw games are significantly longer.

---

## Q13

Most popular opening family

White wins:

```text
Sicilian Defense (1173)
```

Black wins:

```text
Sicilian Defense (1273)
```

---

## Q14

White win rate in rated vs unrated games

```text
Rated Games: 49.84%
Unrated Games: 49.94%
```

Very similar results.

---

## Q15

Game Length Classification

Using:

```python
apply(classify_game_length)
```

Results:

```text
Medium: 63%
Long: 32%
Short: 5%
```

Most games are medium length.

---

# Stage 4 — Merge & Conflict Resolution

## Q16

How many white players have no registry entry?

```text
9,238 unique players
```

Most players in the chess dataset are not present in the registry dataset.

---

## Q17

How many clean country names remain after standardization?

```text
10
```

Country names were standardized using a mapping dictionary.

Examples:

```text
US → United States
USA → United States
GB → United Kingdom
UK → United Kingdom
RUS → Russia
UA → Ukraine
```

---

# Visualizations

## Q18

Win Counts by Color

```text
White: 10,001
Black: 9,107
Draw: 950
```

Saved as:

```text
output/plots/wins_by_color.png
```

---

## Q19

White Rating vs Turns

Observation:

* Higher-rated games are not necessarily longer.
* Game length varies across all rating levels.
* No strong linear relationship appears.

Saved as:

```text
output/plots/rating_vs_turns.png
```

---

## Additional Plot

Turns by Victory Status

Saved as:

```text
output/plots/turns_by_victory_status.png
```

---

# Key Findings

* Higher-rated players win approximately 65% of non-draw games.
* Sicilian Defense is the most popular opening family.
* Most games end by resignation.
* Draw games are the longest games on average.
* Registry coverage is limited compared to the chess dataset.
* Country names required standardization before analysis.

---

# Technologies Used

* Python
* Pandas
* Matplotlib
* Logging
* Git
* GitHub

---

# Skills Demonstrated

* Data Profiling
* Data Cleaning
* Data Validation
* Data Transformation
* Data Quality Assessment
* ETL Concepts
* Logging
* Data Visualization
* Git Version Control
* Reproducible Pipelines

---

# Final Output

Generated Files:

```text
data/processed/chess_clean.csv
output/plots/wins_by_color.png
output/plots/rating_vs_turns.png
output/plots/turns_by_victory_status.png
logs/pipeline.log
```

The pipeline successfully transforms raw chess data into a clean, validated, and analysis-ready dataset.
