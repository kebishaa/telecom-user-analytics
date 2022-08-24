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
def convertByteMB(self, coll) -> pd.DataFrame:
        for col in coll:
            self.df[col] = self.df[col] / 1*10e+5
            self.df.rename(
                columns={col: f'{col[:-7]}(MegaBytes)'}, inplace=True)
        print('Byte to MB change error')
        return self.df
################################################################################################
#  Data Information script
################################################################################################
def show_datatypes(self) -> pd.DataFrame:
        return self.df.dtypes
def show_data_description(self) -> pd.DataFrame:
        return self.df.describe()
def show_data_information(self) -> pd.DataFrame:
        return self.df.info()
def show_statistical_info(self) -> pd.DataFrame:
        return self.df.agg(['mean'])
def show_correlation(self) -> pd.DataFrame:
        return self.df.corr()