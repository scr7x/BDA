import sys
import csv

movies = {}

with open("movies.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        movies[row[0]] = row[1]

currentMovie = None
tags = []

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    movieId, tag = line.split("\t", 1)
    if currentMovie == movieId:
        tags.append(tag)
    else:
        if currentMovie:
            title = movies.get(currentMovie, currentMovie)
            print("%s\t%s" % (title, ",".join(tags)))
        currentMovie = movieId
        tags = [tag]

if currentMovie:
        title = movies.get(currentMovie, currentMovie)
