#!/usr/bin/env python

import csv
from pathlib import Path
import re
from sys import stderr

SRC_PATH = Path('data/collected/salaries-2020-04-03.csv')
HEADERS_PATH = Path('data/archived/compiled-header-map.csv')
DEST_PATH = Path('data/compiled/salaries.csv')

def load_header_map():
    return {h['original_name']: h['compiled_name'] for h in csv.DictReader(open(HEADERS_PATH))}

def load_data(srcpath):
    """returns raw data with a publish_date column"""
    data = []
    pubdate = re.search(r'\d{4}-\d{2}-\d{2}', srcpath.stem).group()
    with open(srcpath) as src:
        for row in csv.DictReader(open(srcpath)):
            row['publish_date'] = pubdate
            data.append(row)
    return data


def process_data(records):
    hmap = load_header_map()
    data = []
    for row in records:
        d = {}
        for oldhead in row.keys():
            h = hmap[oldhead] if hmap.get(oldhead) else oldhead
            d[h] = row[oldhead].strip()
        data.append(d)
    return data

def main():
    srcpath = SRC_PATH
    data = load_data(srcpath)
    data = process_data(data)

    DEST_PATH.parent.mkdir(exist_ok=True, parents=True)
    with open(DEST_PATH, 'w') as w:
        outs = csv.DictWriter(w, fieldnames=data[0].keys())
        outs.writeheader()
        outs.writerows(data)

        stderr.write(f"Compiled {len(data)} rows from {srcpath}\n")
        stderr.write(f"Wrote to {DEST_PATH}\n")

if __name__ == '__main__':
    main()
