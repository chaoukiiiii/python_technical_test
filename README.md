# python_technical_test


# Pipeline global de projet

 organisation de projet:

    |── main.py
    |── datasources_config
    |── input
    |── output
    |── data_preparation
    |── data_transformation
    |── data_export
    |── utils.py
    |── sql
    |── tests

`main.py` est le entry point de repo , il permet de declencher les pipelines pour generer le resultat finale: fichier json dans le dossier output.

- **La data préparation**  consiste a charger les fichiers csv et json dans des pandas dataframes. aprés il y a une etape de preprocessing et nettoyage pour assuer la qualité des données, le resultat de ce pipeline est un dictionnaire qui contients les differents dataframe. Le fichier config_src contient la configurations pour chaque fichier en input.

- **La data transformation** cette etape consiste a faire les transformations necessaires pour creer les relations entre les `drugs` et les titres des publications des journaux. la serie des traitements genere une dataframe qui contient pour chaque couple `(drug,journal)` la liste de `pubmed` et `clinical_trials` avec reference date.
cette structure permet de filtrer pour chaque journal , les drugs mentionnées , aussi de filtrer les differents journaux ou le drug est apparu


Pour exeecuter le script:

`pip install -r requirement.txt`

`python ./main.py`

le resultat se trouve dans le dossier output

- **Comment gérer de grosse volumetrie**:
pandas n'est pas fait pour des volumetries importantes meme si il y a le feature pour lire les fichiers en `chnuks` avec `low_memory` en utilisant la bibleotheque `dask`. si on veut adresser une grosse volumetrie il nous faut un moteur de calcule distrbiuer comme apache beam ou spark.. si on veut partir le fait d'utiliser beam , il y a un cout de modification mineur par rapport au modification de code vers pyspark. 

- **les requetes sql sont dans le dossier sql au racine*

