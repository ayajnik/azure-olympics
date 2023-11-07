import sys

sys.path.append('..')

from operations import io

df_athletes = io.getFile()

print(df_athletes.head())


