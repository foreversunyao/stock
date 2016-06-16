#!/usr/bin/env python
import ystockquote
import json
import MySQLdb

try:
	conn=MySQLdb.connect(host='127.0.0.1',user='p_stock',passwd='p_stock',db='db_stock',port=3307)
	cur=conn.cursor()
	cur.execute('select code from tb_americanstockcode')
	codelist=cur.fetchall()
	for code in codelist:
		#print code[0]
		pre_data2 = ystockquote.get_historical_prices(code[0],'20160101','20160201')
		if  pre_data2[0][0].find('doctype') >= 0:
			continue
		processed_data2 = json.dumps(pre_data2,sort_keys=False,indent=4)
		#print processed_data2
                for data in pre_data2:
			if data[0].find('Date') >= 0:
				continue
			sql_ex="insert into db_stock.tb_stockinfo_day values('"+data[0]+"','"+code[0]+"',"+data[1]+","+data[2]+","+data[3]+","+data[4]+","+data[5]+","+data[6]+")"	 
	                print sql_ex
			cur.execute(sql_ex)
		cur.execute("commit")
	cur.close()
	conn.commit()
	conn.close()
except MySQLdb.Error,e:
	print "Mysql Error %d:%s"%(e.args[0],e.args[1])

#pre_data = ystockquote.get_all('GOOG')
#processed_data = json.dumps(pre_data,sort_keys=False,indent=4)
#print processed_data

#pre_data2 = ystockquote.get_historical_prices('GOOG','20160609','20160610')
#processed_data2 = json.dumps(pre_data2,sort_keys=False,indent=4)
#print processed_data2
