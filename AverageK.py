import pyupbit
import numpy as np


def get_ror(k=0.5):
    df = pyupbit.get_ohlcv("KRW-DOGE", count=100)
    df['range'] = (df['high'] - df['low']) * k
    df['target'] = df['open'] + df['range'].shift(1)

    df['ror'] = np.where(df['high'] > df['target'],
                         df['close'] / df['target'] ,
                         1)

    ror = df['ror'].cumprod()[-2]
    return ror


for k in np.arange(0.3, 0.8, 0.01): # 0.1 부터 1.0까지 0.001씩 증가 시켜서 ror을 보여줌. 
    ror = get_ror(k)
    print("%.3f %f" % (k, ror))
