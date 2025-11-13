from pytrends.request import TrendReq
import pandas as pd

def get_custom_trends():
    pytrends = TrendReq(hl="en-US", tz=0)
    # Aqui você pode definir uma lista de tópicos específicos
    kw_list = ["Python", "YouTube", "Gaming"]
    pytrends.build_payload(kw_list, timeframe='now 7-d')
    data = pytrends.interest_over_time()
    return data.fillna(0).to_dict()

