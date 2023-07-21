


class msg :
    def __init__(self, text, uname, uid, id):
        self.text = text
        self.uname = uname
        self.uid = uid
        self.id = id

class node:
    msg: msg
    next: None
    def __init__(self, msg):
        self.msg = msg
        self.next = None
class msgList(object):
    head: None
    last=""
    def __init__(self):
        self.head = None
        self.last=""
    def length(self):
        p=self.head
        l=0
        while p!=None:
            l+=1
            p=p.next
        return l
    def lastid(self):
        p=self.head
        if p!=None:
            while p.next!=None:
                p=p.next
            self.last=p.msg.id
            return p.msg.id
        return self.last
    def add(self, node):
        p=self.head
        if p==None:
            self.head=node
            return
        while p.next!=None:
            p=p.next
        p.next=node
    def tolist(self):
        p=self.head
        l=[[],[],[]]
        while p!=None:
            l[0].append(p.msg.text)
            l[1].append(p.msg.uname)
            l[2].append(p.msg.uid)
            p=p.next
        return l
    def todict(self):
        p=self.head
        l=[]
        while p!=None:
            text=p.msg.text
            uname=p.msg.uname
            data={"text":text,"uname":uname}
            l.append(data)
            p=p.next
        return l

