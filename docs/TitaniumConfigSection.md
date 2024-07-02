# TitaniumConfigSection

The section of configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] [readonly] 
**options** | [**List[TitaniumTitaniumConfigOption]**](TitaniumConfigOption.md) |  | [optional] 

## Example

```python
from titanium_airflow_client.models.titanium_config_section import TitaniumConfigSection

# TODO update the JSON string below
json = "{}"
# create an instance of TitaniumConfigSection from a JSON string
titanium_config_section_instance = TitaniumConfigSection.from_json(json)
# print the JSON string representation of the object
print(TitaniumConfigSection.to_json())

# convert the object into a dict
titanium_config_section_dict = titanium_config_section_instance.to_dict()
# create an instance of TitaniumConfigSection from a dict
titanium_config_section_from_dict = TitaniumConfigSection.from_dict(titanium_config_section_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


