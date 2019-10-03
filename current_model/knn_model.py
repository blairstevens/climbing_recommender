import numpy as np
import pandas as pd

path = 'data/nmfulldata.csv'

def import_and_clean(path):
    nan = np.nan
    df = pd.read_csv(path)
    route_names = list(df.name.unique())
    route_names.remove(nan)
    df.
    return route_names

route_names = import_and_clean(path)
nan in route_names
