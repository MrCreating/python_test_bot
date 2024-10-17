FROM python:latest

RUN pip install --no-cache-dir pywttr asyncio logging aiogram python-dotenv

WORKDIR /app

COPY . /app

CMD ["python3"]