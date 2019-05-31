# URL shortening service Bitly

import pandas as pd
import numpy as np


from collections import Counter

try:
   
    json_df = pd.read_json("usagov_bitly_data.json", lines=True)

    
    json_df = json_df.replace([np.nan, ""], ["Mising", "Unknown"])

   
    json_df_tz = json_df['tz'].value_counts().head(10)

    
    json_tz = Counter(json_df['tz'])

    json_tz = sorted(json_tz.items(), key=lambda x: x[1], reverse=True)

    json_tz = json_tz[:10]

   
    tz_count = json_df['tz'].value_counts()

    
    json_df_tz.plot.bar()

   
    tokens_df = json_df['a'].str.split(n=1, expand=True).add_prefix("Token_")

    
    tokens_frequency = tokens_df['Token_0'].value_counts()

    
    tokens_frequency.head().plot.bar()

    
    tokens_df = tokens_df.replace(np.nan, 'Mising')

   
    tokens_df["os"] = 'Not Windows'

    
    tokens_df["os"][tokens_df["Token_1"].str.find("Windows") != -1] = "Windows"

except ValueError as e:
    print(e)

except AttributeError as e:
    print(e)

except TypeError as e:
    print(e)