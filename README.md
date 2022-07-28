# Hexagonal Architecture in Python 
Using Flask and SqlAlchemy



## Installation and Usage

local with Python 3.7+, pipenv, and Postgres installed, run the following:
### Docker build

```
git clone repo
cd postit
docker-compose up --build
./setup.sh
```


## How to Run

### Postit Dev
```
    pipenv run postit db migrate
    pipenv run postit server
```

Reset the DB:
```
docker-compose stop
rm -Rf ./var
docker-compose up --build
```

### Postit tests:

```
    pipenv run postit db migrate test
    pipenv run postit check tests
    pipenv run postit check style
```


### TODO
* Add Value Objects
* Add UUID
* Add create migration command
* Clean repository method names