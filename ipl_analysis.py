import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load Dataset
df = pd.read_csv("IPL.csv")

print("Dataset Loaded Successfully ✅")
print("Shape of Dataset:", df.shape)

print("\nFirst 5 Rows:")
print(df.head())

print("\nColumn Names:")
print(df.columns)

print("\nChecking Missing Values:")
print(df.isnull().sum())

df = df.drop(columns=["Unnamed: 0"])

print("Shape after cleaning:", df.shape)

# Top 10 Run Scorers
top_batsmen = df.groupby("batter")["runs_total"].sum().sort_values(ascending=False).head(10)

print("\nTop 10 Run Scorers:")
print(top_batsmen)


# Plot Top 10 Run Scorers
plt.figure(figsize=(10,6))
top_batsmen.plot(kind="bar")

plt.title("Top 10 Run Scorers in IPL History")
plt.xlabel("Player")
plt.ylabel("Total Runs")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


# Most Sixes in IPL History


# Filter only sixes
sixes = df[df["runs_batter"] == 6]

# Count sixes by each batter
top_six_hitters = sixes["batter"].value_counts().head(10)

print("\nTop 10 Six Hitters:")
print(top_six_hitters)

# Plot Graph
plt.figure(figsize=(10,6))
top_six_hitters.plot(kind="bar")

plt.title("Top 10 Six Hitters in IPL History")
plt.xlabel("Player")
plt.ylabel("Number of Sixes")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


# Most Wickets in IPL History


# Remove null wickets
wickets_df = df[df["wicket_kind"].notnull()]

# Remove run outs (not credited to bowler)
wickets_df = wickets_df[wickets_df["wicket_kind"] != "run out"]

# Count wickets by bowler
top_wicket_takers = wickets_df["bowler"].value_counts().head(10)

print("\nTop 10 Wicket Takers:")
print(top_wicket_takers)

# Plot Graph
plt.figure(figsize=(10,6))
top_wicket_takers.plot(kind="bar")

plt.title("Top 10 Wicket Takers in IPL History")
plt.xlabel("Bowler")
plt.ylabel("Number of Wickets")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


# Best IPL Team (Most Match Wins)


# Get unique matches (one row per match)
matches = df.drop_duplicates(subset=["match_id"])

# Count wins by each team
team_wins = matches["match_won_by"].value_counts().head(10)

print("\nTop 10 Most Successful IPL Teams:")
print(team_wins)

# Plot Graph
plt.figure(figsize=(10,6))
team_wins.plot(kind="bar")

plt.title("Top 10 Most Successful IPL Teams")
plt.xlabel("Team")
plt.ylabel("Number of Wins")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()