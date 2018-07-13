from collections import namedtuple
from copy import deepcopy
import wallaroo
import os

def application_setup(args):
    in_host, in_port = wallaroo.tcp_parse_input_addrs(args)[0]
    out_host, out_port = wallaroo.tcp_parse_output_addrs(args)[0]
    tcp_source = wallaroo.TCPSourceConfig(in_host, in_port, decoder)
    tcp_sink = wallaroo.TCPSinkConfig(out_host, out_port, encoder)

    ab = wallaroo.ApplicationBuilder("Hanging message send")
    ab.new_pipeline("Hangy pipeline", tcp_source)
    ab.to_stateful(stateful, Dud, "s")
    ab.to_parallel(stateless)
    ab.to_sink(tcp_sink)
    return ab.build()

@wallaroo.state_computation(name="s")
def stateful(_item, _buffer):
    # 0 = 291, 1 = 295, 2 = 299, 100 = 691, 1000 = 4291
    # Formula: stringlen*4 + 291
    # 4023 = 16383
    # 4024 = 16387 # HANGS
    ret = '\x01' * 4024
    return (ret, False)

class Dud():
    def __init__(self):
        True

@wallaroo.computation(name="stateless")
def stateless(x):
    print "stateless ran on %s"%(os.getpid())
    return x

@wallaroo.decoder(header_length=4, length_fmt=">I")
def decoder(line):
    return("x")

@wallaroo.encoder
def encoder(results):
    return("NODE %s ENCODED\n"%(os.getpid()))
