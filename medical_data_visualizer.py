import pandas as pd

df= pd.read_csv('medical_data.csv')

df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2) > 25).astype(int)

df['smoke'] = df['smoke'].map({1: 'good', 0: 'bad'})

df['alco'] = df['alco'].map({1: 'good', 0: 'bad'})

df['active'] = df['active'].map({1: 'good', 0: 'bad'})

df['cardio'] = df['cardio'].map({1: 'good', 0: 'bad'})

