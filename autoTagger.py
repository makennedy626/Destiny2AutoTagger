import os
from pathlib import Path

from utils.dataLoader import makeCatalog
from utils.godRolls import checkForGodRolls, updateTags
from utils.weaponsConverter import combineData, modifyWeapons


def autoTagger():
    """
    """
    project_path = Path(os.getcwd())

    catalog = makeCatalog(project_path=project_path)

    godRolls = combineData(
        df_list = [
            catalog.get("opulence"),
            catalog.get("drifter"),
            catalog.get("blackArmory"),
            catalog.get("forsakenPVE"),
            catalog.get("forsakenPVP"),
            ]
            )

    modifiedWeapons = modifyWeapons(catalog.get("weapons"))

    matches = modifiedWeapons.join(godRolls.set_index("Name"), on="Name")

    results = checkForGodRolls(matches)

    tagged = catalog.get("weapons").\
        join(results.set_index("Name"), on="Name").\
            pipe(updateTags).drop_duplicates()

    saved = tagged.to_csv('{}/data/updatedWeapons.csv'.format(project_path))


if __name__ == '__main__':
    autoTagger()
