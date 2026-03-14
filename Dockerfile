# # base image
# FROM python:3.9


# # work directry
# workdir / app

# # copy

# COPY . /app

# # run

# run pip install -r requirements.txt

# # port

# expose 8000

# # command

# CMD ['python','./app.py']


# base image
FROM python:3.11

# work directory
WORKDIR /app

# copy project
COPY . .

# install dependencies
RUN pip install -r requirements.txt

# port
EXPOSE 8000

# run app
CMD ["uvicorn","app:app","--host","0.0.0.0","--port","8000"]



### docker build -t car24/table .

## docker run -p 8001:8000 car24/table

## HOST PORT      CONTAINER PORT
##  8001      →        8000

# | Address     | Purpose                   |
# | ----------- | ------------------------- |
# | `0.0.0.0`   | server listens everywhere |
# | `localhost` | access from your computer |
# | `127.0.0.1` | loopback address          |
