import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelBinarizer, MinMaxScaler
from sklearn.neighbors import NearestNeighbors

path = 'data/nmfulldata.csv'
df = pd.read_csv(path)

def import_and_clean(path):
    nan = np.nan
    df = pd.read_csv(path)
    route_names = list(df.name.unique())
    route_names.remove(nan)
    return route_names

route_names = import_and_clean(path)

xf = df.groupby(['name']).mean()

unique_route_frame = pd.DataFrame(data = route_names, columns = ['route'])

def grade_to_frame(frame):
    grade_list = []
    for i in frame['route']:
        grade_list.append(xf['grade_id'].loc[i])
    grade = list(map(int, grade_list))
    frame['grade'] = grade

grade_to_frame(unique_route_frame)

def rating_to_frame(frame):
    avg_rating = []
    for i in frame['route']:
        avg_rating.append(xf['rating'].loc[i])
    frame['avg_rating'] = avg_rating

rating_to_frame(unique_route_frame)

def binned_scaled(frame):
    scal_bin = frame.copy()
    lb = LabelBinarizer()
    scal_bin = scal_bin.join(pd.DataFrame(lb.fit_transform(scal_bin["grade"]), columns=lb.classes_, index=scal_bin.index))
    scal_bin = scal_bin.drop(['grade','route'], axis=1)
    min_max = MinMaxScaler()
    scal_bin = min_max.fit_transform(scal_bin)
    scal_bin = np.round(scal_bin, 2)
    return scal_bin

scal_bin = binned_scaled(unique_route_frame)

nbrs = NearestNeighbors(n_neighbors=6, algorithm='ball_tree', n_jobs=-1)
nbrs.fit(scal_bin)

distances, indices = nbrs.kneighbors(scal_bin)
