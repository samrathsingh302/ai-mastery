"""Reference solution — rung 2."""


def exercise_volume(df):
    return df.groupby("exercise")["volume"].sum().sort_values(ascending=False)


def weekly_volume(df):
    iso = df["date"].dt.isocalendar()
    weeks = iso["year"].astype(str) + "-W" + iso["week"].astype(str).str.zfill(2)
    return df.groupby(weeks)["volume"].sum().sort_index()


def best_set(df, exercise):
    sets = df[df["exercise"] == exercise]
    top = sets.sort_values(["weight_kg", "reps"], ascending=False).iloc[0]
    return (float(top["weight_kg"]), int(top["reps"]))


def est_1rm(df, exercise):
    sets = df[df["exercise"] == exercise]
    epley = sets["weight_kg"] * (1 + sets["reps"] / 30)
    return round(float(epley.max()), 1)
