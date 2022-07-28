from email.policy import default
from urllib import response
from sherlock import sherlock
from sites import SitesInformation
from notify import QueryNotify
import os
import json 



def user_search(user):
    sites = SitesInformation(os.path.join(os.path.dirname(__file__), "resources/data.json"))
    site_data = {site.name: site.information for site in sites}
    query_notify = QueryNotify()
    data = sherlock(user, site_data, query_notify, timeout=2)
    new_dict = {k: [v['url_user'], v['http_status'],] for k, v in data.items()}
    new_new_dict = {}
    for k,v in new_dict.items():
        if v[1] == 200:
            new_new_dict.update({k: v[0]})
        


    # with open ('user_data.json', 'w') as write_file:
    #     write_file.write(json.dumps(new_new_dict, indent=2))
    #     write_file.close()

    return json.dumps(new_dict)
            

