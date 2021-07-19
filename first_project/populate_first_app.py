import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()

import random
from first_app.models import AccessRecord,Topic,Webpage
from faker import Faker

fakegen = Faker()
topics =  ['Search','Social','Marketplace','News','Sports','Games','Education','Cooking']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):

        top = add_topic()

        #fake Date
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        #fake Webpage
        webpg = Webpage.objects.get_or_create(topic=top,name=fake_name,url=fake_url)[0]

        #fake AccessRecord
        ac_rec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

if __name__ ==  "__main__":
    print('populating.......')
    populate(20)
    print("population complete")
