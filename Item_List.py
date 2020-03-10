from pyzabbix.api import ZabbixAPI
import json

zabbix = {}
with open(f'conf.json', 'r') as confs:
    zabbix = json.loads(confs.read())

try:
    zapi = ZabbixAPI(url=zabbix['url'], user=zabbix['username'], password=zabbix['password'])
    print ('Auth Ok!')
except Exception as err:
    print('Erro ao conectar ao Zabbix')
    print('Erro: {}'.format(err))

getHostGroup = zapi.do_request('item.get',
                            {
                                "filter": {
                                    "state": 1
                                },
                                "output": [
                                    "hostid",
                                    "name",
                                    "itemid"
                                ],
                                "monitored": True
                            }
                        )
i=0
for item in getHostGroup["result"]:
    i += 1
    print(f"Item {i} --> {item}")