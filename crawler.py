# 2018 - 02 - 16
# Be made by Yoon Han Sol in Dankook Univ
# For machine Learning

def crawling(driver):
    conn=pymysql.connect(host='localhost', user='root', password='1313',db='upbit',charset='utf8')
    cur=conn.cursor()
    sql='insert into fluctuation value (%s,%s,%s,%s,%s,%s,%s,%s)'
    
    priceB=driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/section[1]/article[2]/span[2]/div[1]/span[1]/strong').text
    buyB=driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/section[1]/div/div[1]/article/span[2]/table/tbody/tr/td[2]').text
    sellB=driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/section[1]/div/div[1]/article/span[2]/table/tbody/tr/td[4]').text
    
    while 1:
        try:
            buy=driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/section[1]/div/div[1]/article/span[2]/table/tbody/tr/td[2]').text
            sell=driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/section[1]/div/div[1]/article/span[2]/table/tbody/tr/td[4]').text
            price=driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/section[1]/article[2]/span[2]/div[1]/span[1]/strong').text
        except Exception:
            continue
        
        if eq(buyB,buy)==False or eq(sellB,sell)==False or eq(priceB,price)==False :
            print(buy+"\t"+sell+"\t"+price.replace(',',''))
            pr=int(price.replace(',',''))
            bid=float(buy)
            offer=float(sell)
            d_now=datetime.today().strftime('%Y-%m-%d, %H:%M:%S')
            
            cur.execute(sql,(1,d_now,pr,bid,offer,pr/int(priceB.replace(',','')),bid/float(buyB),offer/float(sellB)))
            cur.connection.commit()
        
        buyB=buy
        sellB=sell
        priceB=price
        time.sleep(0.05)
    


if __name__=='__main__':
    from selenium import webdriver
    from operator import eq
    import time
    import pymysql
    from datetime import datetime
    
    driver = webdriver.Chrome('C:/Users/yhs/Documents/workspace/upbit_crawling/chromedriver.exe')
    driver.get('https://upbit.com/exchange?code=CRIX.UPBIT.KRW-BTC')
    time.sleep(10)
    
    crawling(driver)
    
