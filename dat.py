#!/usr/bin/env python3

import re
import sys

MISSING = -9999.0

def ghcnm_write(id, values, out):
    """
    `id` is the 11 character identifier.
    `values` is an iterator of (year, data) pairs.
    `out` is a writable file to which data in GHCN-M format is
    written.
    """

    def format_single(v):
        if v == MISSING:
            return "-9999   "
        # Make up a source flag of "f" for foundation.
        return "{:5.0f}  f".format(v*100)

    FORMAT = "{}{}TAVG" + ("{:8s}"*12) + "\n"
    ALL_MISSING = [MISSING]*12
    for year, data in values: 
        if data == ALL_MISSING:
            continue
        data = tuple(format_single(d) for d in data)
        formatted_row = FORMAT.format(*((id, year) + data))
        out.write(formatted_row)


def years_iter(inp):    
    def convert_value(s):
        x = float(s)
        if x == -999.0:
            return MISSING
        return x

    for line in inp:
        if not re.match(r'^\d{4}', line):
            continue
        year = int(line[:4])
        monthly = [convert_value(line[b:b+6])
          for b in range(5, 89, 7)]
        yield (year, monthly)

def main():
    with open('byrd.txt') as byrd:
        # Country Code 798 which is a new fake country in the
        # 7xx series that GHCN-M uses for Antarctica.
        # 89125 is the WMO identifier for Byrd, as used in the
        # GHCN-M .inv file.
        ghcnm_write('79889125000', years_iter(byrd), sys.stdout)

if __name__ == '__main__':
    main()
