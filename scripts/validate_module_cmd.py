"""Recursively validate the numpy docstring of a module."""

from npdocval import validate_recursive


def validate_module(
    module_name: str,
) -> None:
    """Recursively validate the numpy docstring of a module."""
    print("Yeah!")
    print(validate_recursive)
    print(module_name)
