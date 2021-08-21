#https://www.pybootcamp.com/blog/how-to-containerize-python-application/

FROM python:3.8.5-slim-buster
COPY . /src
RUN pip install boto3
RUN pip install pyyaml
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

