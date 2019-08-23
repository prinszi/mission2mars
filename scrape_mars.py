from bs4 import BeautifulSoup as bs
from splinter import Browser
import requests
import pandas as pd
from pprint import pprint

def scrape():

    mars_data = {}
    mars_data["mars_news"] = marsNews()
    mars_data["mars_featured_image"] = marsFeaturedImage()
    mars_data["mars_weather"] = marsWeather()
    mars_data["mars_facts"] = marsFacts()
    mars_data["mars_hemispheres"] = marsHemisphereImageURLs()

    return mars_data

