FROM datamechanics/spark:3.1-latest

WORKDIR /opt/application/

# Set up the ENV vars
ENV AWS_ACCESS_KEY_ID=""
ENV AWS_SECRET_ACCESS_KEY=""
ENV AWS_REGION=""
ENV AWS_SESSION_TOKEN=""
ENV s3_bucket=""
ENV inp_prefix=""
ENV out_prefix=""
ENV PYSPARK_MAJOR_PYTHON_VERSION=3

COPY cda_spark_kubernetes.py $WORKDIR
