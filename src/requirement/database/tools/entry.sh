#!/bin/sh

cd database/db

trap "exit" TERM

mongod --fork --logpath /var/log/mongodb/mongod.log -dbpath .
