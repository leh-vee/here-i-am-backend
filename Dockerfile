FROM ghcr.io/osgeo/gdal:alpine-small-latest

ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
RUN apk add --no-cache python3 py3-pip geos

COPY requirements.txt /app/requirements.txt
RUN pip install --break-system-packages -r requirements.txt 

COPY . /app

# Expose the default Django port
EXPOSE 8080

# start server
CMD ["gunicorn", "--bind", ":8080", "--workers", "1", "backend.wsgi:application"]
