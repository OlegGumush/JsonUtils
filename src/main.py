import null as null

from models.subnet import *
from models.configuration import *
from src.utils.json_utils import *

subnet1_obj = Subnet("172.18.0.93", "mySubnet1", "aa:aa:bb:bb:cc:cc:dd:dd")
subnet2_obj = CloudSubnet("172.18.0.93", "mySubnet1", "aa:aa:bb:bb:cc:cc:dd:dd", "123123123")

print(to_json(subnet1_obj))
print(to_dict(subnet1_obj))

print(to_json(subnet2_obj))
print(to_dict(subnet2_obj))

print(dict_to_json(to_dict(subnet2_obj)))
print(json_to_dict(to_json(subnet2_obj)))

print(contains(to_dict(subnet1_obj), to_dict(subnet2_obj)))
print(contains(to_dict(subnet2_obj), to_dict(subnet1_obj)))

some_cloud_response = {'ip': '172.18.0.93', 'name': 'mySubnet1', 'mac': 'aa:aa:bb:bb:cc:cc:dd:dd', 'bla': None}

print(contains(to_dict(subnet1_obj), some_cloud_response))
print(contains(some_cloud_response, to_dict(subnet1_obj)))

subnets = []
subnets.append(Subnet("172.18.0.93", "mySubnet1", "aa:aa:bb:bb:cc:cc:dd:dd"))
subnets.append(Subnet("172.18.0.93", "mySubnet2", "aa:aa:bb:bb:cc:cc:dd:dd"))
subnets.append(Subnet("172.18.0.93", "mySubnet3", "aa:aa:bb:bb:cc:cc:dd:dd"))

configuration = Configuration("John", 9000, subnets)

print(to_dict(configuration))
print(to_json(configuration))

result_from_sensor = [{'ip': '172.18.0.93', 'name': 'mySubnet1', 'mac': 'aa:aa:bb:bb:cc:cc:dd:dd'},
                      {'ip': '172.18.0.93', 'name': 'mySubnet2', 'mac': 'aa:aa:bb:bb:cc:cc:dd:dd'},
                      {'ip': '172.18.0.93', 'name': 'mySubnet3', 'mac': 'aa:aa:bb:bb:cc:cc:dd:dd'}]

expected = Subnet("172.18.0.93", "mySubnet1", "aa:aa:bb:bb:cc:cc:dd:dd")

for subnet in configuration.subnet_list:
    print(contains(to_dict(expected), to_dict(subnet)))
