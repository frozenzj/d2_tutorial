import requests

def get_api_json(url):
    try:
        r = requests.get(url, timeout=3)
        r_json = r.json()
        return r_json
    except:
        return get_api_json(url)

if __name__ == '__main__':
    pass
def get_ran_match_id(limi=1):
    
#    def ransql(limi=1):
        sql='''select matches.match_id
        from matches
        order by random()
        limit %s'''%(limi)
#        return sql
        r=requests.get('https://api.opendota.com/api/explorer?sql={}'.format(sql))
        r_json=r.json()
        rMi=r_json['rows']
        return rMi
