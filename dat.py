#!/usr/bin/env python3

# https://docs.python.org/3.2/library/codecs.html
import codecs
import re
import sys
# https://docs.python.org/3.2/library/urllib.request.html
import urllib.request

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

def main(argv=None):
    if argv is None:
        argv = sys.argv

    # Get source as an optional argument.
    arg = argv[1:]
    if arg:
        (source,) = arg
    else:
        source = "http://polarmet.osu.edu/Byrd_recon/byrd_temp_recon_monthly_revised.txt"

    if re.match(r'^https?:', source):
        inp = urllib.request.urlopen(source)
        inp = codecs.getreader('ascii')(inp)
    else:
        inp = open(source)
    with inp as byrd, open('byrd.dat', 'w') as out:
        # See README.md for note about identifier.
        ghcnm_write('79889324000', years_iter(byrd), out)

if __name__ == '__main__':
    main()
