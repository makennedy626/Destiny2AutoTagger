#%%
import os
import pandas as pd
from pathlib import Path

project_path = Path(os.getcwd())
test = pd.read_html("{}/data/opulence.html".format(project_path)) # , header=7)


#%%
file_path = "{}/data/opulence.html".format(project_path)
with open(file_path, 'r') as f:
    df = pd.read_html(f.read(), match='Table')

#%%
