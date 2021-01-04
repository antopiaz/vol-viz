from pkg_resources import DistributionNotFound, get_distribution
from .cli import init_app

try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    __version__ = '0.0.0'
