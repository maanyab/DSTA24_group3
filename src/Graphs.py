
import wandb
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def log_confusion_matrix(y_true, y_pred, epoch):
    """
    Log a confusion matrix to W&B.

    Returns:
        Confusion Matrix
    """
    # Compute the confusion matrix
    cm = plt.confusion_matrix(y_true.argmax(axis=1), y_pred.argmax(axis=1))

    # Plot confusion matrix
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",xticklabels=np.arange(10), yticklabels=np.arange(10))
    plt.xlabel("Predicted")
    plt.ylabel("True")
    plt.title(f"Confusion Matrix- Epoch {epoch}")

    # Save and log to W&B
    plt.savefig(f"confusion_matrix_epoch_{epoch}.png")
    wandb.log({"confusion_matrix": wandb.Image(f"confusion_matrix_epoch_{epoch}.png")})





