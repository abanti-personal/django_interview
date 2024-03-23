import requests
from django.core.management.base import BaseCommand
from myapp.models import User, Address, Company


class Command(BaseCommand):
    help = 'Add user details from the API'

    def handle(self, *args, **kwargs):
        url = 'https://jsonplaceholder.typicode.com/users'
        response = requests.get(url)
        data = response.json()

        for user_data in data:
            address_data = user_data['address']
            address = Address.objects.create(
                street=address_data['street'],
                suite=address_data['suite'],
                city=address_data['city'],
                zipcode=address_data['zipcode']
            )

            company_data = user_data['company']
            company = Company.objects.create(
                name=company_data['name'],
                catch_phrase=company_data['catchPhrase'],
                bs=company_data['bs']
            )

            User.objects.create(
                name=user_data['name'],
                username=user_data['username'],
                email=user_data['email'],
                address=address,
                phone=user_data['phone'],
                website=user_data['website'],
                company=company
            )

        self.stdout.write('Users data loaded successfully.')
