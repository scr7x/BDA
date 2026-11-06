import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    date, temp = line.split(',')

    temp = int(temp)

    if temp > 30:
        msg = "Hot"
    elif temp < 15:
        msg = "Cold"
    else:
        msg = "Happy"

    print("%s\t%s" % (date, msg))