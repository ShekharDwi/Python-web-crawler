# Python-web-crawler

**Simple Python Search Spider, Page Ranker, and Visualizer**

By: Shekhar Dwivedi


This Project is a set of programs/modules that emulate some of the functions of a search engine. They
store their data in a SQLITE3 database named 'spider.sqlite'. This file can be removed at any time to
restart the process.
Install the SQLite browser to view and modify the databases from:
http://sqlitebrowser.org/
This program crawls a web site and pulls a series of pages into the database, recording the links
between pages. To start up the program launch the driver by typing following command:  C:\system32/project>python3 driver.py


##       Modules        ##

1. Web Crawler / Spider:

Crawlers are used to collect links from the web.
In the sample run below, we told it to crawl a website and retrieve fifty pages. If you restart the
program again and tell it to crawl more pages, it will not re-crawl any pages already in the database.
Upon restart it goes to a random non-crawled page and starts there. So each successive run of
spider.py is additive.
You can have multiple starting points in the same database - within the program these are called
"webs". The spider chooses randomly amongst all non-visited links across all the webs.

Crawling or collecting links is a slow process and it will take a lot of time if we let it wander between
different sites till it finds sufficient links between the sites. So in my project the crawler is restricted to
crawl in the same domain it started with to make things faster and easily accessible.
Like in the example run we choose a wikipedia page on world war II, Hence our crawler will only
consider the pages/links within the wikipedia.org domain


2. Data dump:

If you want to dump the contents of the spider.sqlite file, you can run spdump.py as follows:

C:\system32/project>python3 spdump.py

This shows the number of incoming links, the old page rank, the new pagerank, the id of the page, and
the url of the page. The spdump.py program only shows pages that have at least one incoming link to
them.

3. Pagerank:

Once you have a few pages in the database, you can run Page Rank on the pages using the sprank.py
program. You simply tell it how many Page Rank iterations to run.
You can dump the database again to see that page rank has been updated:
C:\system32/project>python3 rankalgo.py

You can run rankalgo.py as many times as you like and it will simply refine the page rank the more
times you run it. You can even run sprank.py a few times and then go spider a few more pages sith
spider.py and then run ranker to converge the page ranks.
For each iteration of the page rank algorithm it prints the average change per page of the page rank.
The network initially is quite unbalanced and so the individual page ranks are changing wildly. But in
a few short iterations, the page rank converges. You should run prank.py long enough that the page
ranks converge.


4. JSON Export:


If you want to visualize the current top pages in terms of page rank, run spjson.py to write the pages
out in JSON format to be viewed in a web browser.
C:\system32/project>python3 jsonexport.py


5. Visualization

You can view this data by opening the file force.html in your web browser. This shows an automatic
layout of the nodes and links. You can click and drag any node and you can also double click on a
node to find the URL that is represented by the node.
C:\system32/project>force.html

This visualization is provided using the force layout from:
http://mbostock.github.com/d3/


## Useful utilities ##

1. Delete database
This option deletes the spider.sqlite file
Use this option when you want to start a new crawler run on a different site.

2.Rank reset
If you want to restart the Page Rank calculations without re-spidering the web pages, you can use this
option
All pages ranks will be set to 1.0

3.Exit
To exit the program interface
