# RoleCollection

A collection of roles.  *New in version 2.1.0* 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_entries** | **int** | Count of total objects in the current result set before pagination parameters (limit, offset) are applied.  | [optional] 
**roles** | [**List[Role]**](Role.md) |  | [optional] 

## Example

```python
from titanium_airflow_client.models.role_collection import RoleCollection

# TODO update the JSON string below
json = "{}"
# create an instance of RoleCollection from a JSON string
role_collection_instance = RoleCollection.from_json(json)
# print the JSON string representation of the object
print(RoleCollection.to_json())

# convert the object into a dict
role_collection_dict = role_collection_instance.to_dict()
# create an instance of RoleCollection from a dict
role_collection_from_dict = RoleCollection.from_dict(role_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


