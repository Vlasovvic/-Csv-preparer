import csv
import json


class IterObj:
    Series_reference: str
    Period: str
    Data_value: float
    Suppressed: chr
    STATUS: chr
    UNITS: str
    Magnitude: int
    Subject: str
    Groups: str
    Series_title_1: str
    Series_title_2: str
    Series_title_3: str
    Series_title_4: str
    Series_title_5: str


class CsvFileHelper:

    def CsvFileHelper_COLUMNS_FULL(self, row) -> IterObj:
        result = IterObj()
        if row[0] is not None:
            result.Series_reference = str(row[0])
        if row[1] is not None:
            result.Period = str(row[1])
        if row[2] is not None:
            result.Data_value = float(row[2])
        if row[3] is not None:
            result.Suppressed = chr(row[3])
        if row[4] is not None:
            result.STATUS = chr(row[4])
        if row[5] is not None:
            result.UNITS = str(row[5])
        if row[6] is not None:
            result.Magnitude = int(row[6])
        if row[7] is not None:
            result.Subject = str(row[7])
        if row[8] is not None:
            result.Groups = str(row[8])
        if row[9] is not None:
            result.Series_title_1 = str(row[9])
        if row[10] is not None:
            result.Series_title_2 = str(row[10])
        if row[11] is not None:
            result.Series_title_3 = str(row[11])
        if row[12] is not None:
            result.Series_title_4 = str(row[12])
        if row[13] is not None:
            result.Series_title_5 = str(row[13])
        return result


class HeadersError(Exception):
    def __str__(self):
        return "Csv file have different headers"


class MoreColumnsThenExpected(Exception):
    def __str__(self):
        return "Csv file have more columns then expected"


class LessColumnsThenExpected(Exception):
    def __str__(self):
        return "Csv file have less columns then expected"


def csv_reader(path_to_csv):
    with open(path_to_csv, newline='') as file:
        csv_file = csv.reader(file, delimiter=' ', quotechar='|')
    return csv_file


def check_exceptions(headers, actual_headers):
    for header, actual_header in zip(headers, actual_headers):
        if header != actual_header:
            raise HeadersError
    if len(headers) < len(actual_headers):
        raise MoreColumnsThenExpected
    if len(headers) > len(actual_headers):
        raise LessColumnsThenExpected


def job(config):
    csv_dict = []
    result = {
        "csv_file": None,
        "headers": None,
        "metainformation": None
    }
    iter_obj: IterObj
    actual_colums = []
    path_to_csv = config['path_to_csv']
    headers = config['headers']
    metainformation = config['metainformation']
    with open(path_to_csv, newline='', encoding='UTF-8') as file:
        csv_file = csv.reader(file, quotechar='|')
        for row in csv_file.__iter__():
            actual_colums = row
            # print(headers)
            check_exceptions(headers, row)
            break

        for row in csv_file.__iter__():
            elem = {
                headers[0]: row[0],
                headers[1]: row[1],
                headers[2]: row[2],
                headers[3]: row[3],
                headers[4]: row[4],
                headers[5]: row[5],
                headers[6]: row[6],
                headers[7]: row[7],
                headers[8]: row[8],
                headers[9]: row[9],
                headers[10]: row[10],
                headers[11]: row[11],
                headers[12]: row[12],
                headers[13]: row[13],

            }
            csv_dict.append(elem)
    result['csv_file'] = csv_dict
    result['headers'] = actual_colums
    result['metainformation'] = metainformation

    print(result)
    return result


if __name__ == '__main__':
    with open('config.json') as file:
        config = json.load(file)
    job(config)
