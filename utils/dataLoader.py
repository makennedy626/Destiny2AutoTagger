import os
import pandas as pd
from pathlib import Path

# def loadData(filepath, header='infer'):
#     """Performs pandas.read_csv(filepath, header) and returns the dataframe.
#     """
#     return pd.read_csv(filepath, header=header)

def makeCatalog(project_path):
    """Downloads the files from online and store them in project_path/data/filename. Then creates a dictionary of {dataframe_name: dataframe} pairs that can be queried.
    """

    catalog = {}

    from utils.downloadData import downloadFilesFromURL

    downloadFilesFromURL('https://docs.google.com/spreadsheets/d/1YWX2NCw8joV0T15ivF7Hu98iMC1Za4lzMWpwJiMx6q8/export?format=csv&id=1YWX2NCw8joV0T15ivF7Hu98iMC1Za4lzMWpwJiMx6q8&gid=1967975290', project_path, "forsakenPvE.csv")
        #'https://docs.google.com/spreadsheets/d/1YWX2NCw8joV0T15ivF7Hu98iMC1Za4lzMWpwJiMx6q8/edit#gid=1967975290', project_path, "forsakenPvE.html")
    downloadFilesFromURL('https://docs.google.com/spreadsheets/d/1YWX2NCw8joV0T15ivF7Hu98iMC1Za4lzMWpwJiMx6q8/export?format=csv&id=1YWX2NCw8joV0T15ivF7Hu98iMC1Za4lzMWpwJiMx6q8&gid=487026473', project_path, "forsakenPvP.csv")
        #'https://docs.google.com/spreadsheets/d/1YWX2NCw8joV0T15ivF7Hu98iMC1Za4lzMWpwJiMx6q8/edit#gid=487026473', project_path, "forsakenPvP.html")
    downloadFilesFromURL('https://docs.google.com/spreadsheets/d/1D4Fu6fSoSrPhlSOmCn_n1bItSNGZHbZxNI6_lVpoeB8/export?format=csv&id=1D4Fu6fSoSrPhlSOmCn_n1bItSNGZHbZxNI6_lVpoeB8&gid=0', project_path, "blackArmory.csv")
        #'https://docs.google.com/spreadsheets/d/1D4Fu6fSoSrPhlSOmCn_n1bItSNGZHbZxNI6_lVpoeB8/edit#gid=0', project_path, "blackArmory.html")
    downloadFilesFromURL('https://docs.google.com/spreadsheets/d/1ZEr_TCdCenhBcviXQ5iAKzrPWa_oEav5rvXdy4QaD6I/export?format=csv&id=1ZEr_TCdCenhBcviXQ5iAKzrPWa_oEav5rvXdy4QaD6I&gid=0', project_path, "drifter.csv")
        #'https://docs.google.com/spreadsheets/d/1ZEr_TCdCenhBcviXQ5iAKzrPWa_oEav5rvXdy4QaD6I/edit#gid=0'
    downloadFilesFromURL('https://docs.google.com/spreadsheets/d/1wZkZCt6YeMEkZ2-SxyLCUECVP_o_1wgsRPiC2LblkAM/export?format=csv&id=1wZkZCt6YeMEkZ2-SxyLCUECVP_o_1wgsRPiC2LblkAM&gid=0', project_path, "opulence.csv")
        #'https://docs.google.com/spreadsheets/d/1wZkZCt6YeMEkZ2-SxyLCUECVP_o_1wgsRPiC2LblkAM/edit#gid=0'
        
    catalog["armor"] = pd.read_csv('{}/data/destinyArmor.csv'.format(project_path))
    catalog["weapons"] = pd.read_csv('{}/data/destinyWeapons.csv'.format(project_path))
    catalog["forsakenPVE"] = pd.read_csv("{}/data/forsakenPvE.csv".format(project_path), header=6)
    catalog["forsakenPVP"] = pd.read_csv("{}/data/forsakenPvP.csv".format(project_path), header=6)
    catalog["blackArmory"] = pd.read_csv("{}/data/blackArmory.csv".format(project_path), header=7)
    catalog["drifter"] = pd.read_csv("{}/data/drifter.csv".format(project_path), header=7)
    catalog["opulence"] = pd.read_csv("{}/data/opulence.csv".format(project_path), header=7)

    return catalog

