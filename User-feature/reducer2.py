import sys

currentKey = None
sum = 0.0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    parts = line.split("\t")

    # print(parts)

    if(len(parts) != 3):
        continue

    user, item, val = parts
    key = user + "\t" + item

    try:
        numericVal = float(val)
    except:
        print("Exception")

    if currentKey is not None and currentKey != key:
        print("%s\t%f" % (currentKey, sum))
        sum = 0.0
    currentKey = key
    sum += numericVal

if currentKey is not None:
    print("%s\t%f" % (currentKey, sum))

