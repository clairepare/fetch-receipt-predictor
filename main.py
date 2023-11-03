from fastapi import FastAPI, Request
import numpy as np
from polynomial_regression import PolynomialRegression
from metrics import mean_squared_error
from data_loader import load_data, preprocess_data
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

def main(file_path, degree=1, use_all_data_for_training=True):
    """
        The main method takes as input a file path, the degree of the polynomial regression,
        and a boolean use_all_data_for_training and is responsible for processing the data,
        training the model, and visualizing the results.
        
        Args:
            degree (int): Degree of polynomial used to fit the data.
            file_path (string): a string representing the file path
            use_all_data_for_training (boolean): whether all the data should be used for training
        Returns:
            either a String with the mean squared error or the predicted values
        """
    #calls load_data, preprocess_data in data_loader to load the data
    df = load_data(file_path)
    train_data, test_data = preprocess_data(df)

    #separates the two parts of the data into features (x) and targets (y)
    train_features = np.array(train_data['Month_Number'])
    train_targets = np.array(train_data['Receipt_Count'])

    #if we've split into train and test this shouldn't be empty
    test_features = np.array(test_data['Month_Number'])
    test_targets = np.array(test_data['Receipt_Count'])

    #initializes a new regression model with degree specified and fits it according to the
    #training data
    model = PolynomialRegression(degree)
    model.fit(train_features, train_targets)

    predictions = 0

    if not use_all_data_for_training:
        #test the model using the testing data and return the mean squared error
        predictions = model.predict(test_features)
        mse = mean_squared_error(predictions, test_targets)
        return f"Mean Squared Error on Testing Data: {mse}"
    else:
        #generate a new range of features (the months of 2022)
        test_features = np.array(range(len(train_data) + 1, len(train_data) + 13))  # Month numbers for 2022
        #calls model.predict on the new features to predict the values for 2022
        predictions = model.predict(test_features)
        #plots and saves the data to visualize
        model.visualize_full(degree, train_features, train_targets, test_features, test_targets, predictions)
        return predictions

app.mount("/static", StaticFiles(directory="static"), name="static")

#homepage, displays initial data plot and a prompt to call the model
@app.get("/")
def read_root():
    with open("templates/index.html", "r") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)

templates = Jinja2Templates(directory="templates")

#the result page, runs main() and grabs the predictions to display in a table
@app.get("/run_model", response_class=HTMLResponse)
def run_model(request: Request):
    predictions = main('data_daily.csv', degree=1, use_all_data_for_training=True)
    #results in the format: [{"Month": month, "Value": value}, ...]
    results = [{"Month": month, "Value": value} for month, value in enumerate(predictions, start=13)]
    image_path = "/static/output.png"
    return templates.TemplateResponse("results.html", {"request": request, "results": results, "image_path": image_path})
    #return templates.TemplateResponse("result.html", {"request": request, "results": results})