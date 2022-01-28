import pyupbit

# 로그인 코드 
access = "mpaED5oiKQDkhIIvweKOTH9WsnbIjywou7MCTCec"          
secret = "veqYfo2ZVNFxYYex0hS5nsYXpGRspxnmyqpPfUCq"          
upbit = pyupbit.Upbit(access, secret)

# 잔고 조회 
print(upbit.get_balance("KRW-BTC"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회