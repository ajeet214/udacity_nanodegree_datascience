## **Disaster Response Pipeline Project**

### **Description :**

This project is about building the ETL, NLP and ML pipeline and train, evaluate and optimize the model for classifying the message into 36 different classes/categories.

This project includes a web app where an emergency worker can input a new message and get classification results in several categories. The web app will also display visualizations of the data.

### **Project Components :**
As mentioned in the description, there are three components in this project.

1. **ETL Pipeline**,  
- this is a data pipeline where we load the two different datasets
- merge them together
- clean and process the dataset
- and finally store it to the sql database in a table. 


2. **ML Pipeline**, 
- In the Machine learning pipeline, we first load the cleaned data(from the ETL pipeline) from the database.
- Splits the dataset into training and test sets.
- Builds a text processing and machine learning pipeline.
- Trains and tunes a model using GridSearchCV.
- Output results on the test set.
- and finally Exports the final model as a pickle file.


3. **Flask Web App**, 
- In this section, we create the flask web application to perform the Inference on our trained model. And plot some visualization dashboard.

Below are a few screenshots of the web app.

![alt text](https://video.udacity-data.com/topher/2018/September/5b967bef_disaster-response-project1/disaster-response-project1.png)

![alt text](https://video.udacity-data.com/topher/2018/September/5b967cda_disaster-response-project2/disaster-response-project2.png)

### **Project structure :**
The file structure of this project is as follows:

```python
- disaster_response_pipeline
  | - app
  | - template
  | |- master.html  # main page of web app
  | |- go.html  # classification result page of web app
  |- run.py  # Flask file that runs app
    
  - data
  |- disaster_categories.csv  # data to process 
  |- disaster_messages.csv  # data to process
  |- process_data.py
  |- InsertDatabaseName.db   # database to save clean data to
    
  - models
  |- train_classifier.py
  |- classifier.pkl  # saved model 
    
  - README.md
```
### To create the ETL pipeline, run the below command
```python
python process_data.py disaster_messages.csv disaster_categories.csv DisasterResponse.db
```
Remember to pass the parameter in the same sequence i.e.
- 1st, process_data.py (or the path of this file wherever it exists). This file consists of all the codes for the ETL pipeline.
- 2nd, disaster_messages.csv (or the path of this file wherever it exists). This is the first datasets which consists of the id, message, original and genre columns.
- 3rd, disaster_categories.csv (or the path of this file wherever it exists). This is the second datasets which consists of the id and categories columns.
- 4th, DisasterResponse.db (or the path of this file wherever you want to store). This is the database file where we store the cleaned data.

### To create the ML pipeline, run the below command
```python
python train_classifier.py ../data/DisasterResponse.db classifier.pkl
```
Remember to pass the parameter in the same sequence i.e.
- 1st, train_classifier.py (or the path of this file wherever it exists). This file consists of all the codes for the NLP & ML pipeline.
- 2nd, DisasterResponse.db (or the path of this file wherever it exists). This is the path of database file.
- 3rd, classifier.pkl (or the path of this file wherever it exists). This is the path of saved model file.

### And finally to run the Web App, 

Open a new terminal window. You should already be in the workspace folder, but if not, then use terminal commands to navigate inside the folder with the run.py file.

Type in the command line:
```python
python run.py
```
Remember here, Please check below points before running the run.py

- make sure that the database path is correct.
```python
# load data
engine = create_engine('sqlite:///../data/DisasterResponse.db')
```
- make sure that the table name is correct.
```python
df = pd.read_sql_table('disaster_response', engine)
```
- make sure that the path of model file is correct.
```python
# load model
model = joblib.load("../models/response_classifier.pkl")
```
### Acknowledgements

The starter code for the Web App has been provided by the Udacity.
