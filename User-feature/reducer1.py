import sys

current_item = None
userRating = []
featureValue = []

def flush():
    for u, r in userRating:
        for f, v in featureValue:
            try:
                prod = float(r) * float(v)
                print("%s\t%s\t%f" % (u,f,prod))
            except:
                continue

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    parts = line.split("\t")

    if(len(parts) != 4):
        
        continue

    item, tag, x, y = parts

    if current_item is not None and item != current_item:
        flush()
        userRating[:] = []
        featureValue[:] = []

    current_item = item
    if(tag == 'R'):
        userRating.append((x,y))
    elif(tag == 'F'):
        featureValue.append((x,y))

if current_item is not None:
    flush()