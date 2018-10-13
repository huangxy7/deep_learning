#_*_coding:utf-8_*_


def AddTail(filename):
    res = []

    with open(filename,'r') as f:
        for line in f:
            temp = ''
            pname,ptype = line.split('.')
            if 'red' in pname:
                temp = pname+'.'+ptype
                temp = ' '.join([temp.strip(),'1'])

            elif 'green' in pname:
                temp = pname+'.'+ptype
                temp = ' '.join([temp.strip(),'2'])
            else:
                temp = pname+'.'+ptype
                temp = ' '.join([temp.strip(),'0'])
            print(temp)

            
            res.append(temp+'\n')
    with open('res.txt','wb') as f:
        for line in res:
            f.write(line.encode('utf-8'))

if __name__=='__main__':
    AddTail('./val_bak.txt')
