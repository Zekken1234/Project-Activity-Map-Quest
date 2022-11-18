#!/bin/bash

mkdir tempdir
mkdir tempdir/templates

cp mapquest_parse-json_7.py tempdir/.
cp -r templates/* tempdir/templates/.

echo "FROM python:3" >> tempdir/Dockerfile
echo "RUN pip install flask" >> tempdir/Dockerfile
echo "COPY  ./templates /home/myapp/templates/" >> tempdir/Dockerfile
echo "COPY  mapquest_parse-json_7.py /home/myapp/" >> tempdir/Dockerfile
echo "EXPOSE 5050" >> tempdir/Dockerfile
echo "CMD python3 /home/myapp/mapquest_parse-json_7.py" >> tempdir/Dockerfile

cd tempdir
docker build -t mapquest .
docker run -t -d -p 5050:5050 --name mqrunning mapquest
docker ps -a 
