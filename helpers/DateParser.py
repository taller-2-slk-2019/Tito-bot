from dateutil.parser import *


class DateParser:

    @staticmethod
    def parse(date):
        date_obj = parse(date)
        return date_obj.strftime("%d/%m/%Y")
