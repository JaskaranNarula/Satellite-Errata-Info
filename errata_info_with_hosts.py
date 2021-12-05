"""
Date ......: 12/04/2021
Developer .: Waldirio <waldirio@gmail.com>|<waldirio@redhat.com>
             Jaskaran Narula <narula.jaskaran@gmail.com>|<janarula@redhat.com>
Purpose ...: Add the # of content hosts affected by the errata
License ...: GPL3
"""

import requests
import json
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# variable
USER = "admin"
PASSWORD = "changeme"
SATILLITE_FQDN = "satellite.example.com"
Params = {
          "errata_restrict_applicable": True,
          "errata_restrict_installable": False,
          "per_page": 10000,
         }


# drivercode
def main():
    """
    Funtion to make the API resquest as per the API metioned in URL variable below.
    APIs can be:
    1) /katello/api/errata (default)
    """
    URL = "https://" + SATILLITE_FQDN + "/katello/api/errata"
    response = requests.get(URL, Params, auth=HTTPBasicAuth(USER, PASSWORD), verify=False)
    data = json.loads(response.content)
    csv_file = open("/tmp/results.csv", "w")
    csv_file.write("id,errata_id,erratum_type,title,hosts_applicable_count,issued,updated" + "\n")
    for i in data['results']:
        erratum_list = ",".join([str(i['id']), i['errata_id'], i['title'], i['type'], str(i['hosts_applicable_count']), i['issued'], i['updated']])
        csv_file.write(erratum_list + "\n")
    csv_file.close()


if __name__ == "__main__":
    main()
