FROM python:latest

RUN pip install --no-cache-dir pywttr asyncio logging aiogram

WORKDIR /app

COPY . /app

CMD ["python3"]