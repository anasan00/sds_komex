Workaround for pytrends 

# getting cookie
session = requests.Session()
session.get('https://trends.google.com')
cookies_map = session.cookies.get_dict()
nid_cookie = cookies_map['NID']

# creating an instance of the TrendReq class
pytrends = TrendReq(hl='en-US', tz=-60, 
                    requests_args={'headers': {'Cookie': f'NID={nid_cookie}'}})