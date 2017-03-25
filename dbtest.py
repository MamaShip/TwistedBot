# -*- coding: utf-8 -*-
import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

db = MySQLdb.connect(host="localhost",user="RF",passwd="somanypswd",db="Robot",charset='utf8')
cursor = db.cursor()


sql = "SELECT * FROM friends WHERE id = %d" % (2)
cursor.execute(sql)
results = cursor.fetchone()

print results

db.close()


'''
sql = "INSERT INTO friends VALUES (2,\'聪明\');"

try:
   # 执行sql语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()
'''
