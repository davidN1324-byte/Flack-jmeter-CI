FROM eclipse-temurin:11-jre

ARG JMETER_VERSION=5.6.3

RUN apt-get update && apt-get install -y wget unzip && \
    wget https://archive.apache.org/dist/jmeter/binaries/apache-jmeter-${JMETER_VERSION}.zip && \
    unzip apache-jmeter-${JMETER_VERSION}.zip -d /opt && \
    mv /opt/apache-jmeter-${JMETER_VERSION} /opt/jmeter && \
    rm apache-jmeter-${JMETER_VERSION}.zip && \
    apt-get clean

ENV JMETER_HOME=/opt/jmeter
ENV PATH="$JMETER_HOME/bin:${PATH}"

WORKDIR /tests

CMD ["jmeter", "-v"]
