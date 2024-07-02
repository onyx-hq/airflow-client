# TitaniumConfigOption

The option of configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] [readonly] 
**value** | **str** |  | [optional] [readonly] 

## Example

```python
from titanium_airflow_client.models.titanium_config_option import TitaniumConfigOption

# TODO update the JSON string below
json = "{}"
# create an instance of TitaniumConfigOption from a JSON string
titanium_config_option_instance = TitaniumConfigOption.from_json(json)
# print the JSON string representation of the object
print(TitaniumConfigOption.to_json())

# convert the object into a dict
titanium_config_option_dict = titanium_config_option_instance.to_dict()
# create an instance of TitaniumConfigOption from a dict
titanium_config_option_from_dict = TitaniumConfigOption.from_dict(titanium_config_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


