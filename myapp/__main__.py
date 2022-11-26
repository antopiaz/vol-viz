import sys

from .cli import NAME

cli(sys.argv[1:], prog_name=NAME, auto_envvar_prefix=NAME.upper())
