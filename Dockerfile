ARG BASE_IMAGE=python:3.13-slim-bookworm
ARG USER=api-template
ARG GROUP=api-template


### Install stage ###
FROM $BASE_IMAGE AS installer

RUN pip install uv
WORKDIR /app

COPY uv.lock .
COPY pyproject.toml .

RUN uv export -o requirements.docs.txt --only-group docs && \
    pip wheel -r requirements.docs.txt -w /wheels/docs --no-deps --no-cache-dir && \
    uv export -o requirements.project.txt --no-emit-package api-template && \
    pip wheel -r requirements.project.txt -w /wheels/project --no-deps --no-cache-dir


### Build stage ###
FROM $BASE_IMAGE AS builder

RUN pip install build hatchling
WORKDIR /app

COPY --from=installer /wheels/docs /wheels
RUN pip install /wheels/* --no-deps --no-cache-dir && \
    rm -rf /wheels

COPY . .

RUN mkdocs build && \
    python -m build -w -nx -o /wheels


### Run stage ###
FROM $BASE_IMAGE
ARG GROUP
ARG USER

RUN groupadd $GROUP && \
    useradd -m -g $GROUP -u 1000 $USER
WORKDIR /home/$USER/app

COPY --from=installer /wheels/project /wheels
RUN pip install /wheels/* --no-deps --no-cache-dir && \
    rm -rf /wheels

COPY --from=builder /wheels /wheels
RUN pip install /wheels/* --no-deps --no-cache-dir && \
    rm -rf /wheels

COPY static/docs static/docs
COPY --from=builder /app/site static/site

RUN chown -R $USER:$GROUP /home/$USER
USER $USER
CMD ["api-template"]
