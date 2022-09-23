"""Defines a command-line interface for insights."""

import click

from .validate_module_cmd import validate_module


@click.group()
def cli():
    """Command-line interface for the npdocval package."""
    pass


@cli.command(help=validate_module.__doc__)
@click.argument('module_name', type=str)
def module(
    module_name: str,
) -> None:
    validate_module(module_name)
