# Smart Transformer Health Monitoring System

A machine learning–based Smart Transformer Health Monitoring System that analyzes transformer operational parameters and predicts the health condition of the transformer using historical dataset values.

## Project Overview

This project focuses on analyzing transformer parameters such as temperature, torque, voltage, and current from a dataset to determine the operational health condition of a transformer.

The system uses machine learning techniques to detect abnormal patterns and classify the transformer status as normal or faulty.

## Technologies Used

### Backend

* Python
* Flask
* REST API

### Database

* MySQL

### Machine Learning

* GRU / Deep Learning Model
* Time Series Analysis
* Fault Prediction

### Data Processing

* Pandas
* NumPy
* Scikit-learn
* Matplotlib

## Dataset

The system uses a transformer dataset stored in CSV format containing operational parameters such as:

* Temperature
* Torque
* Voltage
* Current
* Other transformer condition parameters

These features are used to train a machine learning model for health condition prediction.

## Project Workflow

1. Load transformer dataset from CSV
2. Perform data preprocessing and feature selection
3. Train machine learning model
4. Predict transformer health condition
5. Store and visualize results

## Project Structure

smart-transformer-health-monitoring/
│
├── backend/
│   ├── app.py
│   ├── model_training.py
│   ├── prediction.py
│   └── dataset_loader.py
│
├── dataset/
│   └── transformer_data.csv
│
├── models/
│   └── trained_model.pkl
│
└── README.md

## How to Run the Project

1. Install required libraries

pip install -r requirements.txt

2. Run the backend server

python app.py

3. Train the model

python model_training.py

4. Run prediction

python prediction.py

## Features

* Transformer health condition prediction
* Dataset-based fault detection
* Machine learning model training
* REST API for prediction
* Backend architecture using Flask

## Future Enhancements

* Real-time monitoring integration
* IoT sensor integration
* Advanced deep learning models
* Cloud deployment
* Visualization dashboard

## Project Status

✔ Dataset preprocessing completed
✔ Machine learning model developed
✔ Backend API implemented

## Developed By
Laxmipriya Rout
Laxmipriya Rout
B.Tech Computer Science Engineering
