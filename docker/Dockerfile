FROM python:3.9

COPY poetry.lock pyproject.toml Makefile ./

RUN make install-configure-poetry-no-dev

COPY src/ ./src
COPY scripts/ ./scripts

ENV PATH=".:${PATH}"
ENV PYTHONPATH=".:${PYTHONPATH}"