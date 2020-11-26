import pandas as pd
import numpy as np

def load_and_process(filePathCSV):
    df1 = (pd.read_csv(filePathCSV)
           .drop(['TOI/GP','FOW%','S%'], axis=1)
           .rename(columns = {'GP':'GamesPlayed' , '+/-':'PlusMinus', 'PIM':'PenaltyMins', 'S':'Shots', 'S/C':'Hand'})
    )
    df2 = (df1 
           .loc[lambda x: x['Shots']>50]
           .loc[lambda x: x['GamesPlayed']>70]
           .sort_values(by = ['G'], ascending = False)
    )
    return df2
   
    