# parse_httpd_log

Python version : 3.6.0

Usage:

python parse.py 

Count the total number of HTTP requests recorded by this access logfile
[(254322,)]
 
Find the top-10 (host) hosts makes most requests from 2017-06-10 00:00:00 to 2017-06-19 23:59:59, inclusively
[('85.25.236.93', 345),
 ('204.12.238.106', 228),
 ('178.115.130.191', 180),
 ('62.46.92.42', 145),
 ('213.147.163.125', 106),
 ('216.218.222.12', 99),
 ('195.16.224.228', 92),
 ('109.163.234.5', 88),
 ('145.244.10.2', 87),
 ('193.187.235.17', 83)]
 
Find out the country with most requests originating from (according the source IP)
[('205.167.170.15', 'US', 32998),
 ('158.64.79.7', 'LU', 10940),
 ('158.64.79.8', 'LU', 10611),
 ('85.10.113.129', 'LU', 4435),
 ('85.25.236.93', 'DE', 1408),
 ('143.161.248.25', 'AT', 1067),
 ('188.138.56.91', 'DE', 807),
 ('200.137.2.52', 'BR', 747),
 ('52.22.118.215', 'US', 732),
 ('82.80.230.228', 'IL', 724)]
