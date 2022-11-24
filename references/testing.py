import pandas as pd

def add_one(x: int) -> int:
	return int(x + 1)

def read_file(fp: str) -> pd.DataFrame:
	return pd.read_csv(fp)
