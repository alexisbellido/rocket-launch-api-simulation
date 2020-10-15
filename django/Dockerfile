FROM python:3.7.6-slim-buster as builder

RUN set -e \
  && apt-get update \
  && apt-get install -y --no-install-recommends \
    build-essential \
    git-core \
    python3-dev \
    ssh \
  && rm -rf /var/lib/apt/lists/*

ARG SSH_PRIVATE_KEY
RUN mkdir -p /root/.ssh/ \
  && echo "${SSH_PRIVATE_KEY}" > /root/.ssh/id_rsa \
  && chmod 600 /root/.ssh/id_rsa \
  && echo "StrictHostKeyChecking no " > /root/.ssh/config

# Private repositories can be cloned now so the following will work on the
# intermediate container.
# git clone git@github.com:user/project.git
# pip install -e git://git.example.com/MyProject#egg=MyProject

COPY requirements.txt /root/requirements.txt

# Use Python virtual environment to simplify copying installed packages to the next stage
RUN python -m venv /env \
  && . /env/bin/activate \
  && pip install --upgrade pip \
  && pip install --no-cache-dir -r /root/requirements.txt

FROM python:3.7.6-slim-buster

RUN set -e \
  && apt-get update \
  && apt-get install -y --no-install-recommends \
  && apt-get autoremove -y \
  && rm -rf /var/lib/apt/lists/*

ENV PYTHONUNBUFFERED 1
ENV PROJECT_NAME project
ENV PROJECT_SOURCE_DIR $PROJECT_NAME
ENV BASE_DIR code
ENV PROJECT_TARGET_DIR /${BASE_DIR}/${PROJECT_NAME}
ENV PORT 8000

# Create a group and non-root user to run the app
ARG APP_USER=app
# Set the corresponding environment variables for the entrypoint
ENV USER $APP_USER
ENV GROUP $APP_USER

RUN groupadd -r ${APP_USER} && useradd --no-log-init -r -g ${APP_USER} ${APP_USER}

WORKDIR $PROJECT_TARGET_DIR

# Adding to the path allows running docker-entrypoint.sh
ENV PATH=${PATH}:/${BASE_DIR}/bin

EXPOSE $PORT

# Copy the Python virtual environment setup. This is the multi-stage build magic.
COPY --from=builder /env /env

# TODO
# COPY $PROJECT_SOURCE_DIR $PROJECT_TARGET_DIR

RUN mkdir -p /run/secrets
RUN mkdir -p /code/bin

COPY docker-entrypoint.sh /${BASE_DIR}/bin/docker-entrypoint.sh

# chown all the files to the app user
RUN chown -R ${APP_USER}:${APP_USER} /${BASE_DIR}
RUN chown -R ${APP_USER}:${APP_USER} /run/secrets

# Change to the non-root user
USER ${APP_USER}:${APP_USER}

SHELL ["/bin/bash", "-c"]
ENTRYPOINT ["/code/bin/docker-entrypoint.sh"]
