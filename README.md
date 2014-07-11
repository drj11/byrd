Byrd
====

Bromwich (Bromwich et al, 2013, "Central West Antarctica among
the most rapidly warming regions on Earth", Nature Geoscience 6,
139--145 (2013), doi:10.1038/ngeo1671) has published a
reconstructed temperature record for Byrd station (-80-120). It
is much more complete than the records in GHCN-M.

The text file for the recontructed record is here:
http://polarmet.osu.edu/Byrd_recon/byrd_temp_recon_monthly_revised.txt

Run the program:

    ./dat.py

This downloads the record (from the above URL) and converts it
to GHCN-M v3 format, writing its output to `byrd.out`.

Alternatively, if you have already downloaded the text file, you
can convert that:

    ./dat.py byrd.txt

## Station Identifiers

This version of the Byrd record is assigned a station identifier of:

    79889324000

"798" is a fake country in the Antarctic 7xx range used by GHCN-M.

"89324" is Byrd's WMO identifier (in a recent WMO Volume A)
