import pandas as pd
import numpy as np


def combineData(df_list):
    
    combined = pd.DataFrame()

    for df in df_list:
        combined = combined.append(df)

    combined = combined.fillna(method='ffill').drop_duplicates()

    return combined


def modifyWeapons(df):

    modified = pd.DataFrame()
    
    modified["Name"] = df["Name"]

    modified['perksList'] = df["Perks 0"].str.cat(df[["Perks 2", "Perks 3", "Perks 4", "Perks 5", "Perks 6"]], sep=', ')

    return modified
