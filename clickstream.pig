clicks = LOAD 'clickstream.csv' USING PigStorage(',')
          AS (uid: chararray, pid: chararray, action: chararray, timestamp: chararray);

products = LOAD 'products.csv' USING PigStorage(',')
          AS (pid: chararray, price: float, category: chararray);

purchases = FILTER clicks BY LOWER(action) == 'purchase';

views = FILTER clicks BY LOWER(action) == 'view';
view_grouped = GROUP views BY pid;
view_counts = FOREACH view_grouped GENERATE group AS pid, COUNT(views) AS view_count;

joined = JOIN view_counts BY pid, products BY pid;

sorted_views = ORDER joined BY view_count DESC;

STORE purchases INTO 'purOP' USING PigStorage(',');
STORE sorted_views INTO 'viewsOP' USING PigStorage(',');