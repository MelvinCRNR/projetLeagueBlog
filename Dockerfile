FROM python:3
COPY . .
WORKDIR .
EXPOSE 5000
CMD python3 -m venv env
CMD source env/bin/activate
COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt
COPY . .
CMD ["flask", "db", "init"]
CMD ["flask", "db", "migrate"]
CMD ["flask", "db", "update"]
CMD ["flask", "run", "--host=0.0.0.0"]