import sys
import pandas as pd


class ClimateData:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ClimateData, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.data = None
        self.df = None

    def read_input(self):
        n = int(sys.stdin.readline())
        columns = sys.stdin.readline()[:-1].split("\t")
        self.data = [line.split('\t') for line in (sys.stdin.readline() for _ in range(n))]
        self.df = pd.DataFrame(self.data, columns=columns)

    def process_data(self):
        # Find and replace missing values
        for col in ['tmin', 'tmax']:
            self.df[col] = pd.to_numeric(self.df[col], errors='coerce')
            self.df[col] = self.df[col].interpolate(method='polynomial', order=3)
        self.df.set_index(["yyyy", "month"], inplace=True)

    def print_interpolated_values(self):
        for line in self.data:
            if line[2].startswith("Missing"):
                print("%.1f" % self.df.loc[(line[0], line[1]), 'tmax'])
            if line[3].startswith("Missing"):
                print("%.1f" % self.df.loc[(line[0], line[1]), 'tmin'])
