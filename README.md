Byrd
====

Bromwich (Bromwich et al, 2013, "Central West Antarctica among
the most rapidly warming regions on Earth", Nature Geoscience 6,
139--145 (2013), doi:10.1038/ngeo1671) has published a
reconstructed temperature record for Byrd station (-80-120). It
is much more complete than the records in GHCN-M.

The text file for the recontructed record is here:
http://polarmet.osu.edu/Byrd_recon/byrd_temp_recon_monthly_revised.txt

The program `dat.py` converts the `byrd.txt` file to GHCN-M v3 format.

The `byrd.txt` file needs to be extracted from the
`GISTEMPv3_sources.tar.gz` file (at the location
`GISTEMP_sources/STEP0/input_files/byrd.txt`) published by NASA GISS.

## Station Identifiers

This version of the Byrd record is assigned a station identifier of:

    79889125000

("798" is a fake country in the Antarctic 7xx range used by
GHCN-M; "89125" is Byrd's WMO identifier)
