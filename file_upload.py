import base64
import os

class Upload:
    poc=''

    def __init__(self,filename):
        self.filename=filename

    def check(self):
        return  os.path.exists(self.filename)

    def exe(self):
        with open(self.filename, 'r') as file: 
            content = file.read() 
            
            byte_encoded_str = base64.b64encode(content.encode('utf-8'))

            encoded_str=str(byte_encoded_str,'utf-8')

            Upload.poc=encoded_str
            
            
