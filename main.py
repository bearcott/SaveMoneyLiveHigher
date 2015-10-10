import requests

class Text(object):
    def __init__(self, text):
        self.text = text

    def get_item():
        return self.text.find("item: ")

def Walmart(object):
    def __init__(self, item):
        self.item = item

    def get_product_id():
        search = requests.get('http://api.walmartlabs.com/v1/search?apiKey={apiKey}&lsPublisherId={Your LinkShare Publisher Id}&query={0}'.format(self.item)

        if search.status_code == requests.codes.ok and 'json' in r.headers['content-type']:
            product_json = search.json()

        else:
            return -1

        item_list = product_json['items']
        item = item_list[0]
        item_id = item['itemId']

        if item_id > 0:
            return item_id

        else:
            return -2

