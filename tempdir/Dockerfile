FROM python:3
RUN pip install flask
COPY  ./templates /home/myapp/templates/
COPY  mapquest_parse-json_7.py /home/myapp/
EXPOSE 5050
CMD python3 /home/myapp/mapquest_parse-json_7.py
