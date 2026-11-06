from pyspark import SparkContext
from pyspark.sql import SQLContext, Row

sc = SparkContext()
sqlContext = SQLContext(sc)

rdd = sc.textFile("path")

cleaned_rdd = rdd.map(lambda line: ''.join(ch.lower() if ch.isalnum() or ch.isspace() else ' ' for ch in line))

words_rdd = cleaned_rdd.flatMap(lambda w: w.split())

stopWords = set(["the", "is","and", "to", "of", "in", "for", "a", "for", "on", "with", "this", "that", "it", "as", "and","so", "if", "has", "had", "but", "so", "if", "from", "be"])

filtered_rdd = words_rdd.filter(lambda w: w not in stopWords and w != '')
row_rdd = filtered_rdd.map(lambda w: Row(word=w))

df = sqlContext.createDataFrame(row_rdd)

df = df.groupBy("word").count()
df = df.sort(df["count"].desc())

top_n = 10
results = df.take(top_n)

print("Word Count")
for w, c in results:
    print("%s\t%s" %(w,c))