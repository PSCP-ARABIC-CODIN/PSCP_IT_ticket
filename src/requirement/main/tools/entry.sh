#!/bin/sh

cd /var/it_ticket

trap "exit" TERM

poetry install
exec poetry run python3 it_ticket/main.py
