import cx_Oracle
dsn_tns = cx_Oracle.makedsn('198.100.100.201', '1521', 'medprod')
conn = cx_Oracle.connect(user='cpmedix', password='pak123', dsn=dsn_tns)
c = conn.cursor()
c.execute('select * from tab')
for row in c:
   print(row)
conn.close()