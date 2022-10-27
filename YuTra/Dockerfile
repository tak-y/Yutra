
# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.9

EXPOSE 80

COPY ./ /

RUN pip install fastapi, pydantic, datetime, openpyxl, jpholiday, googlemaps, pandas, requests. geopy, geocoder, mangum

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
