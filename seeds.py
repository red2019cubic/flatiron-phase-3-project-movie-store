from models import Actor, Movie
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

import csv

engine = create_engine("sqlite:///movie_store.db")
Session = sessionmaker(bind=engine)
session = Session()

# For generating Fake data: https://faker.readthedocs.io/en/master/providers.html
# from faker import Faker

session.query(Movie).delete()
session.query(Actor).delete()

# For working with an API and retrieving json data
import requests
import json
import random
with open('movies.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        print(row)