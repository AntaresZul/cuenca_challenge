# Saul Penaloza Cuenca Challenge

These are the instructions to initialize the docker-compose solution. (It is assumed that Docker and Docker Compose are previously installed on your machine)

## Build and Initialize Docker

> docker-compose up --build

## Inspect database

> docker exec -it cuenca_test_db_1 bash

> psql postgres://username:secret@localhost:5432/database
