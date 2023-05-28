# FROM python:latest-alpine as bwroline
# FROM bwroline as builder
FROM alpine:3.17
# RUN ./bwroline
WORKDIR . /bwroline/bwroline
ADD ./ bmu.py
ADD ./ .dockerignore
COPY requirements.txt requirements.txt
# RUN pip install --upgrade pip
# RUN pip install -r requirements.txt
# RUN pip install --no-cache-dir --upgrade -r /requirements.txt
RUN pip install -r requirements.txt
FROM alpine:3.17
# COPY --from=builder /bwroline/usr/local
COPY . /bwroline
WORKDIR /bwroline
EXPOSE 8080
ENTRYPOINT "fastapi run bwroline.bmu:bwroline"
CMD ["uvicorn", "echo", "run", "bwroline.bmu:bwroline", "fastapi", "--host", "0.0.0.0", "--port", "8080", "daemon off"]
