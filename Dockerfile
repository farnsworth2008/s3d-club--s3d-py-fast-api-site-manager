# Based on https://fastapi.tiangolo.com/deployment/docker/#dockerfile
FROM python:3.9
RUN echo 'hello world'
COPY ./ .
RUN . ./s3d-env-init
