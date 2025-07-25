FROM python:3

WORKDIR /src

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY testQhue.py ./

CMD ["python", "testQhue.py"]