# TitaniumActionResource

The Action-Resource item.  *New in version 2.1.0* 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**TitaniumTitaniumAction**](.md) |  | [optional] 
**resource** | [**TitaniumTitaniumResource**](.md) |  | [optional] 

## Example

```python
from titanium_airflow_client.models.titanium_action_resource import TitaniumActionResource

# TODO update the JSON string below
json = "{}"
# create an instance of TitaniumActionResource from a JSON string
titanium_action_resource_instance = TitaniumActionResource.from_json(json)
# print the JSON string representation of the object
print(TitaniumActionResource.to_json())

# convert the object into a dict
titanium_action_resource_dict = titanium_action_resource_instance.to_dict()
# create an instance of TitaniumActionResource from a dict
titanium_action_resource_from_dict = TitaniumActionResource.from_dict(titanium_action_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


