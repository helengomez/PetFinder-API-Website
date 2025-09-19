# Petfinder Flask Web Application

## Overview

This is a Flask-based web application that allows users to search for adoptable pets using the Petfinder API. 
Users can enter search criteria such as animal type, location, breed, age, and gender. 
The application fetches matching results in real-time and displays relevant information including the pet's name, type, breed, age, description, and a link to learn more.

## API - Petfinder API
https://www.petfinder.com/developers/

## How to Set Up and Run

1. **Install required packages**
   Run the following command in your terminal:

pip install flask flask-wtf requests

css
Copy
Edit

2. **Add your Petfinder API credentials**  
Create a file named `api_keys.json` in the root folder and add the following with your API key and secret key replace the contents:

```
{
  "api_key": "your_client_id_here",
  "secret_key": "your_client_secret_here"
}
```
3. **Run the application**
```
python app.py
```
4. **Access the application**

Open a web browser and go to:
http://127.0.0.1:5000

## How It Works

The user fills out a form to search for adoptable pets.

When the form is submitted, the application validates the inputs and sends a request to the Petfinder API.

Pets that meet the request are displayed on a results page with key information and external links.

