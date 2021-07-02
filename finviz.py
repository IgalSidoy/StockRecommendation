import requests




base_url = "https://finviz.com/"
sub_url_stock_details = "quote.ashx?"


params = {
  "t": "AA",
  "ty": "c",
  "p": "d",
  "b":"1"
}


params_res = ""
_del = "&"
for p in params:
    params_res+=p+'='+params[p]+_del
params_res = params_res[:-1]

url = base_url+sub_url_stock_details+params_res


headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}

x = requests.get(url, headers=headers)

encoding = 'utf-8'
response = x.content.decode(encoding)
result = response.split("<table")
data =result[12].split("<tr")
#--------------------data extraction-----------------------

#-------------------------------line 1 data
index = 1
_data = data[index].split("<td")
P_and_E = _data[4].split("><b>")[1].split("</b></td>")[0]
EPS_ttm = _data[6].split("><b>")[1].split("</b></td>")[0]
insider_Own = _data[8].split("><b>")[1].split("</b></td>")[0]
shares_outstanding=_data[10].split("><b>")[1].split("</b></td>")[0]
performance_week = _data[12].split("><b>")[1].split("</b></td>")[0]
#-------------------------------line 2 data
index = 2
_data = data[index].split("<td")
market_capitalization = _data[2].split("><b>")[1].split("</b></td>")[0]
forward_price_to_earnings=_data[4].split("><b>")[1].split("</b></td>")[0]
EPS_next_y = _data[6].split("><b>")[1].split("</b></td>")[0]
insider_transactions =_data[8].split("><b>")[1].split("</b></td>")[0]
shares_float = _data[10].split("><b>")[1].split("</b></td>")[0]
performance_month = _data[12].split("><b>")[1].split("</b></td>")[0]
#-------------------------------line 3 data
index = 3
_data = data[index].split("<td")
income_ttm = _data[2].split("><b>")[1].split("</b></td>")[0]
Price_to_Earnings_to_Growth=_data[4].split("><b>")[1].split("</b></td>")[0]
EPS_estimate_for_next_quarter = _data[6].split("><b>")[1].split("</b></td>")[0]
institutional_ownership =_data[8].split("><b>")[1].split("</b></td>")[0]
short_interest_share = _data[10].split("><b>")[1].split("</b></td>")[0]
performance_quarter = _data[12].split("><b>")[1].split("</b></td>")[0]
#-------------------------------line 4 data
index = 4
_data = data[index].split("<td")
revenue_ttm = _data[2].split("><b>")[1].split("</b></td>")[0]
price_to_sales_ttm=_data[4].split("><b>")[1].split("</b></td>")[0]
EPS_growth_this_year = _data[6].split("><b>")[1].split("</b></td>")[0]
institutional_transactions_3_months =_data[8].split("><b>")[1].split("</b></td>")[0]
short_interest_ratio = _data[10].split("><b>")[1].split("</b></td>")[0]
performance_half_year = _data[12].split("><b>")[1].split("</b></td>")[0]
#-------------------------------line 5 data
index = 5
_data = data[index].split("<td")
book_value_per_share_mrq = _data[2].split("><b>")[1].split("</b></td>")[0]
price_to_book_mrq=_data[4].split("><b>")[1].split("</b></td>")[0]
EPS_growth_next_year = _data[6].split("><b>")[1].split("</b></td>")[0]
return_on_assets_ttm =_data[8].split("><b>")[1].split("</b></td>")[0]
target_price = _data[10].split("><b>")[1].split("</b></td>")[0]
performance_year = _data[12].split("><b>")[1].split("</b></td>")[0]
#-------------------------------line 6 data
index = 6
_data = data[index].split("<td")
cash_per_share = _data[2].split("><b>")[1].split("</b></td>")[0]
price_to_ash_per_share_mrq=_data[4].split("><b>")[1].split("</b></td>")[0]
long_term_annual_growth_estimate = _data[6].split("><b>")[1].split("</b></td>")[0]
return_on_equity_ttm =_data[8].split("><b>")[1].split("</b></td>")[0]
_52_Week_trading_range = _data[10].split("><b>")[1].split("</b></td>")[0]
performance_year_to_date = _data[12].split("><b>")[1].split("</b></td>")[0]
#-------------------------------line 7 data
index = 7
_data = data[index].split("<td")
dividend_annual = _data[2].split("><b>")[1].split("</b></td>")[0]
price_to_free_cash_flow_ttm=_data[4].split("><b>")[1].split("</b></td>")[0]
EPS_past_5_years = _data[6].split("><b>")[1].split("</b></td>")[0]
return_on_investment_ttm =_data[8].split("><b>")[1].split("</b></td>")[0]
distance_from_52_week_high = _data[10].split("><b>")[1].split("</b></td>")[0]
beta = _data[12].split("><b>")[1].split("</b></td>")[0]
#-------------------------------line 8 data
index = 8
_data = data[index].split("<td")
dividend_yield_annual = _data[2].split("><b>")[1].split("</b></td>")[0]
quick_ratio_mrq=_data[4].split("><b>")[1].split("</b></td>")[0]
sales_past_5_years = _data[6].split("><b>")[1].split("</b></td>")[0]
gross_margin_ttm =_data[8].split("><b>")[1].split("</b></td>")[0]
distance_from_52_week_low = _data[10].split("><b>")[1].split("</b></td>")[0]
average_true_range_14 = _data[12].split("><b>")[1].split("</b></td>")[0]
#-------------------------------line 9 data
index = 9
_data = data[index].split("<td")
employees = _data[2].split("><b>")[1].split("</b></td>")[0]
current_ratio_mrq=_data[4].split("><b>")[1].split("</b></td>")[0]
quarterly_revenue_growth_yoy = _data[6].split("><b>")[1].split("</b></td>")[0]
operation_margin_ttm =_data[8].split("><b>")[1].split("</b></td>")[0]
relative_strength_index = _data[10].split("><b>")[1].split("</b></td>")[0]
volatility_week_month = _data[12].split("><b>")[1].split("</b></td>")[0]
#-------------------------------line 10 data
index = 10
_data = data[index].split("<td")
optionable = _data[2].split("><b>")[1].split("</b></td>")[0]
total_debt_to_equity =_data[4].split("><b>")[1].split("</b></td>")[0]
quarterly_earnings_growth_yoy = _data[6].split("><b>")[1].split("</b></td>")[0]
profit_margin =_data[8].split("><b>")[1].split("</b></td>")[0]
relative_volume= _data[10].split("><b>")[1].split("</b></td>")[0]
previous_close = _data[12].split("><b>")[1].split("</b></td>")[0]
#-------------------------------line 11 data
index = 11
_data = data[index].split("<td")
shortable = _data[2].split("><b>")[1].split("</b></td>")[0]
long_term_debt_to_equity_mrq =_data[4].split("><b>")[1].split("</b></td>")[0]
earnings_date = _data[6].split("><b>")[1].split("</b></td>")[0]
dividend_payout_ratio_ttm =_data[8].split("><b>")[1].split("</b></td>")[0]
average_volume_3_months= _data[10].split("><b>")[1].split("</b></td>")[0]
price = _data[12].split("><b>")[1].split("</b></td>")[0]
#-------------------------------line 12 data
index = 12
_data = data[index].split("<td")
analysts_mean_recommendation_1_buy_5_sell = _data[2].split("><b>")[1].split("</b></td>")[0]
SMA_20 =_data[4].split("><b>")[1].split("</b></td>")[0]
SMA50 = _data[6].split("><b>")[1].split("</b></td>")[0]
SMA200 =_data[8].split("><b>")[1].split("</b></td>")[0]
volume= _data[10].split("><b>")[1].split("</b></td>")[0]
change_today = _data[12].split("><b>")[1].split("</b></td>")[0]

