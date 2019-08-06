import numpy as np
import pandas as pd

bb_csv_path = "../baseballdatabank-2019.2/core"

pitching = pd.read_csv(f"{bb_csv_path}/Pitching.csv", index_col=["playerID","yearID","stint"], usecols=["playerID","yearID","stint", "pIPouts", "pG"])
batting = pd.read_csv(f"{bb_csv_path}/Batting.csv", index_col=["playerID","yearID","stint"])

bp = pd.merge(batting, pitching, on=["playerID","yearID","stint"], how="outer")

pitcher_batting_stats = bp.query('(pIPouts > 9)').groupby("yearID").sum()
print(pitcher_batting_stats)

batter_batting_stats = bp.query('(pG != pG) & (bAB > 0)').groupby("yearID").sum()
print(batter_batting_stats)
