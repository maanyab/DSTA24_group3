"""
Title: Training and Evaluation 
Description: Functions to Train and Evaluate the Neural Network model
"""
import wandb

# Initialize W&B project
wandb.init(project="model_evaluation", name="evaluating_models")

def train_model(model, x_train, y_train, x_test, y_test, epochs=15):
    """
    Trains the given model on the training data  and logs the metrics on W&B.

    Args:
        model: model to be trained.
        x_train: Training input data.
        y_train: Training target data.
        batch_size: Number of samples in each batch (default:128)
        epochs (int): Number of epochs to train the model (default: 15).
        validation_split (float): Fraction of training data to be used as validation (default: 0.1).

    Returns:
        a trained model
    """
    # Compile the model
    model.compile(
        loss="categorical_crossentropy",
        optimizer="Nadam",
        metrics=["accuracy"]
    )

    for epoch in range(epochs):
        # Train the model for one epoch
        history = model.fit(x_train,
                        y_train, 
                        epochs=1, 
                        batch_size=128, 
                        validation_data=(x_test, y_test)
                    )
        
        # Log loss and accuracy to W&B
        wandb.log({
            "epoch": epoch + 1,
            "loss": history.history['loss'][0],  # Log loss
            "accuracy": history.history['accuracy'][0]  # Log accuracy
        })
    
    return model



