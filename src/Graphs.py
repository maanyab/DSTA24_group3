
import  wandb
import matplotlib.pyplot as plt

def log_confusion_matrix(cm):
    """
    Logs a confusion matrix to W&B as an image.

    Args:
        cm: Confusion matrix (2D array).
    """
    plt.figure(figsize=(8, 8))
    plt.imshow(cm, cmap='Blues')
    plt.title("Confusion Matrix")
    plt.colorbar()
    plt.xlabel("Predicted")
    plt.ylabel("True")
    plt.xticks(range(len(cm)), range(len(cm)))  # Assuming class indices are [0, 1, ..., n-1]
    plt.yticks(range(len(cm)), range(len(cm)))
    plt.tight_layout()

    # Log the plot to W&B
    wandb.log({"Confusion Matrix": plt})
    plt.close()
