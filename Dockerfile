FROM ubuntu:20.04

RUN apt-get update \
    && add-apt-repository ppa:deadsnakes/ppa \
    && apt-get install -y python3.8 software-properties-common python3-pip \ 
    && pip3 --version \     
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
