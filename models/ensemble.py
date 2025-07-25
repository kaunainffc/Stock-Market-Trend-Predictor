import numpy as np
from sklearn.metrics import accuracy_score

def vote(models, X_test, y_test=None):
    predictions = []
    weights = []

    for model in models:
        try:
            y_pred = model.predict(X_test)

            # Ensure y_pred is a 1D array
            y_pred = np.ravel(y_pred)

            acc = accuracy_score(y_test, y_pred) if y_test is not None else 1
            predictions.append(y_pred)
            weights.append(acc)

        except Exception as e:
            print(f"❌ Model prediction failed: {e}")

    predictions = np.array(predictions)

    # Ensure uniform shape before voting
    if predictions.shape[1:] != (len(X_test),):
        raise ValueError("❌ All model predictions must be 1D arrays of the same length.")

    final_pred = np.round(np.average(predictions, axis=0, weights=weights)).astype(int)

    return final_pred[-1]  # Return the latest day prediction
