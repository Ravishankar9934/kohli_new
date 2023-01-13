import pandas as pd

df = pd.read_csv('dataset.csv')

print(df)

"""
Output
Runs   BF  4s  6s  ...  Inns     Opposition         Ground  Start Date
0      12   22   1   0  ...     1    v Sri Lanka       Dambulla   18-Aug-08
1      37   67   6   0  ...     2    v Sri Lanka       Dambulla   20-Aug-08
2      25   38   4   0  ...     1    v Sri Lanka  Colombo (RPS)   24-Aug-08
3      54   66   7   0  ...     1    v Sri Lanka  Colombo (RPS)   27-Aug-08
4      31   46   3   1  ...     2    v Sri Lanka  Colombo (RPS)   29-Aug-08
..    ...  ...  ..  ..  ...   ...            ...            ...         ...
127    45   51   2   1  ...     2  v New Zealand         Ranchi   26-Oct-16
128    65   76   2   1  ...     1  v New Zealand  Visakhapatnam   29-Oct-16
129   122  105   8   5  ...     2      v England           Pune   15-Jan-17
130     8    5   2   0  ...     1      v England        Cuttack   19-Jan-17
131    55   63   8   0  ...     2      v England        Kolkata   22-Jan-17
"""