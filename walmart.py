import requests
import decimal
import config.py as cfg

def Walmart(object):
    """
    Create Walmart object with the item name as the argument.
    Call get_price on the object to get the price.
    """
    def __init__(self, item):
        self.item = item

    def _get_product_id(self):
        search = requests.get('http://api.walmartlabs.com/v1/search?apiKey={0}&lsPublisherId={1}&query={2}'.format(walmart_api_key, linkshare_publisher_id, self.item))

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
        self.item_id = self._get_product_id()

        if self.item_id <= 0:
            return self.item_id

        else:
            lookup = requests.get('http://api.walmartlabs.com/v1/items/{0}?apiKey={1}&lsPublisherId={2}&format=json'.format(self.item, walmart_api_key, linkshare_publisher_id))

        if lookup.status_code == requests.codes.ok and 'json' in r.headers['content-type']:
            item_json = lookup.json()

        else:
            return -3

        price = item_json['salePrice']

        if price > 0:
            return decimal.Decimal(price) / 100   # API returns cost in cents, this converts to dollars

        else:
            return -4


