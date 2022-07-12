FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /api_src
COPY requirements.txt /api_src/
RUN pip install -r requirements.txt
COPY .. /api_src/
