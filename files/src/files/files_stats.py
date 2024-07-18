import datetime
import os

import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
pd.set_option('display.colheader_justify', 'center')
pd.set_option('display.precision', 2)


def convert_bytes(amount: float) -> str:
    converter = {0: 'Б', 1: 'КБ', 2: 'МБ', 3: 'ГБ', 4: 'ТБ'}
    count = 0
    while amount > 1024:
        count += 1
        amount /= 1024
    return f'{round(amount, 2)} {converter.get(count)}'


def get_dir_size(path: str = '.') -> float:
    total = 0
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                total += os.path.getsize(entry)
            elif entry.is_dir():
                total += get_dir_size(entry.path)
    return total


def get_stats(path: str) -> pd.DataFrame:
    content = os.listdir(path)
    data = {'type': [], 'name': [], 'extension': [], 'Created': [], 'Space': [], 'Space bytes': []}

    for raw_name in content:
        name = os.path.join(path, raw_name)
        created = datetime.datetime.fromtimestamp(os.stat(name).st_birthtime).replace(microsecond=0)
        size, bytes_size = 0, 0
        f_type = ''
        try:
            if os.path.isdir(name):
                bytes_size = get_dir_size(name)
                size = convert_bytes(bytes_size)
                f_type = 'directory'
            elif os.path.isfile(name):
                bytes_size = os.path.getsize(name)
                size = convert_bytes(bytes_size)
                f_type = 'file'
        except Exception:
            continue
        data['Created'].append(created)
        data['name'].append(raw_name)
        data['extension'].append(os.path.splitext(name)[1])
        data['Space'].append(size)
        data['type'].append(f_type)
        data['Space bytes'].append(bytes_size)
    df = pd.DataFrame(data)
    return df
