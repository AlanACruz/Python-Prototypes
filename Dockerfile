FROM continuumio/anaconda3:latest

WORKDIR /usr/src/app

COPY . .

RUN conda install jupyter -y && \
    pip install -r requirements.txt

CMD [ "bash", "./run-test.sh" ]