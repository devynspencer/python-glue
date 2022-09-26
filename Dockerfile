FROM python:3.10

# TODO: Standardize environment vars between docker, flask, and the flask config files

# TODO: Structure Dockerfile(s) for multi-app deployments, together with run script and build files

# TODO: FLASK_DEBUG env var not being respected? See issue #52 -- https://github.com/devynspencer/python-glue/issues/52

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

ARG FLASK_DEBUG="false"
ENV FLASK_DEBUG="${FLASK_DEBUG}" \
    FLASK_SKIP_DOTENV="true"

ENTRYPOINT [ "python" ]
CMD [ "run.py" ]
