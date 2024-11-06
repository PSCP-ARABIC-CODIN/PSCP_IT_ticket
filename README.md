# IT TICKET BOT

## DEPENDENCIES
For develop and running this project the packages below this should be installed
* poetry
* Docker

### First step ( •̀ ω •́ )y

To start developing the project. Installing "poetry" is recommmend for this project to prevent something like<br>**"Its work on my machine but not others."**

### Installing poetry ✍️(◔◡◔)
To install poetry run the command below<br>

**Window**<br>
recommend to use git bash
```sh
pip install poetry
```

**Debian based OS (Such as: Ubuntu)**
```sh
sudo apt install python3-poetry
```

### RUN Poetry to set up Virtual Environment 🖥️
Set up the virtual environment for developing thsi project

Go to ```it_ticket``` directory
```sh
cd src/requirement/main/it_ticket
```
Set config for poetry to make it create virtual environment
```sh
poetry config virtualenvs.in-project true
```
Then to install all dependencies run
```sh
poetry install
```

### Containerize 📦
Docker also require in order to run an entire service.
```sh
make build
```

start all microservice
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
