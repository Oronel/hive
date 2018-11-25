import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hive.settings')
import django
django.setup()


import random
from faker import Faker
from first_app.models import User, Feed


fakegen = Faker()

def create_user():
    username  = fakegen.user_name()
    email     = fakegen.email()
    password  = fakegen.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)
    bio       = fakegen.text(max_nb_chars=140)
    fullName  = fakegen.name()

    return User.objects.get_or_create(user_name=username, email=email, password=password, full_name= fullName, bio= bio)[0]


def create_feed(user):
    text  = fakegen.text(max_nb_chars=140)
    date  = fakegen.date()
    like  = fakegen.random_digit_not_null()


    return Feed.objects.get_or_create(text=text, user=user, date=date, like= like)[0]


def populate():
    users = []
    for user in range(20):
        user = create_user()
        for tweet in range(10):
            tweet = create_feed(user)


if __name__ == '__main__':
  print('Starting to populate...')
  populate()
  print('Finished populating!')