#!/usr/bin/env python3

"""
Forward prometheus notifications to teams.

Usage:
    python prom2teams --help
"""

import logging

import prom2teams.configuration
import prom2teams.server
import prom2teams.processor

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

LOGGER = logging.getLogger(__name__)

def main():
    """ Main function of the prom2teams """
    args = prom2teams.configuration.get_config()

    with open(args.template, 'r') as template_file:
        template = template_file.read()

    processor = prom2teams.processor.Processor(template, args.connectors)

    server = prom2teams.server.Server()
    server.listen(args.host, args.port, processor.process)

if __name__ == '__main__':
    main()