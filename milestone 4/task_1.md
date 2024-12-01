# Task 1

- Experiment Management allows you to organize and compare different machine learning experiments while training models. It is important beacuse it keep track of all the important metrics which are helpful to reproduce the experiments and also helps you to compare different models in order to identify the most efficient solution.

- A metric in ML is a measure used to evaluate the performance of a model. Metrics are chosen based on the type of problem (regression, classification). Examples of measures are accuracy, precision, recall, F1 score.

- Precision measures how many of the predictions that were "positive" are actually correct. It is the share of 'true positives' in the total positives (true positives + false positives).
Recall measures how many of the pactual ositives were actually correctly predicted. It is the share of 'true positives' in the total of true positives + false negatives.
There is a trade-off because increasing precision may decrease recall. This happens because if you want higher precision you'll make stricter predictions, which help to reduce the chance of false positives but it also may miss some of the true positives.
Instead, increasing recallmay decrease precision because making less stricter predictions will allow you to capture more true positives but at the same time also increases false positives.

- AUROC is the Area Under The Receiving Operating Characteristics Curve and it a metric that evaluates how well the model separates two classes (the performance of a binary classifier). The higher value possible is a score of 1.0, which indicates that the model is perfectly distinguishing between classes. The more the value is to 1.0, the higher is the ability of the model to distiguish between the two classes.

- A Confusion Matrix is a table that shows how well a classification model is working, summarizing the results. It shows the number of: True Positives (positive cases correctly predicted) - True Negatives (negative cases correctly predicted) - False Positives (positive cases incorrectly predicted) - False negatives (negative cases incorrectly predicted). 