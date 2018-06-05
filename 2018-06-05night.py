import requests
def get_ran_match_id(limi=1):

#    def ransql(limi=1):
    i=0
    rec=[]
    sql='''select matches.match_id
    from matches
    order by random()
    limit %s'''%(limi)
#        return sql
    r=requests.get('https://api.opendota.com/api/explorer?sql={}'.format(sql))
    r_json=r.json()
    rMi=r_json['rows']
#        return rMi
    for i in range(len(rMi)):
        rec.append(rMi[i]['match_id'])
    return rec
