from vispy import app
from LiveGraph import LiveGraph, Canvas, DataStream

# Graph layout variables
rows = 2
cols = 1
samples = 1000

# Set up graphs
graph = LiveGraph(rows, cols, samples)

# Create datastream with n signals per graph, m graphs and random data if random=True
with DataStream(graph.n, graph.m, random=False) as data_stream:
    # Send graph setup object, y data, and amplitude array
    c = Canvas(graph, data_stream.y, data_stream)
    app.run()

