import requests

class Text(object):
    def __init__(self, text):
        self.text = text

    def get_item():
        return self.text.find("item: ")

def Walmart(object):
    def __init__(self, item):
        self.item = item

    def get_product_id(self):
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

    def get_price(self):
        self.item_id = self.get_product_id()

        if self.item_id <= 0:
            return self.item_id

        else:
            lookup = requests.get('http://api.walmartlabs.com/v1/items/12417832?apiKey={apiKey}&lsPublisherId={Your LinkShare Publisher Id}&format=json')

        if lookup.status_code == requests.codes.ok and 'json' in r.headers['content-type']:
            item_json = lookup.json()

        else:
            return -3

        price = item_json['salePrice']

        if price > 0:
            return price

        else:
            return -4
