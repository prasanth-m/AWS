FROM public.ecr.aws/lambda/python:3.8

ARG HADOOP_VERSION=3.2.0
ARG AWS_SDK_VERSION=1.11.375

RUN yum -y install java-1.8.0-openjdk

RUN pip install pyspark

ENV SPARK_HOME="/var/lang/lib/python3.8/site-packages/pyspark"
ENV PATH=$PATH:$SPARK_HOME/bin
ENV PATH=$PATH:$SPARK_HOME/sbin
ENV PYTHONPATH=$SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.10.9-src.zip:$PYTHONPATH
ENV PATH=$SPARK_HOME/python:$PATH

RUN mkdir $SPARK_HOME/conf

RUN echo "SPARK_LOCAL_IP=127.0.0.1" > $SPARK_HOME/conf/spark-env.sh

#ENV PYSPARK_SUBMIT_ARGS="--master local pyspark-shell"
ENV JAVA_HOME="/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.302.b08-0.amzn2.0.1.x86_64/jre"
ENV PATH=${PATH}:${JAVA_HOME}/bin

# Set up the ENV vars for code
ENV AWS_ACCESS_KEY_ID=""
ENV AWS_SECRET_ACCESS_KEY=""
ENV AWS_REGION=""
ENV AWS_SESSION_TOKEN=""
ENV s3_bucket=""
ENV inp_prefix=""
ENV out_prefix=""

RUN yum install wget
# copy hadoop-aws and aws-sdk
RUN wget https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/${HADOOP_VERSION}/hadoop-aws-${HADOOP_VERSION}.jar -P ${SPARK_HOME}/jars/ && \ 
    wget https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/${AWS_SDK_VERSION}/aws-java-sdk-bundle-${AWS_SDK_VERSION}.jar -P ${SPARK_HOME}jars/

COPY spark-class $SPARK_HOME/bin/
COPY delta-core_2.12-0.8.0.jar ${SPARK_HOME}/jars/
COPY cda_spark_lambda.py ${LAMBDA_TASK_ROOT}

CMD [ "cda_spark_lambda.lambda_handler" ]