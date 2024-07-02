# TitaniumRoleCollection

A collection of roles.  *New in version 2.1.0* 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_entries** | **int** | Count of total objects in the current result set before pagination parameters (limit, offset) are applied.  | [optional] 
**roles** | [**List[TitaniumTitaniumRole]**](TitaniumRole.md) |  | [optional] 

## Example

```python
from titanium_airflow_client.models.titanium_role_collection import TitaniumRoleCollection

# TODO update the JSON string below
json = "{}"
# create an instance of TitaniumRoleCollection from a JSON string
titanium_role_collection_instance = TitaniumRoleCollection.from_json(json)
# print the JSON string representation of the object
print(TitaniumRoleCollection.to_json())

# convert the object into a dict
titanium_role_collection_dict = titanium_role_collection_instance.to_dict()
# create an instance of TitaniumRoleCollection from a dict
titanium_role_collection_from_dict = TitaniumRoleCollection.from_dict(titanium_role_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


