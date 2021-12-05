# Satellite Errata Info

The main idea of this script is to generate a csv errata report as in Satellite webUI, including the # of affected content hosts (applicable erratas).


## How to use this script. 

1. Download the python scripts to any desired directory or on your Red Hat Satellite 6.7 or later.

2. Add the admin creds of the satellite admin user to the script under the variables:
~~~
USER = "admin"
PASSWORD = "changme"
SATILLITE_FQDN = "satellite.example.com"
~~~

3. The Applicablity and Installabilty can be changed as per your wish.
- By-default Red Hat Satellite has "per_page" set to "1000" which can be changed. 
~~~
Params = {
          "errata_restrict_applicable":True,     
          "errata_restrict_installable":False,
          "per_page":10000,
         }
~~~

4. Run the scripts as below.

#### Usage
~~~
# python3 errata_info_with_hosts.py
~~~

# Examples
~~~
```
# cat /tmp/results.csv
id,errata_id,erratum_type,title,count,issued,updated
4906,RHSA-2021:4904,security,Critical: nss security update,1,2021-12-01,2021-12-01
4915,RHBA-2021:4789,bugfix,kbd bug fix and enhancement update,2,2021-11-23,2021-11-23
4913,RHBA-2021:4794,bugfix,gettext bug fix and enhancement update,2,2021-11-23,2021-11-23
...
```
~~~


# Authors 
~~~
Developer.: Jaskaran Singh Narula 
Mentor    : Waldirio
~~~ 
