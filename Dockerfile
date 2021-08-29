#https://www.pybootcamp.com/blog/how-to-containerize-python-application/
# Pull Python base Image
FROM python:3.8.5-slim-buster
# Copy the project over the container path(/src)
COPY . /src
# Install Required Packages
RUN pip install boto3
RUN pip install pyyaml
RUN pip3 install mysql-connector-python

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2
# Install project-specific libraries
RUN python /src/setup.py install

#RUN pip install -r /src/requirements.txt
#docker build -t health-analytics-system .

# Execute the code
#docker run health-analytics-system python /src/app.py

# Run interative mode with bash command
#docker run --rm -it --entrypoint bash health-analytics-system

# Run interative mode with python
#docker run --rm -it health-analytics-system

# Run Python Script Directly
#docker run -it --rm health-analytics-system /usr/local/bin/python /src/data_management/bin/run_s3_loader.py

