# 
FROM python:3.10.5

USER root

# 
WORKDIR /app

# 
COPY ./requirements.txt /app/requirements.txt

# 
RUN python -m venv venv && chmod +x ./venv/bin/activate
RUN ./venv/bin/activate
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# 
COPY ./ /app/

RUN adduser --system deploy

RUN chown -R deploy /app

USER deploy

EXPOSE 5000

ENTRYPOINT ["/app/deploy/startup"]
CMD ["run"]
