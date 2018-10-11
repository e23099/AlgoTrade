def byProfit(price, x, cost, direction, add_cut):
    profit = (price - cost) * direction
    if profit * add_cut >= x:
        return(True) # or return(cost + x * stop_limit * Trade.dir)
    return(False)

