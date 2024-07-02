# TitaniumProvider

The provider  *New in version 2.1.0* 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**package_name** | **str** | The package name of the provider. | [optional] 
**description** | **str** | The description of the provider. | [optional] 
**version** | **str** | The version of the provider. | [optional] 

## Example

```python
from titanium_airflow_client.models.titanium_provider import TitaniumProvider

# TODO update the JSON string below
json = "{}"
# create an instance of TitaniumProvider from a JSON string
titanium_provider_instance = TitaniumProvider.from_json(json)
# print the JSON string representation of the object
print(TitaniumProvider.to_json())

# convert the object into a dict
titanium_provider_dict = titanium_provider_instance.to_dict()
# create an instance of TitaniumProvider from a dict
titanium_provider_from_dict = TitaniumProvider.from_dict(titanium_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


