import re
import time
import requests
import networkx as nx
import matplotlib.pyplot as plt
from getpass import getpass
import cPickle as pickle

class spider():    
    def __init__(self):

        self.data={}
        self.myuid=471872181
        self.ss = requests.Session()
        EMAIL = raw_input("enter your email on renren.com: ")
        PWD = getpass("enter the password: ") 
        acc_info = {'email': EMAIL, 'password': PWD}
        self.ss.post("http://www.renren.com/PLogin.do", data=acc_info)
    
    def get_friends(self, uid=471872181):

        print 'working on user %d\r' % uid, 
        page = 0
        res = [0]
        self.data[uid]=[]
        pa = re.compile('<dd>.*profile\.do\?id=(\d*)">.*</a>')
        url = "http://friend.renren.com/GetFriendList.do"
        
        while res:

            payload = {'curpage':str(page), 'id':str(uid)}
            r = self.ss.get(url, params = payload)
            res = map(lambda x:int(x), re.findall(pa, r.text))
            self.data[uid]+=res
            page+=1
##            time.sleep(1)
            
    def remove_dup(self):

        for l in self.data.values():
            try:
                l.remove(self.myuid)
            except ValueError:
                continue
    @property
    def relations(self):

        self.get_friends()
        my_friends = self.data[471872181]
        for u in my_friends:
            self.get_friends(uid=u)
        self.remove_dup()
        return self.data

sp = spider()
f = open('relations.pkl', 'wb')
pickle.dump(sp.relations, f, True)
