# Import libraries
import sys

import pandas as pd

from sqlalchemy import create_engine

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


def load_datasets(messages_file, categories_file):
    """
    loads and merges the disaster_messages.csv and disaster_categories.csv files

    Args:
        messages_file: the path of disaster_messages.csv file.
        categories_file: the path of disaster_categories.csv file.

    Returns:
        df: the merged dataframe of messages and categories file.
    """

    # load the messages dataset
    messages = pd.read_csv(messages_file)
    # print(messages.head())

    # load the categories dataset
    categories = pd.read_csv(categories_file)
    # print(categories.head())

    # merge the datasets
    df = messages.merge(categories, how='outer', on='id')
    # print(df.head())

    return df


def data_processing(df):
    """
    clean and transform the input dataframe.

    Args:
        df: the unprocessed merged dataframe.

    Returns:
        clean_df: the processed & transformed dataframe.
    """

    # create a dataframe of the 36 individual categories columns
    categories = df['categories'].str.split(';', expand=True)
    # print(categories.head())

    # select the first row of the categories dataframe
    row = categories.iloc[0, :]

    # use this row to extract a list of new column names for categories.
    category_colnames = row.apply(lambda x: x[:-2])
    # print(category_colnames)

    # rename the columns of 'categories'
    categories.columns = category_colnames
    # print(categories.head())

    for column in categories:
        # set each value to be the last character of the string
        categories[column] = categories[column].apply(lambda x: x[-1])

        # convert column from string to numeric
        categories[column] = categories[column].apply(lambda x: int(x))

    # print(categories.head())

    # drop the original categories column from 'df'
    df.drop(columns=['categories'], inplace=True)
    # print(df.head())

    # concatenate the original dataframe with the new 'categories' dataframe
    df = pd.concat([df, categories], axis=1)
    # print(df.head())

    # check number of duplicates
    # print(df.duplicated())

    # drop duplicates
    clean_df = df.drop_duplicates()
    # print(clean_df.shape)

    # check number of duplicates
    # print(df.duplicated().sum())
    return clean_df


def save_dataset(clean_df, database_path):
    """
    load the cleaned dataframe into the sql database.

    Args:
        clean_df: the processed dataframe
        database_path: database path

    Returns:
        None
    """
    # create the connection and insert the data to the database.
    engine = create_engine(f"sqlite:///{database_path}")
    clean_df.to_sql(name="disaster_response", con=engine, index=False)


if __name__ == "__main__":
    # print(sys.argv)

    if len(sys.argv) == 4:

        save_dataset(data_processing(load_datasets(sys.argv[1], sys.argv[2])), sys.argv[3])
    else:
        print("Please follow the given format:\npython python_file.py messages_file_name.csv, \
        categories_file_name.csv, database_file.db")

# RUN THE SCRIPT
# python process_data.py disaster_messages.csv disaster_categories.csv DisasterResponse.db