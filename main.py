from timeit import timeit
from tabulate import tabulate
import sys

from io import BytesIO
import fastavro

setup_protobuf = '''

import data_pb2

d = data_pb2.Data(words="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris adipiscing adipiscing placerat. Vestibulum augue augue, pellentesque quis sollicitudin id, adipiscing.",
                  list=list(range(100)),
                  dict=dict((str(i), 'a') for i in iter(range(100))),
                  int=100,
                  float=100.123456,
                  )
#d.words = """
 # Lorem ipsum dolor sit amet, consectetur adipiscing
 # elit. Mauris adipiscing adipiscing placerat.
 # Vestibulum augue augue,
 # pellentesque quis sollicitudin id, adipiscing.
 # """
#d.list.extend(list(range(100)))
#d.dict = dict((str(i), 'a') for i in iter(range(100)))
#d.int = 100
#d.float = 100.123456

src = d.SerializeToString()

'''

setup_avro = '''

import fastavro
from io import BytesIO
import json

from schema import SCHEMA

def avro_serialize(data, schema=SCHEMA):
    bytes_writer = BytesIO()
    fastavro.schemaless_writer(bytes_writer, schema, data)
    return bytes_writer.getvalue()


def avro_deserialize(binary, schema=SCHEMA):
    bytes_writer = BytesIO()
    bytes_writer.write(binary)
    bytes_writer.seek(0)

    data = fastavro.schemaless_reader(bytes_writer, schema)
    return data
    
d = {
    'words': """
 Lorem ipsum dolor sit amet, consectetur adipiscing
 elit. Mauris adipiscing adipiscing placerat.
 Vestibulum augue augue,
 pellentesque quis sollicitudin id, adipiscing.
 """,
    'list': list(range(100)),
    'dict': dict((str(i), 'a') for i in iter(range(100))),
    'int': 100,
    'float': 100.123456,
}

src = avro_serialize(d)
    
'''


"""
Dependencies:
 wget http://pyyaml.org/download/libyaml/yaml-0.2.5.tar.gz
 tar -xvzf yaml-0.2.5.tar.gz
 cd yaml-0.2.5
 ./configure
 make
 make install
 
 wget https://pyyaml.org/download/pyyaml/PyYAML-5.1.tar.gz
 tar -xvzf PyYAML-5.1.tar.gz  
 cd PyYAML-5.1
 python setup.py --with-libyaml install
 
 wget https://github.com/protocolbuffers/protobuf/releases/download/v3.19.4/protobuf-python-3.19.4.tar.gz
 tar -xvzf protobuf-python-3.19.4.tar.gz
 cd protobuf-python-3.19.4 && ./configure && make && sudo make install
 protoc -I=. --python_out=. data.proto
 pip3 install protobuf
 
 pip3 install tabulate simplejson msgpack dict2xml fastavro protobuf
"""

message = '''d = {
    'words': """
 Lorem ipsum dolor sit amet, consectetur adipiscing
 elit. Mauris adipiscing adipiscing placerat.
 Vestibulum augue augue,
 pellentesque quis sollicitudin id, adipiscing.
 """,
    'list': list(range(100)),
    'dict': dict((str(i), 'a') for i in iter(range(100))),
    'int': 100,
    'float': 100.123456,
}'''

setup_pickle = '%s ; import pickle ; src = pickle.dumps(d, 2)' % message
setup_json = '%s ; import json; src = json.dumps(d)' % message
setup_yaml = '%s ; import yaml ; from yaml import CLoader as Loader, CDumper as Dumper ; src = yaml.dump(d, Dumper=Dumper)' % message
setup_msgpack = '%s ; import msgpack ; src = msgpack.dumps(d)' % message
setup_xml = '%s ; from xml.dom.minidom import parseString ; from dicttoxml import dicttoxml ; src = dicttoxml(d)' % message
# setup_fastavro = '''%s ; import fastavro ; src = avro_serialize(d)''' % message
tests = [
    # (title, setup, enc_test, dec_test)
    ('protobuf', setup_protobuf, 'd.SerializeToString()', 'd.ParseFromString(src)'),
    ('avro', setup_avro, 'avro_serialize(d)', 'avro_deserialize(src)'),
    ('pickle (native serialization)', 'import pickle; %s' % setup_pickle, 'pickle.dumps(d, 2)', 'pickle.loads(src)'),
    ('json', 'import json; %s' % setup_json, 'json.dumps(d)', 'json.loads(src)'),
    ('msgpack', 'import msgpack ; %s' % setup_msgpack, 'msgpack.dumps(d)', 'msgpack.loads(src)'),
    ('xml', 'from xml.dom.minidom import parseString ; from dicttoxml import dicttoxml ; %s' % setup_xml, 'dicttoxml(d)', 'parseString(src).toprettyxml()'),
    ('yaml', 'import yaml ; %s' % setup_yaml, 'yaml.dump(d, Dumper=Dumper)', 'yaml.load(src, Loader=Loader)'),
    ]

loops = 500
enc_table = []
dec_table = []
print("Running tests (%d loops each)" % loops)

for title, mod, enc, dec in tests:
    print(title)
    print(" [Encode]", enc)
    result = timeit(enc, mod, number=loops)
    exec(mod)
    enc_table.append([title, result, sys.getsizeof(src)])
    print(" [Decode]", dec)
    result = timeit(dec, mod, number=loops)
    dec_table.append([title, result])


enc_table.sort(key=lambda x: x[1])
enc_table.insert(0, ['Package', 'Seconds', 'Size'])
dec_table.sort(key=lambda x: x[1])
dec_table.insert(0, ['Package', 'Seconds'])
print("\nEncoding Test (%d loops)" % loops)
print(tabulate(enc_table, headers="firstrow"))
print("\nDecoding Test (%d loops)" % loops)
print(tabulate(dec_table, headers="firstrow"))
