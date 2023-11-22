import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from enum import Enum
from scipy.stats import norm
import sys

from chapter1 import pd_readcsv
from chapter3 import standardDeviation

# NEED TO READ DATA FIRST

# grab fisrt string from arg
filename = sys.argv[1]
data = pd_readcsv(filename)
data = data.dropna()
