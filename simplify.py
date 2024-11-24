#简化shell提示符

import re

class Simplify:
    start=''
    target=''

    def __init__(self, str):
        self.start=str
        
    def filter(self):
        if re.match('.',self.start):
            x=self.start.split('/')

            #去掉..
            i=0
            j=0
            list=[]
            list1=[]

            for value in x:
                if value=='..':
                    list.append(i)
                i=i+1 

            list.reverse()

            for num in list:
                del x[num]
                del x[num-1]

            #去掉.
            for value in x:
                if value=='.':
                    list1.append(j)
                j=j+1 
                
            list1.reverse()   

            for num in list1:
                del x[num]

            self.target=("/".join(x))
            return self.target
            

        else:
            return self.start



if __name__ == "__main__":
    str='./home'
    clz=Simplify(str)
    str=clz.filter()
    print(str)
