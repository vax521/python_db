import ibm_db
conn = ibm_db.connect("DATABASE=tkopmd;HOSTNAME= 127.0.0.1;PORT=50000;PROTOCOL=tcpip;UID=**;PWD=***;", "", "")
empid = 100000000000
#print(conn)
if conn:
    for i in range(100,101):
        sql = """ INSERT INTO OPMD_TRANSFER_EMPLOYEE_BASE_INFO_TKCMS ( C_GROUPEMPID,  C_OAUSERNAME,C_EMPNUM,C_NAME)
    VALUES
    ('"""+str(empid)+"""'
        ,
        'test"""+str(i)+"""',
        '00001111',
        '张三"""+str(i)+"""'
    );"""
        stmt = ibm_db.exec_immediate(conn,sql)
        # while ibm_db.fetch_row(stmt) != False:
        #     result = ibm_db.fetch_assoc(stmt)
            # for key,value in result.items():
            # print(key,value)
        empid = empid+1
#最后记得关闭数据库连接
ibm_db.close(conn)