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
#TEAM_GOLD
#match_info = apimatch.json()    slot_s = start slot num.   slot_e = end slot num.
def get_totalgold(match_info,slot_s=0,slot_e=5):
    i=0
    j=0
    k=0
    for i in range(slot_s,slot_e):
        k=match_info['players'][i]['total_gold']
        j=j+k
    return j
