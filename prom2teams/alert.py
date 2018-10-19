import logging

import json
import pprint

LOGGER = logging.getLogger(__name__)

class Alert(object):

    def __init__(self, generic, alert):
        self.generic_fields = generic
        self.fields = alert

    @staticmethod
    def parse(content):
        """ Parse alerts """
        parsed_values = json.loads(content)
        parsed_alerts = parsed_values.get("alerts")

        del parsed_values["alerts"]

        alerts = []

        for alert in parsed_alerts:
            alerts.append(Alert(parsed_values, alert))

        return alerts