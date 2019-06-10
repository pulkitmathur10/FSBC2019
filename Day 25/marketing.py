#Online Marketing
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sqlite3

query = open('online_marketing.sql', 'r')
conn = sqlite3.connect('online_marketing.db')
DF = pd.read_sql('online_marketing.sql', conn)

