FROM python:3.10

# TODO: Standardize environment vars between docker, flask, and the flask config files

# TODO: Structure Dockerfile(s) for multi-app deployments, together with run script and build files

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]
CMD [ "run.py" ]
