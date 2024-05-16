# import_inspection_data.py
import pandas as pd
from datetime import datetime
from django.core.management.base import BaseCommand
from ...models import InspectionApplication, Inspector

class Command(BaseCommand):
    help = 'Import data from Excel file to InspectionApplication model'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the Excel file')
        parser.add_argument('sheet_name', type=str, help='Name of the sheet to read data from')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        sheet_name = kwargs['sheet_name']
        df = pd.read_excel(file_path, sheet_name=sheet_name)

        inspection_applications = []

        for index, row in df.iterrows():
            date_obj = self.convert_date(row.get("date"))
            inspection_date_obj = self.convert_date(row.get("inspection_date"))
            date_collected_obj = self.convert_date(row.get("date_collected"))

            # contractor = self.get_inspector_by_licence_no(row.get("Contractor_number"))
            # inspectors = self.get_inspectors_by_licence_nos(row.get("Contractor_number"))
            # assistants = self.get_inspectors_by_licence_nos(row.get("Contractor_number"))
            # print(inspectors, assistants,  contractor)

            inspection_app = InspectionApplication(
                date=date_obj,
                app_no=row.get("app_no"),
                receipt_no=row.get("receipt_no"),
                amount=row.get("amount"),
                cert_no=row.get("cert_no"),
                name=row.get("name"),
                area=row.get("area"),
                zone=row.get("zone"),
                # contactor=contractor,
                lights=row.get("lights"),
                sockets=row.get("sockets"),
                switches=row.get("switches"),
                BC=row.get("BC"),
                LE=row.get("LE"),
                LN=row.get("LN"),
                EN=row.get("EN"),
                AE=row.get("AE"),
                ins_type=row.get("ins_type"),
                mA=row.get("mA"),
                sub_circuit=row.get("sub_circuit"),
                main_rating=row.get("main_rating"),
                inspection_date=inspection_date_obj,
                collected_by=row.get("collected_by"),
                date_collected=date_collected_obj,
            )

            # Save the instance to the list
            inspection_applications.append(inspection_app)

        # Bulk create the inspection applications
        InspectionApplication.objects.bulk_create(inspection_applications)

        # Add many-to-many relationships
        # for index, row in df.iterrows():
        #     inspection_app = inspection_applications[index]
        #     inspectors = self.get_inspectors_by_licence_nos(row.get("Contractor_number"))
        #     assistants = self.get_inspectors_by_licence_nos(row.get("Contractor_number"))
        #     inspection_app.inspector.set(inspectors)
        #     inspection_app.assistant.set(assistants)

        # self.stdout.write(self.style.SUCCESS('Data imported successfully'))

    def convert_date(self, date_str):
        if not date_str:
            return None
        for fmt in ('%d-%b-%y', '%B %d, %Y'):
            try:
                return datetime.strptime(date_str, fmt).date()
            except ValueError:
                continue
        return None

    # def get_inspector_by_licence_no(self, licence_no):
    #     if licence_no:
    #         inspector = Inspector.objects.get_or_create(licence_no=licence_no)
    #         return inspector
    #     return None

    # def get_inspectors_by_licence_nos(self, licence_nos):
    #     if licence_nos:
    #         licence_nos_list = licence_nos
    #         inspectors = Inspector.objects.filter(licence_no__in=licence_nos_list)
    #         return inspectors
    #     return []
