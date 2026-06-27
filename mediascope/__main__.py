"""Allow running mediascope as ``python -m mediascope``.

This module wires up Click's CLI entry point so that the package can be
invoked directly::

    python -m mediascope --help
    python -m mediascope ingest -p wired --since 2025-01-01
    python -m mediascope analyze -p wired -t Meta
    python -m mediascope careers list

It is equivalent to calling the ``mediascope`` console script installed
by ``pip install -e .`` or ``pip install mediascope``.
"""

from mediascope.cli import cli

if __name__ == "__main__":
    cli()
