# Micro-Doppler Target Classification System

This project implements a micro-Doppler target classification system that differentiates between birds and drones based on the frequency of their wing movements. The system consists of a backend built with Flask and a frontend developed using React.

## Project Structure

- **backend/**: Contains the server-side application.
  - **app.py**: Main entry point for the backend application.
  - **requirements.txt**: Lists dependencies required for the backend.
  - **models/**: Contains the classification model implementation.
    - **classification_model.py**: Implements the model for classification.
  - **routes/**: Defines API endpoints for the backend.
    - **api.py**: Handles requests related to classification.
  - **database/**: Sets up the database connection.
    - **db_setup.py**: Defines the schema for storing classification results.

- **frontend/**: Contains the client-side application.
  - **public/**: Static files for the frontend.
    - **index.html**: Main HTML file for the application.
  - **src/**: Source files for the React application.
    - **App.js**: Main React component.
    - **components/**: Contains React components.
      - **ClassificationResult.js**: Displays classification results.
    - **services/**: API call functions.
      - **api.js**: Functions for interacting with the backend.
    - **styles/**: CSS styles for the application.
      - **App.css**: Styles for the frontend.
  - **package.json**: Configuration file for npm.

- **data/**: Contains sample data for training and testing.
  - **sample_data.csv**: Sample micro-Doppler data.

- **ml/**: Contains machine learning scripts.
  - **preprocess.py**: Functions for data preprocessing.
  - **train.py**: Code for training the classification model.
  - **evaluate.py**: Functions for evaluating the model's performance.

## Setup Instructions

1. **Backend Setup**:
   - Navigate to the `backend` directory.
   - Install the required dependencies using:
     ```
     pip install -r requirements.txt
     ```
   - Run the backend server:
     ```
     python app.py
     ```

2. **Frontend Setup**:
   - Navigate to the `frontend` directory.
   - Install the required dependencies using:
     ```
     npm install
     ```
   - Start the frontend application:
     ```
     npm start
     ```

## Usage

- Access the frontend application in your web browser at `http://localhost:3000`.
- Use the interface to upload micro-Doppler data and receive classification results indicating whether the target is a bird or a drone.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.