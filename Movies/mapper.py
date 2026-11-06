import sys
import csv

for line in sys.stdin:
    line = line.strip()
    if not line or line.startswith("userId"):
        continue

    try:
        fields = next(csv.reader([line]))
        movieId = fields[1]
        tag = fields[2]
        if movieId and tag:
            print("%s\t%s" % (movieId, tag))
    except:
        continue

