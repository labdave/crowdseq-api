"""

"""
import pandas as pd
import json
from django.core.management.base import BaseCommand
from Aries.storage import StorageFile

from api.models import Variants


class Command(BaseCommand):
    """

    See https://docs.djangoproject.com/en/1.11/howto/custom-management-commands/
    """
    help = 'Matches a gene and amino acid change to the chrom-pos-ref-alt from an Excel file.'

    def add_arguments(self, parser):
        """Positional arguments

        See https://docs.python.org/3/library/argparse.html for more details about add_argument
        """
        parser.add_argument('file', type=str, help="local excel file with gene and aa change data")

    def handle(self, *args, **options):

        filename = options['file']

        if StorageFile(filename).exists():
            new_file = filename.replace('.xlsx', '_matched.xlsx')
            xls = pd.ExcelFile(filename, engine='openpyxl')
            sheet_1 = xls.sheet_names[0]
            df = pd.read_excel(xls, sheet_name=sheet_1)
            data = df.to_dict('records')
            for row in data:
                variant_list = Variants.objects.filter(gene__approved_symbol=row['gene'], aa_transcript_variants__amino_acid__short_name__icontains=row['feature'])
                if variant_list:
                    cpra = ', '.join(v.alt_chrom_pos_ref_alt for v in variant_list)
                    row['chrom_pos_ref_alt'] = cpra
            df = pd.DataFrame(data)
            df.to_excel(new_file, index=False)
