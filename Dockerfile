FROM python:3.7-slim

WORKDIR /django
COPY . /django/
RUN pip install -r /django/requirements.txt

ENV LD_LIBRARY_PATH=/opt/oracle/instantclient_21_4

RUN apt-get update && \
    apt-get install -y libpq-dev zlib1g-dev build-essential shared-mime-info libaio1 libaio-dev unzip wget --no-install-recommends && \
    wget https://download.oracle.com/otn_software/linux/instantclient/214000/instantclient-basic-linux.x64-21.4.0.0.0dbru.zip && \
    mkdir -p /opt/oracle && \
    cp instantclient-* /opt/oracle/ && \
    cd /opt/oracle/ && \
    unzip instantclient-basic-linux.x64-21.4.0.0.0dbru.zip && \
    rm -rf /var/lib/apt/lists/* instantclient-basic-linux.x64-21.4.0.0.0dbru.zip && \
    apt -y clean && \
    apt -y remove wget unzip && \
    apt -y autoremove && \
    rm -rf /var/cache/apt



# CMD ["gunicorn", "--bind", ":8080", "--workers", "1", "--threads", "8" ,"manage.py"]
# CMD exec gunicorn --bind :8080 --workers 1 --threads 8 --timeout 0 manage.py runserver:app
# CMD ["gunicorn", "manage.py", "runserver", "0.0.0.0:8080"] 

EXPOSE 8080
# start server
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8080"]

# CMD exec gunicorn --bind :8081 --workers 1 --threads 8 --timeout 0 python manage.py runserver:application
