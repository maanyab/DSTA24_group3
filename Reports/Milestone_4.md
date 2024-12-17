# Milestone 4 Report 

*DSTA24 Fall Term 2024 - Group 3*

__*Authors*__
- *Vishal Alluri* 
- *Maanya Bagga*
- *Tommaso Fruci*

## Task 1

- **Experiment Management** allows you to organize and compare different machine learning experiments while training models. It is important beacuse it keep track of all the important metrics which are helpful to reproduce the experiments and also helps you to compare different models in order to identify the most efficient solution.

- A **metric** in ML is a measure used to evaluate the performance of a model. Metrics are chosen based on the type of problem (regression, classification). Examples of measures are accuracy, precision, recall, F1 score.

- **Precision** measures how many of the predictions that were "positive" are actually correct. It is the share of 'true positives' in the total positives (true positives + false positives). Recall measures how many of the pactual ositives were actually correctly predicted. It is the share of 'true positives' in the total of true positives + false negatives. There is a trade-off because increasing precision may decrease recall. This happens because if you want higher precision you'll make stricter predictions, which help to reduce the chance of false positives but it also may miss some of the true positives. Instead, increasing recallmay decrease precision because making less stricter predictions will allow you to capture more true positives but at the same time also increases false positives.

- **AUROC** is the Area Under The Receiving Operating Characteristics Curve and it a metric that evaluates how well the model separates two classes (the performance of a binary classifier). The higher value possible is a score of 1.0, which indicates that the model is perfectly distinguishing between classes. The more the value is to 1.0, the higher is the ability of the model to distiguish between the two classes.

- A **Confusion Matrix** is a table that shows how well a classification model is working, summarizing the results. It shows the number of: True Positives (positive cases correctly predicted) - True Negatives (negative cases correctly predicted) - False Positives (positive cases incorrectly predicted) - False negatives (negative cases incorrectly predicted).


## Task 2

Since our machine learning model is classifying image, the metric that we chose to optimise the model were - 

**Accuracy scores** - This is a common mentric used in classification problems. We chose this metric based on the fact that our dataset is balanced, therefore, this metric is useful to us. The accuracy score will tell us how many digit predictions are accurate.

**Confusion matrix** - We decided to use confusion matrix as it is a useful representation of the model reults. We can analyse where the model is struggling i.e. which digit's image is the model classifying incorrectly thereafter use that information to improve the model.

**Loss function** - The model also tracks the loss function, however, that was already in the code since the beginning. Loss function is more suited when one needs to optimise the model during training which we didn't do this time.

**Precision** - Though precision can handle multic-classsification, but currently one particular digit isn't more important than the rest, maybe in the future depending on the problem at hand precision metric can be useful.

- We set up git secret to share the private API keys securely. While setting up git secret we selected an algorithm we want to use for encryption and decryption.

**Issues encountered**
- encountered some memory issues while installing requirements which were sorted by cleaning cache and deleting unnecessary stuff.
- Encountered an issue while building the docker image, it was unable to access the entrypoint file. The path/name of the file were incorrect, corrected that and built it again.

- It would not allow me to use two CMD therefore, had to use ENTRYPOINT to tell docker to run the entrypoint script first.
```
ENTRYPOINT ["/app/Entrypoint.sh"]
```
- The major issue that we encountered was memory issue while building the docker container.

- There was an issue while building docker container while running the entry point command, therefore, tweaked it a little bit as below.

```
ENTRYPOINT ["/bin/bash","/app/Entrypoint.sh"]
```
- Encountring error - AttributeError: 'Node' object has no attribute 'inbound_layers' - while mapping confusion matrix, tried to fix it but couldn't so didn't use it for wandb. 


**Training run links for wandb**

- Only a sample of images from the dataset
  https://wandb.ai/maanya-bagga-university-of-luzern/model_evaluation/runs/64lax4zd

- loss function:"categorical_crossentropy"
  https://wandb.ai/maanya-bagga-university-of-luzern/model_evaluation/runs/m49hou3n

- loss function: 'cosine_similarity'- Usually used to measure similarity, such as in text or image similarity tasks.
  https://wandb.ai/maanya-bagga-university-of-luzern/model_evaluation/runs/15pugm8d

- Optimiser:Nadam
  https://wandb.ai/maanya-bagga-university-of-luzern/model_evaluation/runs/ugkd2kqe

- Changed a layer: layers.Conv2D(64, kernel_size=(5, 5), activation="tanh")
  https://wandb.ai/maanya-bagga-university-of-luzern/model_evaluation/runs/zux9mye4

- Increased epoc and batchsize 
  https://wandb.ai/maanya-bagga-university-of-luzern/model_evaluation/runs/uairk7k2

- Run with hyperaparmeters logged
  https://wandb.ai/maanya-bagga-university-of-luzern/model_evaluation/runs/zwhkhtj8