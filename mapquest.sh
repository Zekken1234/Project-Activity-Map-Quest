#!/bin/bash

mkdir tempdir

cp mapquest_parse-json_7.py tempdir/.

echo "FROM python" >> tempdir/Dockerfile
echo "RUN pip install flask" >> tempdir/Dockerfile
echo "COPY  mapquest_parse-json_7.py /home/myapp/" >> tempdir/Dockerfile
echo "EXPOSE 8080" >> tempdir/Dockerfile
echo "CMD python3 /home/myapp/mapquest_parse-json_7.py" >> tempdir/Dockerfile

cd tempdir
docker build -t mapquest .
docker run -t -d -p 8080:8080 --name mqrunning mapquest
docker ps -a 
