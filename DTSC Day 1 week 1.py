# python - m venv venv/ virtual enviornment


import pandas as pd

def clean_data(path:str) -> pd.DataFrame:
    """Clean data and return only the necessary columns

    Args: path(str): location of the file on our computers

    returns:
        pd.DataFrame: the out put dataframe with the correct column"""

    assert path[-4:] == '.csv'
    df pd.read_csv(path)
    return df[['wine','acidity', 'quality']]

"""git push origion main 

THis is how you would push something ot the git hub """







