#!/bin/sh

# python3 /var/src/main.py

cd /var/it_ticket

trap "exit" TERM

poetry install
exec poetry run python3 it_ticket/__init__.py
