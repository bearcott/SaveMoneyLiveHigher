import requests, pprint, time
from config import conf




class TextWrapper:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    def send(self, message):
        payload = {
            'method':'post',
            'to':"+2145420981",
            'message':message
        }
        send = requests.post('https://:@api.clicksend.com/rest/v2/send.json', auth=(self.username,self.password), params=payload)
        return send

    def getReply(self):
        reply = requests.post('https://:@api.clicksend.com/rest/v2/reply.json', auth=(self.username,self.password))
        #refresh request every time u get no replies
        while(reply.json()['replycount'] == '0'):
            time.sleep(1)
            print "."
            reply = requests.post('https://:@api.clicksend.com/rest/v2/reply.json', auth=(self.username,self.password))
        return reply.json()

    def parse(self,text):
        return



texter = TextWrapper(conf['USERNAME'],conf['PASSWORD'])

texter.send(conf['TEAM'])
pprint.pprint(texter.getReply())
response = raw_input("The price is?")
texter.send(response)
pprint.pprint(texter.getReply())

pprint.pprint(texter.getReply())


'''
    1. send text name
    2. get reply, recieve intro
    3. parse intro, get num
    4. send num
    5. get reply, recieve follow up
    6. repeat 3-5

'''
