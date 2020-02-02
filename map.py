import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

#data_folder = Path("Documents/corona")
df = pd.read_scv('Documents/corona/coordinates.csv')
pd.head()

BBox = ((df.longitude.min(),df.longitude.max(), df.latitude.min(), df.latitude.max())

