# TitaniumConnection

Full representation of the connection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_id** | **str** | The connection ID. | [optional] 
**conn_type** | **str** | The connection type. | [optional] 
**description** | **str** | The description of the connection. | [optional] 
**host** | **str** | Host of the connection. | [optional] 
**login** | **str** | Login of the connection. | [optional] 
**var_schema** | **str** | Schema of the connection. | [optional] 
**port** | **int** | Port of the connection. | [optional] 
**password** | **str** | Password of the connection. | [optional] 
**extra** | **str** | Other values that cannot be put into another field, e.g. RSA keys. | [optional] 

## Example

```python
from titanium_airflow_client.models.titanium_connection import TitaniumConnection

# TODO update the JSON string below
json = "{}"
# create an instance of TitaniumConnection from a JSON string
titanium_connection_instance = TitaniumConnection.from_json(json)
# print the JSON string representation of the object
print(TitaniumConnection.to_json())

# convert the object into a dict
titanium_connection_dict = titanium_connection_instance.to_dict()
# create an instance of TitaniumConnection from a dict
titanium_connection_from_dict = TitaniumConnection.from_dict(titanium_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


