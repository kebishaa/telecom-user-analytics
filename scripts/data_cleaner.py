from helper import helper
import numpy as np
import pandas as pd

class CleanTelecomData:
    def __init__(self, df: pd.DataFrame):
        self.df = df
        
        print('Cleaning on the way ....')

    def drop_duplicate(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        drop duplicate rows
        """
        df.drop_duplicates(inplace=True)

        return df

    def convert_to_datetime(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        convert column to datetime
        """

        df['Start'] = pd.to_datetime(
            df['Start'])
        df['End'] = pd.to_datetime(
            df['End'])

        return df

    

    def handle_missing_qantitative_data_with_mean(self, df: pd.DataFrame, method="mean"):

        numeric_data = ['int16', 'int32', 'int64',
                        'float16', 'float32', 'float64']

        all_cols = df.columns.to_list()
        num_cols = [c for c in all_cols if df[c].dtypes in numeric_data]

        if (method == "mean"):

            for col in num_cols:
                df[col] = df[col].fillna(df[col].mean())

            return df

        elif method == "ffill":

            for col in num_cols:
                df[col] = df[col].fillna(method='ffill')

            return df

        elif method == "bfill":

            for col in num_cols:
                df[col] = df[col].fillna(method='bfill')

            return df
        else:
            print("Method unknown")
            return df
    
    def handle_missing_categorical_data_with(self, df: pd.DataFrame, method="ffill"):

        numeric_data = ['int16', 'int32', 'int64',
                        'float16', 'float32', 'float64']

        all_cols = df.columns.to_list()
        num_cols = [c for c in all_cols if not df[c].dtypes in numeric_data]
        
        if method == "ffill":

            for col in num_cols:
                df[col] = df[col].fillna(method='ffill')

            return df

        elif method == "bfill":

            for col in num_cols:
                df[col] = df[col].fillna(method='bfill')

            return df
        else:
            print("Method unknown")
            return df

    def handle_outliers(self, df, col):
        df = df.copy()
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)

        lower_bound = q1 - ((1.5) * (q3 - q1))
        upper_bound = q3 + ((1.5) * (q3 - q1))

        df[col] = np.where(df[col] < lower_bound, lower_bound, df[col])
        df[col] = np.where(df[col] > upper_bound, upper_bound, df[col])

        return df

    def convert_to_mega_bytes(self, df):

        df = self.__convert_bytes_to_megabytes(df, 'social_media_dl_(bytes)')
        df = self.__convert_bytes_to_megabytes(df, 'social_media_ul_(bytes)')

        df = self.__convert_bytes_to_megabytes(df, "google_dl_(bytes)")
        df = self.__convert_bytes_to_megabytes(df, "google_ul_(bytes)")

        df = self.__convert_bytes_to_megabytes(df, "email_dl_(bytes)")
        df = self.__convert_bytes_to_megabytes(df, "email_ul_(bytes)")

        df = self.__convert_bytes_to_megabytes(df, "youtube_dl_(bytes)")
        df = self.__convert_bytes_to_megabytes(df, "youtube_ul_(bytes)")

        df = self.__convert_bytes_to_megabytes(df, "netflix_dl_(bytes)")
        df = self.__convert_bytes_to_megabytes(df, "netflix_ul_(bytes)")

        df = self.__convert_bytes_to_megabytes(df, "gaming_dl_(bytes)")
        df = self.__convert_bytes_to_megabytes(df, "gaming_ul_(bytes)")

        df = self.__convert_bytes_to_megabytes(df, "other_dl_(bytes)")
        df = self.__convert_bytes_to_megabytes(df, "other_ul_(bytes)")

        df = self.__convert_bytes_to_megabytes(df, "total_dl_(bytes)")
        df = self.__convert_bytes_to_megabytes(df, "total_ul_(bytes)")

        
    
    def __convert_bytes_to_megabytes(df, bytes_data):

        megabyte = 1*10e+5
        megabyte_col = df[bytes_data] / megabyte

        return megabyte_col