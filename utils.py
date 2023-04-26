import pandas as pd

COLLEGES: list[str] = (data := pd.read_csv(f"data/filtered-data.csv")).groupby("INSTNM").agg("mean", numeric_only=True).reset_index()[["INSTNM", "COSTT4_A","SAT_AVG"]].copy().dropna(axis="rows").sample(100, random_state=0)["INSTNM"].unique()

def heuristic_function(college_name: str) -> tuple[float,float]:
    features = ["COSTT4_A", "SAT_AVG", "ACTWRMID", "ACTMTMID"]

    data = pd.read_csv(f"data/filtered-data.csv", low_memory=False)
    data = data.groupby("INSTNM").agg("mean", numeric_only=True).reset_index()

    data = data[["INSTNM"] + features].copy()
    data["ACT_AVG"] = data["ACTWRMID"] + data["ACTMTMID"]
    
    data["initial_value"] = data["COSTT4_A"] + data["SAT_AVG"]
    data["desired_value"] = data["initial_value"] * 4 

    return data[data["INSTNM"] == college_name][["initial_value", "desired_value"]].values[0]