# 損益出場

def byProfit(price, x, cost, stop_limit):
    """
    根據損益點數，出清所有部位。

    Example:

        byProfit(price, 20, InPrice.max(), -1)    以成本最高者計算停損點
        byProfit(price, 20, get_open_price(), -1) 以開盤價計算停損點
        byProfit(price, 100, InPrice[-1] , 1)     以最新單計算停利點

    :param x: 損益點數
    :param cost: 成本計價方式(最新價、最高價、平均價、特定價格)
    :param stop_limit: 停損或停利(1/-1)
    :return: True/False 或應出場價格
    """

    profit = (price - cost) * Trade.dir

    if profit * stop_limit >= x:
        return(True) # or return(cost + x * stop_limit * Trade.dir)
    else:
        return(False)

# 時間出場
    
def byTime(day=0,hour=0,minute=0,second=0,spe_date_or_weekday,typee=1,in_time):
    """
    時間格式: 年(西元)月日時分秒 (特定日期或星期使用)
             ex. 20181002180605  (2018/10/02,18:06:05) (表特定日期)
             ex. 5  (表星期)
    根據時間，出清所有部位。
    
    :param day: 平倉距離進場的時長天數
    :param day: 平倉距離進場的時長時數
    :param day: 平倉距離進場的時長分鐘數
    :param day: 平倉距離進場的時長秒數
    注:前四者組合成一時間段
    :param spe_data_or_weekday: 特定日期或時間
    :param typee: 1: 採用距離時長法  
                  2: 採用特定時點法
    :param in_time: 進場時間
    
    """
    
    
    if typee == 1:
        
