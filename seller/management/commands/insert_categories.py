import sys
from django.core.management import BaseCommand
from seller.models import Categories
from csv import reader
from os import path


class Insert:
    parent_file_dir = path.abspath(path.join(path.dirname(__file__), "../../.."))

    def insert(self):
        with open(self.parent_file_dir + '/csv_data/categories.csv', 'r+', encoding='UTF8') as f:
            csv_reader = reader(f, delimiter=',')
            for row in csv_reader:
                Categories.objects.create(name_category=row[0])


class Command(BaseCommand):
    help = 'Insert Categories'

    def handle(self, *args, **options):
        sys.stdout.write(f'Start processing Categories.\n')
        self.insert()
        sys.stdout.write('\n')

    @staticmethod
    def insert():
        inserter = Insert()
        try:
            inserter.insert()
        except Exception as e:
            sys.stdout.write('{}.\n'.format(e))
