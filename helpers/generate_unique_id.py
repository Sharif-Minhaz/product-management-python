import base64
import uuid


def generate_product_id():
    return "prod-" + base64.urlsafe_b64encode(uuid.uuid1().bytes)[:10].decode('utf-8')
