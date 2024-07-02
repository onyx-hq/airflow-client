# TitaniumRole

a role item.  *New in version 2.1.0* 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the role  *Changed in version 2.3.0*&amp;#58; A minimum character length requirement (&#39;minLength&#39;) is added.  | [optional] 
**actions** | [**List[TitaniumTitaniumActionResource]**](TitaniumActionResource.md) |  | [optional] 

## Example

```python
from titanium_airflow_client.models.titanium_role import TitaniumRole

# TODO update the JSON string below
json = "{}"
# create an instance of TitaniumRole from a JSON string
titanium_role_instance = TitaniumRole.from_json(json)
# print the JSON string representation of the object
print(TitaniumRole.to_json())

# convert the object into a dict
titanium_role_dict = titanium_role_instance.to_dict()
# create an instance of TitaniumRole from a dict
titanium_role_from_dict = TitaniumRole.from_dict(titanium_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


