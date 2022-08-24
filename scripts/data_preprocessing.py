import pandas as pd
import numpy as np


class data_preProcessing_script:

    def __init__(self, df: pd.DataFrame) -> None:
        self.df = df

################################################################################################
#  Data cleaning script
################################################################################################

    def drop_duplicates(self) -> pd.DataFrame:
        droped = self.df[self.df.duplicated()].index
        return self.df.drop(index=droped, inplace=True)
def convert_to_numbers(self) -> pd.DataFrame:
        self.df = self.df.apply(pd.to_numeric, errors='coerce')
        return self.df