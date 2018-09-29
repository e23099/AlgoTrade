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
