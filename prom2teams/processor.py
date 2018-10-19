import logging

import prom2teams.alert
import prom2teams.card
import prom2teams.connector

LOGGER = logging.getLogger(__name__)

class Processor(object):

    def __init__(self, template, connectors):
        self.template = template
        self.connectors = connectors

    def process(self, content):
        alerts = prom2teams.alert.Alert.parse(content)
        LOGGER.debug("Received %s new alerts", len(alerts))

        card = prom2teams.card.Card(self.template)
        for alert in alerts:
            alert_card = card.generate(alert)

            for connector in self.connectors:
                prom2teams.connector.get_connector(connector).send(alert_card)
