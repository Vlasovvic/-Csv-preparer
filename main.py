import csv
import json


class HeadersError(Exception):
    def __str__(self):
        return "Csv file have different headers"


class MoreColumnsThenExpected(Exception):
    def __str__(self):
        return "Csv file have more columns then expected"


class LessColumnsThenExpected(Exception):
    def __str__(self):
        return "Csv file have less columns then expected"


def column_Gen(row):
    columns = row
    yield columns


def dict_Gen(row, headers):
    elem = {}
    for iter in zip(row, headers):
        elem[f'{iter[0]}'] = iter[1]
    yield elem


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
    actual_headers = []
    path_to_csv = config['path_to_csv']
    headers = config['headers']
    metainformation = config['metainformation']
    with open(path_to_csv, newline='', encoding='UTF-8') as file:
        csv_file = csv.reader(file, quotechar='|')
        for index, row in enumerate(csv_file.__iter__()):
            if index == 0:
                if row == headers:
                    actual_headers = next(column_Gen(row))
                else:
                    check_exceptions(headers, row)
            else:
                row_buffer = dict_Gen(headers, row)
                csv_dict.append(next(row_buffer))
    result['csv_file'] = csv_dict
    result['headers'] = actual_headers
    result['metainformation'] = metainformation
    print(result)
    return result


if __name__ == '__main__':
    with open('config.json') as file:
        config = json.load(file)
    job(config)
