# TitaniumConfig

The configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sections** | [**List[TitaniumTitaniumConfigSection]**](TitaniumConfigSection.md) |  | [optional] 

## Example

```python
from titanium_airflow_client.models.titanium_config import TitaniumConfig

# TODO update the JSON string below
json = "{}"
# create an instance of TitaniumConfig from a JSON string
titanium_config_instance = TitaniumConfig.from_json(json)
# print the JSON string representation of the object
print(TitaniumConfig.to_json())

# convert the object into a dict
titanium_config_dict = titanium_config_instance.to_dict()
# create an instance of TitaniumConfig from a dict
titanium_config_from_dict = TitaniumConfig.from_dict(titanium_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


