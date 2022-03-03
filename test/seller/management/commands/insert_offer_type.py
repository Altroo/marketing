import sys
from django.core.management import BaseCommand
from seller.models import OfferType
from csv import reader
from os import path


class Insert:
    parent_file_dir = path.abspath(path.join(path.dirname(__file__), "../../.."))

    def insert(self):
        with open(self.parent_file_dir + '/csv_data/offer_type.csv', 'r+', encoding='UTF8') as f:
            csv_reader = reader(f, delimiter=',')
            for row in csv_reader:
                OfferType.objects.create(name_offer=row[0])


class Command(BaseCommand):
    help = 'Insert Offer type'

    def handle(self, *args, **options):
        sys.stdout.write(f'Start processing Offer type.\n')
        self.insert()
        sys.stdout.write('\n')

    @staticmethod
    def insert():
        inserter = Insert()
        try:
            inserter.insert()
        except Exception as e:
            sys.stdout.write('{}.\n'.format(e))
