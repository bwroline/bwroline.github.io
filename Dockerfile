# build an image starting with python latest version
# FROM python:3.1.0-alpine
# FROM 3.1.0-alpine as builder
# set work directory to bwroline and bmu
FROM alpine:3.17
# RUN ./bmu
WORKDIR /bmu
ADD ./ bmu.py
COPY requirements.txt /requirements.txt
# RUN pip install --upgrade pip
# RUN pip install -r requirements.txt
# RUN pip install --no-cache-dir --upgrade -r requirements.txt ./requirements.txt

FROM alpine:3.17
# COPY --from=builder /bmu/usr/local
# copy current dir . in project directory to work directory . in the image
COPY . /bmu
WORKDIR /bmu
EXPOSE 8080
# default command for container to fastapi run
CMD ["uvicorn", "echo", "bmu:bwroline", "run", "fastapi", "--host", "0.0.0.0", "--port", "8080", "daemon off"]
# CMD ["uvicorn", "shamudoents.com", "fastapi", "run"]
