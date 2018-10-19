import logging

import urllib.request
import ssl

LOGGER = logging.getLogger(__name__)

_instances = {}

def get_connector(webhook):
    if webhook not in _instances:
        _instances[webhook] = Connector(webhook)
    return _instances[webhook]

class Connector(object):

    def __init__(self, webhook):
        self.webhook = webhook

        self.context = ssl.create_default_context()
        self.context.check_hostname = False
        self.context.verify_mode = ssl.CERT_NONE

    def send(self, data):
        encoded_data = data.encode('utf-8')

        req =  urllib.request.Request(self.webhook, data=encoded_data) # this will make the method "POST"
        try:
            LOGGER.debug("Sending alert to %s", self.webhook)
            resp = urllib.request.urlopen(req, context=self.context)
            LOGGER.debug("Alert sent to %s with return code %s",self.webhook, resp.getcode())
        except Exception as e:
            LOGGER.error("Error sending alert to %s: %s", self.webhook, e)