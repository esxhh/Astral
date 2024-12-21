def evaluate_model(model, test_data, test_labels):
    from sklearn.metrics import accuracy_score, classification_report

    # Make predictions on the test data
    predictions = model.predict(test_data)

    # Calculate accuracy
    accuracy = accuracy_score(test_labels, predictions)

    # Generate a classification report
    report = classification_report(test_labels, predictions)

    return accuracy, report


if __name__ == "__main__":
    import joblib
    import pandas as pd

    # Load the trained model
    model = joblib.load('path/to/your/trained_model.pkl')

    # Load test data
    test_data = pd.read_csv('path/to/your/test_data.csv')
    test_labels = test_data['label']  # Assuming the label column is named 'label'
    test_data = test_data.drop(columns=['label'])  # Drop the label column for predictions

    # Evaluate the model
    accuracy, report = evaluate_model(model, test_data, test_labels)

    print(f"Model Accuracy: {accuracy}")
    print("Classification Report:")
    print(report)