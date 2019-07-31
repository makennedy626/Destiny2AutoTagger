import os
import pandas as pd
from pathlib import Path

def loadData(filepath, header='infer'):
    """Performs pandas.read_csv(filepath, header) and returns the dataframe.
    """
    return pd.read_csv(filepath, header=header)

def makeCatalog(project_path):
    """Creates a dictionary of {dataframe_name: dataframe} pairs that can be queried.
    """

    catalog = {}

    catalog["armor"] = loadData('{}/data/destinyArmor.csv'.format(project_path))
    catalog["weapons"] = loadData('{}/data/destinyWeapons.csv'.format(project_path))
    catalog["forsakenPVE"] = loadData("{}/data/forsakenPvE.csv".format(project_path), header=6)
    catalog["forsakenPVP"] = loadData("{}/data/forsakenPvP.csv".format(project_path), header=6)
    catalog["blackArmory"] = loadData("{}/data/blackArmory.csv".format(project_path), header=7)
    catalog["drifter"] = loadData("{}/data/drifter.csv".format(project_path), header=7)
    catalog["opulence"] = loadData("{}/data/opulence.csv".format(project_path), header=7)

    return catalog

