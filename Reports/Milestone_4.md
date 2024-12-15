# Milestone 4 Report 

*DSTA24 Fall Term 2024 - Group 3*

__*Authors*__
- *Vishal Alluri* 
- *Maanya Bagga*
- *Tommaso Fruci*


## Task 2

Since our machine learning model is classifying image, the metric that we chose to optimise the model were - 

**Accuracy scores** - This is a common mentric used in classification problems. We chose this metric based on the fact that our dataset is balanced, therefore, this metric is useful to us. The accuracy score will tell us how many digit predictions are accurate.

**Confusion matrix** - We decided to use confusion matrix as it is a useful representation of the model reults. We can analyse where the model is struggling i.e. which digit's image is the model classifying incorrectly thereafter use that information to improve the model.

**Loss function** - The model also tracks the loss function, however, that was already in the code since the beginning. Loss function is more suited when one needs to optimise the model during training which we didn't do this time.

**Precision** - Though precision can handle multic-classsification, but currently one particular digit isn't more important than the rest, maybe in the future depending on the problem at hand precision metric can be useful.


- We set up git secret to share the private keys securely. While setting up git secret we selected an algorithm we want to use for encryption and decryption.

**Issues encountered**
- encountered some memory issues while installing requirements which were sorted by cleaning cache and deleting unnecessary stuff.
- Encountered an issue while building the docker image, it was unable to access the entrypoint file. The path/name of the file were incorrect, corrected that and built it again.

- It would not allow me to use two CMD therefore, had to use ENTRYPOINT to tell docker to run the entrypoint script first.
```
ENTRYPOINT ["/app/Entrypoint.sh"]
```
- The major issue that we encountered was memory issue while building the docker container.

