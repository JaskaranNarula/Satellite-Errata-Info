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
# wget https://raw.githubusercontent.com/JaskaranNarula/Satellite-Errata-Info/main/errata_info_with_hosts.py
# python3 errata_info_with_hosts.py
~~~

# Examples
~~~
```
# cat /tmp/results.csv
id,errata_id,erratum_type,title,hosts_applicable_count,hosts_installable_count,issued,updated,reboot_suggested
4906,RHSA-2021:4904,security,Critical: nss security update,1,1,2021-12-01,2021-12-01,False
4915,RHBA-2021:4789,bugfix,kbd bug fix and enhancement update,2,2,2021-11-23,2021-11-23,False
4913,RHBA-2021:4794,bugfix,gettext bug fix and enhancement update,2,2,2021-11-23,2021-11-23,False
4912,RHSA-2021:4788,security,Moderate: krb5 security update,2,2,2021-11-23,2021-11-23,False
4910,RHBA-2021:4786,bugfix,subscription-manager bug fix and enhancement update,2,2,2021-11-23,2021-11-23,False
4907,RHBA-2021:4790,bugfix,bash bug fix and enhancement update,2,2,2021-11-23,2021-11-23,False
4905,RHBA-2021:4784,bugfix,bind bug fix and enhancement update,2,2,2021-11-23,2021-11-23,False
4903,RHBA-2021:4797,bugfix,qemu-kvm bug fix and enhancement update,1,1,2021-11-23,2021-11-23,False
4902,RHSA-2021:4782,security,Moderate: openssh security update,2,2,2021-11-23,2021-11-23,False
...
```
~~~


# Authors 
~~~
Developer.: Jaskaran Singh Narula 
Mentor    : Waldirio M Pinheiro
~~~ 
