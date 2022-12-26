FROM python 

COPY . /main.py 

WORKDIR .

CMD ["python3", "./main.py"]
