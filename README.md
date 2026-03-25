 Multi-Dataset Machine Learning & Data Analysis Project

This repository contains multiple machine learning tasks performed on real-world datasets, including data preprocessing, exploratory data analysis (EDA), linear & logistic regression, model evaluation, and dataset-specific analysis.

 Datasets
Heart Disease Dataset
Sources: Cleveland, Hungarian, Switzerland, VA datasets
Files: cleveland.data, processed.cleveland.data, hungarian.data, etc.
Task: Predict heart disease presence using medical features
MovieLens 100K Dataset
Files: ml-100k/u.data, ml-100k/u.user, ml-100k/u.item
Task: Basic data analysis on user ratings and movie metadata
IMDB Movie Reviews
File: IMDB Dataset.csv
Task: Text preprocessing, sentiment analysis
Air Quality Dataset
File: AirQualityUCI.csv
Task: Time series preprocessing, resampling, interpolation, smoothing
 Data Preprocessing
Heart Disease
Columns standardized across datasets
Missing values handled with imputation
Features like age, cholesterol, blood pressure used as inputs
Target variable: presence of heart disease
MovieLens
Ratings, user info, and movie info merged
Categorical features (occupation, genre) encoded
Dataset ready for collaborative filtering or exploratory analysis
IMDB Reviews
Reviews cleaned by:
Lowercasing
Removing punctuation and stopwords
Tokenization
Joining back cleaned tokens
Prepared for NLP or sentiment classification
Air Quality
Date and Time combined into DateTime index
Invalid timestamps dropped
Resampled hourly using mean
Linear interpolation for missing values
Optional smoothed CO column (rolling mean)
📈 Linear Regression
Applied to predict continuous variables (e.g., car prices or numerical heart metrics)
Steps:
Feature normalization
Train-test split
Model fitting
Predictions
Evaluation using:
Mean Squared Error (MSE)
Root Mean Squared Error (RMSE)
R² Score
 Logistic Regression
Applied for classification tasks (e.g., heart disease, IMDB sentiment)
Steps:
Encode categorical variables
Train-test split
Fit logistic regression
Predict class probabilities
Evaluation using:
Accuracy
Confusion matrix
Precision, Recall, F1-score
ROC curve and AUC
 Model Evaluation
Metrics for regression:
MSE, RMSE, R²
Metrics for classification:
Accuracy, Precision, Recall, F1-score
ROC-AUC
Visualizations included:
Feature distributions
Predicted vs Actual plots
Confusion matrices
ROC curves
🛠 Tools & Libraries
Python 3.12
pandas, numpy
matplotlib, seaborn
scikit-learn
NLTK (for text preprocessing)
zipfile (for compressed dataset reading)
 File Structure
project/
│
├─ datasets/
│   ├─ heart/
│   ├─ ml-100k/
│   ├─ IMDB/
│   └─ AirQuality/
│
├─ notebooks/
│   ├─ heart_analysis.ipynb
│   ├─ movielens_analysis.ipynb
│   ├─ imdb_preprocessing.ipynb
│   └─ air_quality_analysis.ipynb
│
├─ scripts/
│   └─ data_preprocessing.py
│
└─ README.md
 Notes
Always ensure correct CSV separators when reading data (',' vs ';')
Handle missing values and invalid timestamps before modeling
For NLP tasks, download NLTK data before preprocessing:
import nltk
nltk.download('stopwords')
nltk.download('punkt')
Resample and interpolate time series for consistent hourly data
