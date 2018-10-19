import logging

import jinja2

LOGGER = logging.getLogger(__name__)

class Card(object):

    def __init__(self, template):
        self.template = jinja2.Environment().from_string(template)

    def generate(self, alert):
        LOGGER.debug("Generate alert for: %s", alert)
        return self.template.render(alert=alert)