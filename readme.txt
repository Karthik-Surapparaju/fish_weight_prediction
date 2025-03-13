# Fish Weight Prediction Model

## Project Overview
This project creates a machine learning model to predict fish weights based on measurements from the [Fish Market Dataset]. It implements a regression model to accurately estimate fish weight given various physical measurements.

## Problem Statement
We are addressing a regression problem to predict the weight of fish based on their physical measurements (lengths, height, and width). This prediction can be useful for fish market operations, fishing industries, and marine biology research.

## Model Details
- **Model Type**: Random Forest Regressor
- **Features Used**: 
  - Length1 (Vertical Length)
  - Length2 (Diagonal Length) 
  - Length3 (Cross Length)
  - Height
  - Width
- **Target Variable**: Weight (in grams)
- **Preprocessing**: Standard scaling of features

## Project Structure
- `app.py`: Flask application that serves the model
- `fish_model.pkl`: Serialized trained model
- `scaler.pkl`: Serialized scaler for feature normalization
- `templates/index.html`: Frontend HTML interface
- `static/style.css`:
- `Fish.csv`: Dataset file

## How to Run Locally
1. Clone this repository
2. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the Flask application:
   ```
   python app.py
   ```
4. Open a web browser and navigate to `http://localhost:5000`

## Deployment
The model is deployed on Heroku and can be accessed at [Heroku App URL].

## How to Use
1. Enter the fish measurements (lengths, height, and width) in the provided form
2. Click "Predict Weight"
3. The predicted weight of the fish will be displayed below the form

## Model Performance
- Root Mean Squared Error (RMSE): Approximately XX grams
- R² Score: Approximately XX%

## Future Improvements
- Experiment with different regression algorithms
- Collect more data for better model training
- Add visualization of prediction results
- Implement model retraining functionality

## License
This project is licensed under the MIT License - see the LICENSE file for details.
