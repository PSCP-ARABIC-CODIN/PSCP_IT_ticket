# IT TICKET BOT

## DEPENDENCIES
for develop and running this project the packages below this should be installed

### First step

to start developing the project. Installing "poetry" is recommmend for this project to prevent something like "Its work on my machine but not others".

### Installing poetry
To install poetry run the command below<br>

**Window**
```sh
pip install poetry
```

**Debian based OS (Such as: Ubuntu)**
```sh
sudo apt install python3-poetry
```

### RUN Poetry to set up Virtual Environment
Set up the virtujal environment for developing thsi project

Go to ```it_ticket``` directory
```sh
cd src/requirement/main/it_ticket
```
Set config for poetry to make it create virtual environment
```sh
poetry config virtualenvs.in-project true
```
Then install all dependencies run
```sh
poetry install
```

### Now Good to go 👍
except.... for those who want to use docker<br>
to build docker compose run this at root directory of the project 
```sh
make build
```

for start all microservice
```sh
make up
```

to stop the container
```sh
make down
```

to restart the service 
```sh
make re
```
