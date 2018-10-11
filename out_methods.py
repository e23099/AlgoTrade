# 損益出場

def byProfit(price, x, cost, direction, stop_limit):
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

    profit = (price - cost) * direction

    if profit * stop_limit >= x:
        return(True) # or return(cost + x * stop_limit * Trade.dir)
    else:
        return(False)

# 時間出場
    
def byTime(day=0,hour=0,minute=0,second=0,spe_date_or_weekday,typee=1,in_time):
    """
    時間格式: 年(西元)/月/日/星期/時/分/秒 (特定日期或星期使用)
             ex. 2018/10/02/0/18/06/05             
             ex. 0000/00/00/2/00/00/00  (表星期)
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
        in_Time=in_time.split("/")
        int_in_time=[]
        for row in in_Time:
            k=int(row)
            int_in_time.append(k)
        out_time=[]
        out_time.append(int_in_time[0])
        out_time.append(int_in_time[1])
        out_time.append(int_in_time[2]+day)
        out_time.append(0)
        out_time.append(int_in_time[4]+hour)
        out_time.append(int_in_time[5]+minute)
        out_time.append(int_in_time[6]+second)
        if out_time[6] >= 60:
            out_time[6] = out_time[6] - 60
            out_time[5] = out_time[5] + 1
        if out_time[5] >= 60:
            out_time[5] = out_time[6] - 60
            out_time[4] = out_time[5] + 1
        if out_time[4] >= 24:
            out_time[4] = out_time[6] - 24
            out_time[2] = out_time[5] + 1
        if out_time[2] >= 30 and (out_time[1] in [2,4,6,9,11] ) :
            out_time[2] = out_time[2] - 30
            out_time[1] = out_time[1] + 1
        elif out_time[2] >= 31 and (out_time[1] in [1,3,5,7,8,10,12] ) :
            out_time[2] = out_time[2] - 31
            out_time[1] = out_time[1] + 1
        if out_time[1] >= 12:
            out_time[1] = out_time[1] - 12
            out_time[0] = out_time[0] + 1
        time=time.split("/")
        int_time=[]
        for row in time:
            k=int(row)
            int_time.append(k)
        if int_time == out_time :
            return True
    if typee == 2:
        spe_date_or_weekday=spe_date_or_weekday.split("/")
        int_spe_date_or_weekday=[]
        for row in spe_date_or_weekday:
            k=int(row)
            int_spe_date_or_weekday.append(k)
        time=time.split("/")
        int_time=[]
        for row in time:
            k=int(row)
            int_time.append(k)
        if int_spe_date_or_weekday == int_time :
            return True
        if int_spe_data_or_weekday[3] == int_time[3] :
            return True

def single_reverse(direction, in_method, args):
    """
    in_method : 採用的進場方法(回傳值須為-1,0,1)
    args      : 進場方法所需的參數，以一個 () 或 [] 傳入所有參數

    當訊號出現不作為(0)或是與方向相反的結果(1/-1)時，平倉出場

    """
    if direction * in_method(*args) <= 0:
        return True
    return False