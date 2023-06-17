# python-web-api-flask-async-surrealdb-simple

## Description
Creates an async api of `dog` document.
Has the ability to query by parameters.

Remotely tested with *testify*.

## Tech stack
- python
  - flask
    - async
  - surrealdb
  - testify
  - requests

## Docker stack
- python:latest
- surrealdb/surrealdb:latest

## To run
`sudo ./install.sh -u`
- Get all routes: http://localhost/help

## To stop
`sudo ./install.sh -d`

## For help
`sudo ./install.sh -h`

## Credits
- [Surrealdb docker image](https://surrealdb.com/docs/installation/running/docker)