#	This is Makefile just to make life easier
#	for those who want to build and run on docker
#	by run "make" following by rule declared below
#	Ex.
# 		"make build" - to build the docker compose
#		"make up" - to start all microservice
#		"make down" - to stop all microservice
#		"make re" - to restart all microservice

all: re

init-dir: src/requirement/database/db

src/requirement/database/db:
	mkdir -p src/requirement/database/db

build: init-dir
	docker compose -f ./src/docker-compose.yml build --no-cache

up:
	docker compose -f src/docker-compose.yml up -d

down:
	docker compose -f src/docker-compose.yml down

re: down up

.PHONY: all build up down re
