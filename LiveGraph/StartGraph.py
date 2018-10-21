from vispy import app, LiveGraph
from LiveGraph import Canvas
from DataHandling import DataStream

# Graph layout variables
rows = 2
cols = 1
samples = 100
frequency = 2
port = 'COM3'
baud = 9600
data_delimiter = ' '
parity = None
# data_file = "G:\PyCharm\LiveGraph\LiveGraph\\test_data.txt"

# Set up data source
# source = serial()
def livevispygraph(data_file):
    with open(data_file, 'r') as source:

        # Set up graphs
        graph = LiveGraph(rows, cols, samples)

        # Create data stream with n signals per graph, m graphs and random data if random=True
        # with SerialDataStream(port, baud, parity, delim=data_delimiter) as sdata_stream:
        with DataStream(graph.n, graph.m, random=False, source=source) as data_stream:
            # Send graph setup object, y data, and amplitude array
            c = Canvas(graph, data_stream, frequency)
            app.run()

def livematlibgraph(data_file):
    with open(data_file, 'r') as source:
        pass
