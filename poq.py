class Computer():
    def __init__(self,cpu_freq,cpu_cores, ram, hdd = None, sdd = None):
        self.cpu_freq = cpu_freq
        self.cpu_cores = cpu_cores
        self.ram = ram
        self.hdd = hdd
        self.sdd = sdd