FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /code
COPY ./requirements.txt /code
WORKDIR /code
# Add --no-cache to the line below to skip caching.
#RUN apk add --update --virtual .build-deps gcc musl-dev build-base python-dev py-pip jpeg-dev zlib-dev && \
#    apk add libffi-dev postgresql-dev wkhtmltopdf
RUN pip install -r requirements.txt
#RUN apk del .build-deps

COPY . /code
EXPOSE 8000
ENTRYPOINT sh entrypoint.sh
