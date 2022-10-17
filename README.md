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

main.py est le entry point de repo , il permet de declencher les pipelines pour generer le resultat finale: fichier json dans le dossier output.

- **La data préparation**  consiste a charger les fichiers csv et json dans des pandas dataframes. aprés il y a une etape de preprocessing et nettoyage pour assuer la qualité des données, le resultat de ce pipeline est un dictionnaire qui contients les differents dataframe.

- **La data transformation** cette etape consiste a faire les transformations necessaires pour creer les relations entre les drugs et les titres des publications des journaux. la serie des traitements genere une dataframe qui contient pour chaque couple (drug,journal) la liste de pubmed et clinical_trials avec reference date.

