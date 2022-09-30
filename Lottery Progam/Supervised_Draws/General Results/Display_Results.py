import pandas as pd
import numpy as np
from datetime import datetime as dt

#Display Results

df = pd.read_csv("November_Results.csv", index_col =['Day'])

print(df)

