#!/usr/bin/env python

import csv
from datetime import date
from pathlib import Path
from sys import stderr

SRC_PATH = Path('data/compiled/salaries.csv')
DEST_PATH = Path('data/wrangled/salaries.csv')



def fix_date(datestr):
    """
    datestr (string): is a date in MM/DD/YY format
    Returns: a string properly formatted as iso8601, i.e.  YYYY-MM-DD
    """
    m, d, y = datestr.split("/")
    # return '-'.join([y,
    #                  m.rjust(2, '0'),
    #                  d.rjust(2, '0'),])

def wrangle_data(srcpath):
    data = []
    return data


def main():
    DEST_PATH.parent.mkdir(exist_ok=True, parents=True)
    with open(DEST_PATH, 'w') as w:
        outs = csv.DictWriter(w, fieldnames=OUTPUT_HEADERS)
        outs.writeheader()
        data = sorted(wrangle_data(SRC_PATH), key=lambda d: d['last_name'])
        outs.writerows(data)

    stderr.write(f"Wrangled {len(data)} rows from {SRC_PATH}\n")
    stderr.write(f"Wrote to {DEST_PATH}\n")


if __name__ == '__main__':
    main()
