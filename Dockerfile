FROM python:3.8-buster

RUN pip install --upgrade pip

ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

# include user code
ADD . /opt/code/packpack
WORKDIR /opt/code/packpack
RUN pip install -e .

#bind volume for easy development
VOLUME /opt/code/packpack
