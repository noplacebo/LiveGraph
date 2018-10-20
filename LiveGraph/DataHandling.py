import numpy as np
import serial


class DataStreamError(Exception):
    pass


class DataStream(object):
    def __init__(self, no_signals, m, random=True, serial=None, data_chars=3):
        self.no_signals = no_signals
        self.m = m
        self.random = random
        self.amplitudes = None
        self.y = None
        self.serial = serial
        self.data_chars = data_chars

    def __enter__(self):
        self.amplitudes = np.zeros((self.m, 1)).astype(np.float32)
        self.y = self.amplitudes * np.zeros(self.m, self.no_signals).astype(np.float32)
        return self

    def __exit__(self, ex_type, ex_value, ex_traceback):
        pass

    def getdata(self):
        if self.random:
            data = .1 + .2 * np.random.rand(self.m, 1).astype(np.float32)
        else:
            data = self.getserial()
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



