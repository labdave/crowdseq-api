# base image
FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# update and install system packages
RUN apt update \
    && apt-get install -y postgresql-server-dev-all gcc python3-dev musl-dev

# copy the requirements file
COPY requirements.txt .

# update the pip and install the requirements
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# copy the api code
COPY . .

# expose the port 8000
EXPOSE 8000
