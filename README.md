# python-machine-learning-assignments
Student information
Name WILFORD ESHIKUMO

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
