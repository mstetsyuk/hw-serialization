FROM python:3.9

COPY . .

RUN apt update && apt install build-essential

#RUN cd yaml-0.2.5 && ./configure && make && make install && cd ../PyYAML-5.1 && python setup.py --with-libyaml install

RUN pip3 install tabulate simplejson msgpack dicttoxml dict2xml fastavro protobuf pyyaml

ENTRYPOINT python3 main.py
