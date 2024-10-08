#FROM --platform=linux/amd64 keppel.eu-de-1.cloud.sap/ccloud-dockerhub-mirror/library/python:3.12.5-slim
FROM --platform=linux/amd64 keppel.eu-de-1.cloud.sap/ccloud-dockerhub-mirror/library/python:3.13.0rc1-alpine

WORKDIR /usr/src/app

COPY setup.py /usr/src/app/
COPY README.md /usr/src/app/
RUN python -m pip install --upgrade pip
# Elasticsearch switched to a non open source license from version 7.11 onwards.
# Limit to earlier versions to avoid license and compatibility issues.
RUN pip install -e . 'elasticsearch<7.11'

COPY prometheus_es_exporter/*.py /usr/src/app/prometheus_es_exporter/
COPY LICENSE /usr/src/app/

EXPOSE 9206

LABEL source_repository="https://github.com/sapcc/prometheus-es-exporter"

ENTRYPOINT ["python", "-u", "/usr/local/bin/prometheus-es-exporter"]
