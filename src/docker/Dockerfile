FROM python:3.9

WORKDIR /usr/src
COPY src/ .

RUN pip install -r requirements.txt

EXPOSE 5500

ENTRYPOINT ["python", "-u", "read_data.py"]