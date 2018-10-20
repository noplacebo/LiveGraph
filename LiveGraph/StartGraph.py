from vispy import app
from LiveGraph import LiveGraph, Canvas
from DataHandling import SerialDataStream, DataStream

# Graph layout variables
rows = 2
cols = 1
samples = 10000
frequency = 200
port = 'COM3'
baud = 9600
data_delimiter = ' '
parity = None

# Set up graphs
graph = LiveGraph(rows, cols, samples)

# Create data stream with n signals per graph, m graphs and random data if random=True
with SerialDataStream(port, baud, parity, delim=data_delimiter) as sdata_stream:
    with DataStream(graph.n, graph.m, random=False, serial=sdata_stream) as data_stream:
        # Send graph setup object, y data, and amplitude array
        c = Canvas(graph, data_stream, frequency)
        app.run()

