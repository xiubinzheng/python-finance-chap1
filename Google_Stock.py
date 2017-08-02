import numpy as np
import pandas as pd
from pandas_datareader import data, wb

#ImportError: The pandas.io.data module is moved to a separate package
#  (pandas-datareader). After installing the pandas-datareader package
# (https://github.com/pydata/pandas-datareader),
# you can change the import
# ``from pandas.io import data, wb`` to
# ``from pandas_datareader import data, wb``.



goog = data.DataReader('GOOG', data_source='google',start='3/14/2015',end='4/14/2017')

goog.tail(0)