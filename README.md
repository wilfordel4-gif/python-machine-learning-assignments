# python-machine-learning-assignments
Student information
Name WILFORD ESHIKUMO
supervised machine learning description

Project Description: Student Exam Score Prediction

This project implements a supervised machine learning pipeline using Linear Regression to predict a student's final examination score based on the total number of hours they studied. By analyzing historical student performance data, the model establishes a clear mathematical relationship (a line of best fit) between study time and academic outcomes. This allows educators to input a specific number of study hours for any student and immediately receive an automated, data-driven prediction of their expected exam score
unsupervised machine learning description

Project Description: Customer Segmentation
Instructions for installing dependencies and running your code.
Step 1: Install Python

Ensure you have Python 3.8 or higher installed on your system. You can verify your installation by opening a terminal (Linux/macOS) or Command Prompt/PowerShell (Windows) and running:
bash
python --version
Step 2: Set Up a Virtual Environment (Recommended)

Creating an isolated environment prevents library version conflicts with other projects on your machine.
• On Windows:powershell
python -m venv ml_env
ml_env\Scripts\activate

Step 3: Install Required Dependencies

Both projects rely on standard scientific data stacks. Run the following command to download and install all necessary dependencies via pip:
bash
pip install numpy matplotlib scikit-learn

Package	Purpose
numpy	Handles numerical arrays, dataset structures, and vector operations.
scikit-learn	Contains the algorithmic models (LinearRegression, KMeans), data splitters, scalers, and validation metrics.
matplotlib	Handles structural plot generations and data distribution visuals.


Step 4: Save the Code Files

1. Create a project directory on your computer.
2. For the supervised project, save the code inside a file named predict_scores.py.
3. For the unsupervised project, save the code inside a file named customer_segments.py.

Step 5: Run the Applications


• To run the Student Prediction model:bash
python .py
• To run the Customer Segmentation model:bash
python unsupervised_ML.py


This project implements an unsupervised machine learning pipeline using K-Means Clustering to automatically group supermarket customers based on their monthly spending habits and shopping frequency. Because customer behavior data does not come with pre-assigned category labels, the algorithm analyzes the natural spatial proximity between data points in a two-dimensional feature space. This enables the marketing team to uncover distinct customer personas (e.g., high-spending frequent shoppers vs. low-spending occasional visitors) and execute highly targeted business strategies without requiring manual classification.

1. What is Supervised Machine Learning?

Supervised machine learning is a type of machine learning where the model is trained on a labeled dataset. This means that for every input data point in the training set, the corresponding correct output (or "ground truth" label) is already provided. The model learns a mapping function from the inputs to the outputs, aiming to accurately predict the labels for new, unseen data.

2. What is Unsupervised Machine Learning?

Unsupervised machine learning is a type of machine learning where the model is trained on an unlabeled dataset. The algorithm is given raw data without any explicit output labels or target variables. Its goal is to explore the data, find hidden patterns, uncover underlying structures, or group similar data points together entirely on its own.

3. Difference Between Supervised and Unsupervised Learning


Feature	Supervised Learning	Unsupervised Learning
Data Type	Input data paired with explicit labels (targets).	Input data is unlabeled (raw features only).
Primary Goal	Predict outcomes or classify new observations.	Discover hidden patterns, clusters, or structures.
Feedback Loop	Direct feedback mechanism (measures error against ground truth).	No feedback mechanism (no ground truth to compare against).
Core Tasks	Classification, Regression.	Clustering, Dimensionality Reduction, Association.


4. Why is Linear Regression Considered Supervised Learning?

Linear Regression is supervised because it requires a labeled target variable (\(y\)) to map against its input features (\(x\)).
• During training, the algorithm calculates the error between its predicted continuous values and the actual known values.
• It uses optimization techniques (like Gradient Descent) to minimize this error, explicitly relying on the presence of labels to learn the best-fitting line.

5. Why is K-Means Considered Unsupervised Learning?

K-Means is unsupervised because it groups data strictly based on inherent feature similarities without using any pre-assigned category labels.
• The algorithm looks at the spatial distance between data points in a multi-dimensional feature space.
• It groups data points into \(K\) distinct clusters based purely on proximity, without knowing what those clusters represent or having a target variable to guide its accuracy.

6. What is the Difference Between fit() and predict()?

• fit(): This method executes the training phase. The algorithm ingests the training data, learns the underlying patterns, adjusts internal weights/parameters, and builds the mathematical model.
• predict(): This method executes the inference phase. Once the model is trained, predict() applies the learned parameters to new, unseen input features to generate predictions or classifications.

7. Real-World Applications


Supervised Learning

• Email Spam Detection: Classifying incoming emails as "Spam" or "Not Spam" based on historical, labeled email datasets.
• Credit Score Profiling: Predicting a borrower's likelihood of default (a numerical risk score) using historical loan repayment history.

Unsupervised Learning

• Customer Segmentation: Grouping e-commerce shoppers into distinct clusters based on purchasing habits to design targeted marketing campaigns.
• Anomaly Detection: Identifying unusual, non-matching transaction patterns in banking logs to catch credit card fraud before it is reported.
