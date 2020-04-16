FROM python:3.8.2-buster
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app
CMD ["flask", "run", "--host=0.0.0.0"]