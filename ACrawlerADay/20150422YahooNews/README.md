ROOT_URL = https://tw.news.yahoo.com/politics/archive/
START = 2015/04/22 1000
DUE = 2015/04/23 1000
DATA_FORMAT:

(1) posts

[pk] id (請自定規則 or hash)
title
text
postAt (Date)
monitorAt (Date)
url
(2) related_posts

[fk] p1id
[fk] p2id
monitorAt (Date)

