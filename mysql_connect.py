import nmap                       
import pymysql

        

class mysql_scan:

    def __init__(self,ip,port):
        self.ip=ip
        self.port=port
    
    def scan(self):
        nm = nmap.PortScanner()           
        nm.scan(self.ip,self.port) 

        for host in nm.all_hosts():      
            for proto in nm[host].all_protocols():                  #nm[host].all_protocols获取执行的协议['tcp','udp']
                lport = nm[host][proto].keys()                      #获取目标主机所开放的端口赋值给lport
                if 3306 in lport:
                    return 1
                else:
                    return 0

class mysql_connect:

    def __init__(self,host,user,password,database):
        self.host=host
        self.user=user
        self.password=password
        self.database=database

    def exe(self):

        db = pymysql.connect(host=self.host,user=self.user,password=self.password,database=self.database) 
       

        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        
        
        while True:
            
            sql_command=input("mysql>")
            
            if sql_command=='exit':
                db.close()
                break

            else:  
                try:  
                    # 使用 execute()  方法执行 SQL 查询
                    cursor.execute(sql_command)
                    

                    # 使用 fetchone() 方法获取单条数据.
                    data = cursor.fetchone()
                    
                    print ("%s" % data)
                
                except:
                    db.rollback()  # 事务回滚，撤销之前的操作
    
    def connect(self):
        try:
            conn = pymysql.connect(host=self.host,user=self.user,password=self.password,database=self.database)
            return 1

        except:
            return 0