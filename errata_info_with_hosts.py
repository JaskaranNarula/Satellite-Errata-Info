"""
Date ......: 12/04/2021
Developer .: Waldirio <waldirio@gmail.com>|<waldirio@redhat.com>
             Jaskaran Narula <narula.jaskaran@gmail.com>|<janarula@redhat.com>
Purpose ...: Add the # of content hosts affected by the errata
License ...: GPL3
"""

import csv
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

    stage_list = []
    final_list = []

    stage_list.append("id")
    stage_list.append("errata_id")
    stage_list.append("erratum_type")
    stage_list.append("title")
    stage_list.append("hosts_applicable_count")
    stage_list.append("hosts_installable_count")
    stage_list.append("issued")
    stage_list.append("updated")
    stage_list.append("reboot_suggested")

    final_list.append(stage_list)
    stage_list = []

    for element in data['results']:
        stage_list.append(element['id'])
        stage_list.append(element['errata_id'])
        stage_list.append(element['type'])
        stage_list.append(element['title'])
        stage_list.append(element['hosts_applicable_count'])
        stage_list.append(element['hosts_available_count'])
        stage_list.append(element['issued'])
        stage_list.append(element['updated'])
        stage_list.append(element['reboot_suggested'])

        final_list.append(stage_list)
        stage_list = []


    with open("/tmp/results.csv", "w") as csv_file:
        writer = csv.writer(csv_file)
        for lines in final_list:
            writer.writerow(lines)

    print("Please, check the file '/tmp/results.csv'")

if __name__ == "__main__":
    main()
