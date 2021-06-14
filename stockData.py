import finnhub
import json
import statistics
from types import SimpleNamespace as Namespace

# Setup client
finnhub_client = finnhub.Client(api_key="bt7akff48v6ppe5o15d0")
def error(name,value):
    print(name + ' is ' + str(value))


def get_data_by_symbol(symbol):
    print('############################################################')
    res_data = finnhub_client.company_basic_financials(symbol,"all")
    symbol = res_data["symbol"]
    EPS    = res_data["metric"]["epsExclExtraItemsTTM"]
    #Fetch Forcast 3 years EPS
    EPS_3  = res_data["metric"]["epsGrowth3Y"]
    is_calculated = False
    if EPS_3 == None:
        is_calculated = True
        EPS_back_year = []
        EPS_back_year.append(res_data["series"]["annual"]["eps"][0]["v"])
        EPS_back_year.append(res_data["series"]["annual"]["eps"][1]["v"])
        EPS_back_year.append(res_data["series"]["annual"]["eps"][2]["v"])
        EPS_average = round(statistics.mean(EPS_back_year),4)
        EPS_3 = (EPS-EPS_average)
        EPS_3 = round(EPS_3/EPS_average,4)
    if is_calculated == False:
        EPS_3 = EPS_3/100+1

    #Fetch Forcast 5 years EPS
    is_calculated = False
    EPS_5  = res_data["metric"]["epsGrowth5Y"]
    if EPS_5 == None:
        is_calculated = True
        EPS_back_year = []
        EPS_back_year.append(res_data["series"]["annual"]["eps"][0]["v"])
        EPS_back_year.append(res_data["series"]["annual"]["eps"][1]["v"])
        EPS_back_year.append(res_data["series"]["annual"]["eps"][2]["v"])
        EPS_back_year.append(res_data["series"]["annual"]["eps"][3]["v"])
        EPS_back_year.append(res_data["series"]["annual"]["eps"][4]["v"])
        EPS_average = round(statistics.mean(EPS_back_year),4)
        EPS_5 = abs((EPS-EPS_average))
        EPS_5 = round(EPS_5/EPS_average,4)
    if is_calculated == False:
        EPS_5 = EPS_5/100+1

    PE     = res_data["metric"]["peExclExtraTTM"]
    if PE == None:
        error('PE',PE)
        exit()

    _intrinsicVal_3Y = round(EPS*EPS_3*PE,2)
    _intrinsicVal_5Y = round(EPS*EPS_5*PE,2)

 
    print('symbol ----------------------------|' + str(symbol))
    print('EPS -------------------------------|' + str(EPS))
    print('EPS_3 -----------------------------|' + str(EPS_3))
    print('EPS_5 -----------------------------|' + str(EPS_5))
    print('P/E -------------------------------|' + str(PE))
    print('IntrinsicVal 3 Year ---------------|$' + str(_intrinsicVal_3Y))
    print('IntrinsicVal 5 Year ---------------|$' + str(_intrinsicVal_5Y))
    exit()


    res_data = finnhub_client.quote(symbol) #-------> get quates http request.
    current_close_price = res_data["c"]

    gain_3Y = _intrinsicVal_3Y - current_close_price
    gain_5Y = _intrinsicVal_5Y - current_close_price
    gain_3Y =round(gain_3Y,2)
    gain_5Y =round(gain_5Y,2)

    gain_3Y_percent = current_close_price / _intrinsicVal_3Y 
    gain_5Y_percent = current_close_price / _intrinsicVal_5Y 

    gain_3Y_percent = round((1-gain_3Y_percent)*100,2)
    gain_5Y_percent = round((1-gain_5Y_percent)*100,2)


    print('current_close_price -------------- $'+str(current_close_price))
    print('gain_3Y -------------------------- $'+str(gain_3Y))
    print('gain_5Y -------------------------- $'+str(gain_5Y))
    print('gain_3Y_percent ------------------ %'+str(gain_3Y_percent))
    print('gain_5Y_percent ------------------ %'+str(gain_5Y_percent))
    print('############################################################')



def get_data_by_arr():
    symbols = ['F']
    for symbol in symbols:
        get_data_by_symbol(symbol)


get_data_by_arr()