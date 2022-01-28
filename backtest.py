import pyupbit
import numpy as np

# OHLCV = open, high, low, close, volume의 약자 (시가, 고가, 저가, 종가, 거래량)
df = pyupbit.get_ohlcv("KRW-BTC", count=10) # count의 정수는 며칠간의 시장을 분석할 것이냐에 대한 값임 .

# 변동폭 * k 계산, (고가 - 저가) *k 값  
df['range'] = (df['high'] - df['low']) * 0.5

# target(매수가), range 칼럼을 한칸씩 밑으로 내림 
df['target'] = df['open'] + df['range'].shift(1)

# ror(수익률), np.where(조건문, 참일때 값, 거짓일때 값)
df['ror'] = np.where(df['high'] > df['target'],
                     df['close'] / df['target'] ,
                     1)
# hpr = 누적수익률 
df['hpr'] = df['ror'].cumprod()

# dd = 하락폭 , Max dd = mdd = 최대 하락폭
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100
print("MDD(%): ", df['dd'].max())
df.to_excel("dd.xlsx")