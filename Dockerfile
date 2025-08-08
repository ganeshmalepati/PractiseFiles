FROM python

WORKDIR /app

COPY ./app

CMD["bash", "-c", "for file in *.py; do echo running $file; python \"file\": done"]
