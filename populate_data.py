import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Project_Third.settings')

import django

django.setup()

from user.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5):
    for entry in range(N):
        fakeFirstName = fakegen.first_name()
        fakeLastName = fakegen.last_name()
        fakeEmail = fakegen.email()

        user = User.objects.get_or_create(firstName=fakeFirstName, lastName=fakeLastName, email=fakeEmail)[0]


if __name__ == '__main__':
    populate(20)
    print("Populating complete!")