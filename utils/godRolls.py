import numpy as np
import pandas as pd

def checkForGodRolls(df):
    """
    """
    results = pd.DataFrame(columns=["Name", "godMag", "godSights", "godPerk1", "godPerk2"])

    for row in df.itertuples():
        
        results.loc[row.Index, "Name"] = row.Name

        if str(row.Magazine) in str(row.perksList):
            results.loc[row.Index, "godMag"] = 1
        else:
            results.loc[row.Index, "godMag"] = 0
        if str(row._8) in str(row.perksList):
            results.loc[row.Index, "godSights"] = 1
        else:
            results.loc[row.Index, "godSights"] = 0
        if str(row._6) in str(row.perksList):
            results.loc[row.Index, "godPerk1"] = 1
        else:
            results.loc[row.Index, "godPerk1"] = 0
        if str(row._7) in str(row.perksList):
            results.loc[row.Index, "godPerk2"] = 1
        else:
            results.loc[row.Index, "godPerk2"] = 0

    results["godScore"] = results["godMag"]+results["godSights"]+results["godPerk1"]+\
        results["godPerk2"]

    return results


def updateTags(data):
    """Looks at cumulative score ``godScore`` and tags the item as ``Keep`` or ``Junk``
    """
    df = data
    df['Tag'] = np.where(df['godScore'] == 4, 'Keep', df['Tag'])
    df['Tag'] = np.where(df['godScore'] == 0, 'Junk', df['Tag'])

    return df
