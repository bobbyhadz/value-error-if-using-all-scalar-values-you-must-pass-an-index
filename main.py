# ValueError: If using all scalar values, you must pass index

import pandas as pd

df = pd.DataFrame({
    'A': [50],
    'B': [100],
    'C': [150]
})

print(df)