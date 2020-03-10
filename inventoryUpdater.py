from datetime import datetime
noww=datetime.now()
import pandas as pd
import requests
import time
Products = pd.read_csv('http://users.metu.edu.tr/e216801/input.txt', sep="\t")
tx=pd.DataFrame(columns=['sku','price','minimum-seller-allowed-price','maximum-seller-allowed-price','quantity'])

for sk,prCode in zip(Products['seller-sku'],Products['asin1']):
    stat=1
    while stat==1:
        url='https://www.amazon.com/dp/'+prCode
        cook={
            'csm-hit':'tb:s-H3S6ARXV362CPRT826JE|1579712457922&t:1579712461853&adb:adblk_no',
            'i18n-prefs':'USD',
            'session-id':'137-0128695-8361860',
            'session-id-time':'2082787201l',
            'session-token':'KIUqpWOEt/CeS2mXMN6Jr23SPTB+RKVYCqYsjVJ3pz5K1nPXY9vFOizt9yIEMCQv3zzV54O2vldO2bLan2mctAYKF44HWV+ZcUvgu4C8agxYfBssWvrbZmvEapxiNLFYTM9uPh+a4/axIDfw2x90DzkuyBFrfGo73uUF6e8jn55cFC9v/3s3DjykLZx/8ruy1+qz7PpE6vSYVRSHTbycNuGUegM4qLBOp71orGaeYtPuAmkZZWcRLh7sZG8S90Ep',
            'sp-cdn':'"L5Z9:CA"',
            'ubid-main':'131-6721994-0471151',
            'x-wl-uid':'1LxhrZLPfosfFWGwg/89bEtUOXNk3g08EHOYMnMAPDdZrNCVwcuy2ymuOxPNpM9E1QxE+aK9b2Lw='
        }

        headers = {
            'Referer': 'http://www.amazon.com',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
            'X-Requested-With':'XMLHttpRequest'
        }
        data=requests.get(url,headers=headers,cookies=cook)
        a=data.text
        print(len(a))
        if len(a)>100000:
            stat=0
        else:
            time.sleep(50)
    q=a.find('a-size-base a-color-base',1)
    w=a.find('a-size-base a-color-base',q+1)
    e=a.find('a-size-base a-color-base',w+1)
    r=a.find('a-size-base a-color-base',e+1)
    out=a[r:]
    st=out.find('>')
    fn=out.find('<')
    TotalPrice=out[st+3:fn-1]
    try:
        TotalPrice=float(TotalPrice)

        cap=1.4*TotalPrice*1.15*1.3*1.02
        capmin=1.4*TotalPrice*1.15*1.15
        capmax=1.4*TotalPrice*1.15*1.8
        stat=a.find('a-size-medium a-color-success')
        if stat>5:
            stock=20
        else:
            ind=a.find('left in stock')
            stock=int(a[ind-3:ind])
            if stock<10:
                stock=0
    except:
        TotalPrice=300
        cap=1.4*TotalPrice*1.15*1.3
        capmin=1.4*TotalPrice*1.15*1.15
        capmax=1.4*TotalPrice*1.15*1.8
        stock=0
    print(sk,cap,stock)


    tx=tx.append({'sku':sk,'price':cap,'minimum-seller-allowed-price':capmin,'maximum-seller-allowed-price':capmax,'quantity':stock},ignore_index=True)

tx=tx.round(2)
tx.to_csv('/var/www/html/output.txt', index=None, sep='\t', mode='a')
thenn=datetime.now()
print(thenn-noww)