result = {
  "P/E": P_and_E,
  "EPS(ttm)":EPS_ttm,
  "InsiderOwn":insider_Own,
  "SharesOutstanding":shares_outstanding,
  "Performance_Week":performance_week,
  "MarketCapitalization":market_capitalization,
  "Forward_P/E":forward_price_to_earnings,
  "EPS_Next_Year":EPS_next_y,
  "Insider_Transactions":insider_transactions,
  "Shares_Float":shares_float,
  "Performance_Month":performance_month,
  "Income(ttm)":income_ttm,
  "PEG":Price_to_Earnings_to_Growth,
  "EPS_Next_Quarter":EPS_estimate_for_next_quarter,
  "Institutional_Ownership":institutional_ownership,
  "Short_Float":short_interest_share,
  "Performance_Quarter":performance_quarter,
  "Sales":revenue_ttm,
  "P/S":price_to_sales_ttm,
  "EPS_This_Year":EPS_growth_this_year,
  "Inst_Trans":institutional_transactions_3_months,
  "Short_Ratio":short_interest_ratio,
  "Performance_Half_Year":performance_half_year,
  "Book/Share":book_value_per_share_mrq,
  "P/B":price_to_book_mrq,
  "EPS_Next_Year":EPS_growth_next_year,
  "Return_On_Assets_ttm":return_on_assets_ttm,
  "Target_Price":target_price,
  "Performance_Year":performance_year,
  "Cash/Share":cash_per_share,
  "P/C":price_to_ash_per_share_mrq,
  "EPS_Next_5Years":long_term_annual_growth_estimate,
  "return_on_equity_ttm":return_on_equity_ttm,
  "52W Range":_52_Week_trading_range,
  "Performance_Year_To_Date":performance_year_to_date,
  "Dividend_Annual":dividend_annual,
  "P/FCF":price_to_free_cash_flow_ttm,
  "EPS_Past_5_Years":EPS_past_5_years,
  "ROI":return_on_investment_ttm,
  "52W_High":distance_from_52_week_high,
  "Beta":beta,
  "Dividend_Yield_Annual":dividend_yield_annual,
  "Quick_Ratio":quick_ratio_mrq,
  "Sales_Past_5_Years":sales_past_5_years,
  "Gross_Margin_ttm":gross_margin_ttm,
  "52W_Low":distance_from_52_week_low,
  "ATR":average_true_range_14,
  "Employees":employees,
  "Current_Ratio":current_ratio_mrq,
  "Sales Q/Q":quarterly_revenue_growth_yoy,
  "Operation_Margin":operation_margin_ttm,
  "RSI_14":relative_strength_index,
  "Volatility_Week/Month":volatility_week_month,
  "Optionable":optionable,
  "Total_Debt_To_Equity":total_debt_to_equity,
  "EPS Q/Q":quarterly_earnings_growth_yoy,
  "Profit_Margin":profit_margin,
  "Relative_Volume":relative_volume,
  "Previous_Close":previous_close,
  "Shortable":shortable,
  "LT_Debt/Eq":long_term_debt_to_equity_mrq,  
  "Earnings_Date":earnings_date,
  "dividend_payout_ratio_ttm":dividend_payout_ratio_ttm,
  "Payout":dividend_payout_ratio_ttm,
  "Average_Volume_3_Months":average_volume_3_months,
  "Price":price,
  "Analysts' mean recommendation (1=Buy 5=Sell)":analysts_mean_recommendation_1_buy_5_sell,
  "SMA_20":SMA_20,
  "SMA50":SMA50,
  "SMA200":SMA50,
  "Volume":volume,
  "Change_Today":change_today
  }

#-------------------remove extra html tags
for item in result:
  if (len(result[item])>10):
    result[item] = result[item].split(">")[1].split("</span")[0]
    if "</small" in result[item]:
       result[item] = result[item].replace("</small","")

print(result)



