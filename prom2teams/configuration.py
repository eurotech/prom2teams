import logging

import configargparse

LOGGER = logging.getLogger(__name__)

def get_config():
    p = configargparse.ArgParser(
        default_config_files=['/etc/prom2teams/prom2teams.conf']
    )

    p.add('-c', '--config', required=False, is_config_file=True, help='config file path')

    p.add('--host', help='bind host')
    p.add('--port', help='bind port', type=int)

    p.add('--level', help='log level')

    p.add('--template', help='template path')

    p.add('--connectors', help='teams connector', nargs='+', env_var='CONNECTOR')

    args, _ = p.parse_known_args()

    return args