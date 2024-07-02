# TitaniumResource

A resource on which permissions are granted.  *New in version 2.1.0* 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the resource | [optional] 

## Example

```python
from titanium_airflow_client.models.titanium_resource import TitaniumResource

# TODO update the JSON string below
json = "{}"
# create an instance of TitaniumResource from a JSON string
titanium_resource_instance = TitaniumResource.from_json(json)
# print the JSON string representation of the object
print(TitaniumResource.to_json())

# convert the object into a dict
titanium_resource_dict = titanium_resource_instance.to_dict()
# create an instance of TitaniumResource from a dict
titanium_resource_from_dict = TitaniumResource.from_dict(titanium_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


