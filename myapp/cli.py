import logging
from configparser import ConfigParser
import os

import aiohttp_jinja2
import click
import jinja2
from aiohttp import web

from .database import connect_db, disconnect_db
from .middlewares import setup_middlewares
from .routes import setup_routes

NAME = __package__

DEFAULT_CONFIG_PATHS = ['config.ini']
DEFAULT_CONFIG = {
    'host': None,
    'port': None,
    'logging': 'INFO',
    'mongouri': None,
    'mongodb': 'db',
}


async def init_app(config=DEFAULT_CONFIG):
    app = web.Application()
    app['config'] = config
    aiohttp_jinja2.setup(app, loader=jinja2.PackageLoader(NAME, 'templates'))

    app.on_startup.append(startup_tasks)
    app.on_cleanup.append(cleanup_tasks)

    setup_routes(app)
    setup_middlewares(app)

    return app


def config_callback(ctx, config_param, config_file):
    config_paths = DEFAULT_CONFIG_PATHS + ([config_file] if config_file else [])
    cfgparser = ConfigParser()
    cfgparser.read(config_paths)
    config = dict(cfgparser[NAME]) if NAME in cfgparser else dict()
    for param in ctx.command.params:
        if param.name in config:
            param.default = config[param.name]


async def startup_tasks(app):
    gunicorn_nworkers = int(os.environ.get('GUNICORN_NUM_WORKERS', 0))
    gunicorn_workerid = int(os.environ.get('GUNICORN_WORKER_ID', 0))

    global_period = 10
    worker_period = global_period * gunicorn_nworkers
    worker_offset = (gunicorn_workerid - 1) * global_period
    await asyncio.sleep(worker_offset)

    app['polling'] = asyncio.create_task(polling(period=worker_period, token=app['token']))


async def cleanup_tasks(app):
    app['polling'].cancel()
    with suppress(asyncio.CancelledError):
        await app['polling']

'''
@click.command()
@click.version_option(prog_name=NAME, version='0.0.0')
@click.option('--host', default=DEFAULT_CONFIG['host'], type=str, help='Server IP address')
@click.option('--port', default=DEFAULT_CONFIG['port'], type=int, help='Server port number')
@click.option('--logging', default=DEFAULT_CONFIG['logging'], help='Logging output level')
@click.option('--mongouri', default=DEFAULT_CONFIG['mongouri'], type=str, help='MongoDB URI')
@click.option(
    '--mongodb', default=DEFAULT_CONFIG['mongodb'], type=str, help='MongoDB Database Name'
)
@click.option(
    '--config',
    default=None,
    type=click.Path(exists=True),
    help='User-defined configuration file location',
    is_eager=True,
    expose_value=False,
    callback=config_callback,
)
def cli(**config):
    logging.basicConfig(level=getattr(logging, config['logging']))
    app = init_app(config=config)
    web.run_app(app, host=config['host'], port=config['port'])
'''
