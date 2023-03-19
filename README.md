## Apartment-Data-Scraper-and-Price-Predictor  

This Python script scrapes apartment data from the Immowelt.de website and helps users find an apartment based on desired area and number of rooms. If no matching apartments are found, the script predicts the price of a desired apartment in a desired city using machine learning technology based on data from the website. All data is stored and retrieved from a MongoDB database.


**Prerequisites**

Python 3.x
Required libraries: BeautifulSoup, requests,  scikit-learn, pymongo

**Installation**

Clone or download the repository to your local machine.

Install the required libraries using pip:
pip install beautifulsoup4 requests  scikit-learn pymongo

**Usage**

Run the script immowelt_scraper.py in a Python environment.
The script will prompt the user to enter the desired city, area, and number of rooms for the apartment.
The script will then scrape the data from Immowelt.de and find any matching apartments.
If matching apartments are found, the script will display the apartment details, including the price, area, and number of rooms. The data will also be saved to a MongoDB database.
If no matching apartments are found, the script will use machine learning technology to predict the price of a desired apartment in the desired city.
The script will display the predicted price for the desired apartment. The data will also be saved to a MongoDB database.


**Authors**

Morteza Baniadam

