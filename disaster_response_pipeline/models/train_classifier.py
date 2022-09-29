import sys

import nltk
import pandas as pd
from sqlalchemy import create_engine

from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.model_selection import GridSearchCV
from sklearn.multioutput import MultiOutputClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib
nltk.download(['punkt', 'wordnet', 'omw-1.4'])


def load_data(database_filepath):
    """
    load and read the database table.

    Args:
        database_filepath: Path to the database file.

    Returns:
        X: the independent features
        Y: the target feature
        category_names: list of the categories name/class
    """
    engine = create_engine(f'sqlite:///{database_filepath}')
    df = pd.read_sql_table(con=engine, table_name="disaster_response")
    # print(df.head())
    # print(df.columns)
    X = df['message']
    Y = df.iloc[:, 4:]
    category_names = list(df.columns[4:])
    return X, Y, category_names


def tokenize(text):
    """
    process the raw text and return the clean text after applying word Tokenization and lemmatization.

    Args:
        text: Text to be tokenized and lemmatized.

    Returns:
        clean_tokens: Returns cleaned tokens
    """
    # call the word_tokenize function and pass the 'text' to be tokenized.
    tokens = word_tokenize(text)

    # initialize the WordNet lemmatizer object.
    lemmatizer = WordNetLemmatizer()

    clean_tokens = []

    # iterate over all the word tokens.
    for tok in tokens:
        # apply lemmatization on each token followed by lowercase normalization and leading/trailing white-space removal.
        clean_tok = lemmatizer.lemmatize(tok).lower().strip()
        clean_tokens.append(clean_tok)

    return clean_tokens


def build_model():
    """
    Builds classifier ML pipeline and optimize the model with GridSearchCV.

    Returns:
        cv: the final model
    """
    pipeline = Pipeline([
        ('vect', CountVectorizer(tokenizer=tokenize)),
        ('tfidf', TfidfTransformer()),
        ('clf', MultiOutputClassifier(RandomForestClassifier()))
    ])

    parameters = {
        'clf__estimator__n_estimators': [50, 100],
    }

    cv = GridSearchCV(pipeline, param_grid=parameters, verbose=0)

    return cv


def evaluate_model(model, X_test, Y_test, category_names):
    """
    evaluate the trained model

    Args:
        model: the trained model
        X_test: X component of the test dataset
        Y_test: Y component of the test dataset
        category_names: list of category columns

    """
    y_pred = model.predict(X_test)
    y_pred = pd.DataFrame(y_pred, columns=category_names)
    # print(y_pred.head())

    for category in category_names:
        print(f"classification report for '{category}':")
        report = classification_report(Y_test[category], y_pred[category])
        print(report)


def save_model(model, model_filepath):
    """
    Save the trained model at given model_filepath.
    Args:
        model: the trained model object
        model_filepath: path to save the model file
    """
    joblib.dump(model, model_filepath, compress=True)


def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print(f'Loading data...\n    DATABASE: {database_filepath}')
        X, Y, category_names = load_data(database_filepath)
        # print(category_names)

        # split the dataset into train and test set
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

        print('Building model...')
        model = build_model()

        print('Training model...')
        model.fit(X_train, Y_train)

        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test, category_names)

        print(f'Saving model...\n    MODEL: {model_filepath}')
        save_model(model, model_filepath)
        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database as the first argument and the filepath of the pickle file to save the model to as the second argument. \n\nExample: python train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()


# RUN THIS SCRIPT TO TRAIN THE MODEL
# python models\train_classifier.py data\DisasterResponse.db models\response_classifier.pkl