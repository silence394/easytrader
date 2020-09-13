import easytrader
import sys
import time

argname = 'ht_client_liaolong.json'

if len(sys.argv) > 1:
    argname = sys.argv[1]

path = 'D:/MyGits/trader/huataitrader/'

argname = path + argname

user = easytrader.use('ht_client')

user.prepare(argname)

# user.position

# user.auto_ipo()
# user.auto_ipo_kzz()
ret = user.ipo_KZZ()
print(argname, ret)

time.sleep(10)
user.exit()
# user.today_trades


