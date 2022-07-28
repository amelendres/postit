#!/bin/sh

pipenv install --dev

cp local/.env* .

echo "Run the database migrations!"
echo "postit db create && postit db migrate"
echo "postit db create test && postit db migrate test"