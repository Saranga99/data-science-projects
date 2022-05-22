def up_trend(cur_price, price_trigger, stock):       ### Check up trend
    if cur_price[-1] > price_trigger:
        print(f"{stock} " + "in Trigger and cut up ",price_trigger,"$")
        return 1
    else: return 0


def down_trend(cur_price, price_trigger, stock):    ### Check down trend
    if cur_price[-1] < price_trigger:
        print(f"{stock} " + "in Trigger and cut down ",price_trigger,"$")
        return 1
    else: return 0
