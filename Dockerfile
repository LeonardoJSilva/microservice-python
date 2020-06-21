# Here is the build image
FROM python:slim-buster
WORKDIR /src
RUN apt-get update \
&& apt-get clean

ADD pyproject.toml* ./

RUN pip install 'pip==20.0.2' --force-reinstall

RUN pip install --no-cache -U poetry && poetry lock && poetry export -f requirements.txt > requirements.txt && pip install -r requirements.txt

ADD . .