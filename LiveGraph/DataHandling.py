import numpy as np
import serial


class DataStreamError(Exception):
    pass


class DataStream(object):
    def __init__(self, no_signals, m, source, random=True, data_chars=3, delim=' '):
        self.no_signals = no_signals
        self.source = source
        self.delim = delim
        self.m = m
        self.random = random
        self.amplitudes = None
        self.y = None
        self.data_chars = data_chars
        self.slice_op = slice(data_chars)
        self.amplitudes = np.zeros((self.m, 1)).astype(np.float32)
        self.y = self.amplitudes * np.zeros((self.m, self.no_signals)).astype(np.float32)

    def __enter__(self):
        return self

    def __exit__(self, ex_type, ex_value, ex_traceback):
        pass

    def getdata(self):
        if self.random:
            data = .1 + .2 * np.random.rand(self.m, 1).astype(np.float32)
        else:
            rawdata = self.source.readline()
            splitdata = rawdata.split(self.delim)
            data = np.zeros((len(splitdata),1))
            for i in range(len(splitdata)):
                data[i] = float(splitdata[i][self.slice_op])
                data = data.astype(np.float32)
                print(data)
        return data

    def getserial(self):
        raw_data = self.serial.getdata()
        data = np.zeros(len(raw_data)).astype(np.float32)
        for i in range(len(data)):
            data[i] = raw_data[i][0][self.data_chars]
        return data


class SerialDataStream(object):
    def __init__(self, port, baud, parity, timeout=1, rtscts=1, delim=' '):
        self.port = port
        self.baud = baud
        self.timeout = timeout
        self.parity = parity
        self.rtscts = rtscts
        self.serial_conn = None
        self.delim=delim

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # self.serial_conn.close()
        pass

    def getdata(self):
        dataline = self.serial_conn.readline()
        data = dataline.split(self.delim)
        return data



