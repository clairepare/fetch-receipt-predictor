# Fetch Receipt Predictor

## Description
The Fetch Receipt Predictor is a web application that uses a polynomial regression model to predict the number of receipts generated for a given month. The application is packaged in a Docker container for easy deployment.

# Method 1: Using Docker

## Prerequisites
Ensure that you have Docker installed on your system. If not, you can download and install Docker from [here](https://www.docker.com/get-started).

## How to Run the Application

### **Step 1: Pull the Docker Image**
Pull the Docker image from Docker Hub using the following command:
```sh
docker pull clairempare/fetch-receipt-predictor:v1.0
```
### **Step 2: Run the Docker Container**
After the image has been pulled successfully, you can run the container using the following command:

```sh
docker run -p 4000:80 clairempare/fetch-receipt-predictor:v1.0
```
This command maps port 4000 on your host machine to port 80 on the Docker container.

### **Step 3: Access the Application**
Once the container is running, you can access the application by opening a web browser and navigating to:

```sh
http://localhost:4000
```
You should see the Fetch Receipt Predictor application interface, and you can interact with it as needed.

# Method 2: Running the Project Locally

## Prerequisistes:
Ensure you have the following installed on your local machine:

- Python 3.9+
- Pip (Python Package Installer)

### Step 1: Clone the repository:
```sh
git clone https://github.com/clairepare/fetch-receipt-predictor.git
cd fetch-receipt-predictor
```
### Step 2: Install Dependencies:
Install the necessary Python packages via `pip`
```sh
pip install -r requirements.txt
```
### Step 3: Run the Application:
Start the FastAPI application:
```sh
uvicorn main:app --reload
```
The application should be running on `http://127.0.0.1:4000/`.
You should see the Fetch Receipt Predictor application interface, and you can interact with it as needed.
