FROM python:3.14-slim
WORKDIR /app
COPY . .
RUN pip install discord.py  # Hier nur deine wichtigste Library rein
EXPOSE 10000
CMD ["python", "main.py"]
