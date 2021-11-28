# COVID 19 Computer Vision Project
---
## Project Description:
A web application that will take an x-ray scan and diagnose whether or not the subject of the x-ray scan has COVID 19. 
Dataset provided from https://www.kaggle.com/tawsifurrahman/covid19-radiography-database.

## Running the Project:
Download:
* static
* templates
* app.py
* model_V10.h5
* requirements.txt 

Install the dependencies in requirements.txt (ex. `conda install --file requirements.txt`) and run app.py.  
Navigate to your http://127.0.0.1:5000/ to access the web application.   
To use the model, take an image from the Kaggle link or one of the random ones from the 'Samples' page, upload it, and hit submit. 

## Repository Organization:
1. Deliverables, Model Creation
  * Deliverables detailing my progression throughout the project submitted to the MAIS 202 Organizers
  * Jupyter Notebook file used to create the model
2. static/
  * CSS and Image files for the landing page
3. templates/
  * HTML templates for landing page
4. app.py
  * Python script to instantiate the Flask server
5. model_V10.h5
  * The 10th iteration of the trained weights of the model
6. requirements.txt
  * Requirements needed to run the web application

## Final Results:
![alt text](https://github.com/Vermillion-Chen/Covid19Predictor/blob/main/static/images/Final%20Results.png?raw=true)
