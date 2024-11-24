#payload: echo admin | sudo -S whoami
class su:
    passwd=''
    payload=''
    ex=''

    def __init__(self,passwd):
        self.passwd=passwd
        
    def get_payload(self):
        self.payload='echo '+self.passwd+' | sudo -S whoami'
        return self.payload

    def get_ex(self):
        self.ex='sudo -S '
        return self.ex

if __name__ == "__main__":
    clz=su('123456')
    print(clz.get_payload())
    print(clz.get_ex())