def single_break_through(input_value, upper_bound=None, lower_bound=None):
    """
    single break through: 單一指標突破
    input根據其他function生成。
    接著比較upper_bound以及lower_bound回傳做多、做空以及不作為。

    :param input_value: 根據不同策略生成
    :param upper_bound: 上界
    :param lower_bound: 下界
    :return: [-1(做空), 0(不作為), 1(做多)]
    """

    if (upper_bound is not None) and (input_value > upper_bound):
        return 1

    elif (lower_bound is not None) and (input_value < lower_bound):
        return -1

    else:
        return 0


