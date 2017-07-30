import os
import sys
import json
import sqlite3
from pprint import pprint
import time
from time import mktime
from datetime import datetime
import requests
from bs4 import BeautifulSoup


def main():

	#檢查資料檔案是否存在，存在就刪除
	if os.path.exists("./login_record.db"):
	   os.remove("./login_record.db")

	conn = sqlite3.connect('./login_record.db')

	# 創建一個Cursor:
	cursor = conn.cursor()

	# 執行一個SQL命令，建立login_record表:
	cursor.execute('create table login_record ( id integer primary key autoincrement not null, source_ip varchar(15), login_time datetime)')

	#讀取 log 檔案
	with open('./sre_test_access.log') as f:
	    content = f.readlines()

	#進行資料預處理後，加入 login_record 表裡
	for x in content:

		source_ip = x.split(" ")[0]

		login_time = x.split(" ")[3]
		login_time = login_time[1:]
		login_time = time.strptime(login_time, "%d/%b/%Y:%H:%M:%S")
		login_time = datetime.fromtimestamp(mktime(login_time))	

		cursor.execute('insert into login_record (source_ip, login_time) values (?,?)',(source_ip, login_time))


	#建立 country_mapping 表	
	cursor.execute('create table country_mapping ( source_ip varchar(15) primary key not null, country varchar(50), times integer)')


	#從 login_record 表中找出連練次數最多的IP，用它來來找出所在的國家，存入 country_mapping 表
	cursor.execute('select source_ip, count(source_ip) from login_record group by source_ip order by 2 desc limit 10')

	values = cursor.fetchall()

	for z in values:

		source_ip = str(z[0])
		resp = requests.get('http://ipinfo.io/%s' % (source_ip))
		location = json.loads(resp.text)

		cursor.execute('insert into country_mapping (source_ip, country, times) values (?,?,?)',(source_ip, location['country'], z[1]))

	
	#查詢連線次數最多的IP，所在的國家和次數
	#cursor.execute('select * from country_mapping')
	#values = cursor.fetchall()
	#pprint (values)

	

	print ("Count the total number of HTTP requests recorded by this access logfile")

	cursor.execute('select count(source_ip) from login_record')
	values = cursor.fetchall()
	pprint (values)
	print (" ")

	print ("Find the top-10 (host) hosts makes most requests from 2017-06-10 00:00:00 to 2017-06-19 23:59:59, inclusively")
	cursor.execute('select source_ip, count(source_ip) from login_record where login_time between "2017-06-10 00:00:00" and "2017-06-19 23:59:59" group by 1 order by 2 desc limit 10')
	values = cursor.fetchall()
	pprint (values)
	print (" ")

	print ("Find out the country with most requests originating from (according the source IP)")
	cursor.execute('select * from country_mapping')
	values = cursor.fetchall()
	pprint (values)


	#關閉SQL命令
	cursor.close()
	#送出commit
	conn.commit()
	# 關閉Connection
	conn.close()
	

if __name__ == '__main__':
	main()