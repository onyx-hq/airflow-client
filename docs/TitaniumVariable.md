# TitaniumVariable

Full representation of Variable

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**description** | **str** | The description of the variable.  *New in version 2.4.0*  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from titanium_airflow_client.models.titanium_variable import TitaniumVariable

# TODO update the JSON string below
json = "{}"
# create an instance of TitaniumVariable from a JSON string
titanium_variable_instance = TitaniumVariable.from_json(json)
# print the JSON string representation of the object
print(TitaniumVariable.to_json())

# convert the object into a dict
titanium_variable_dict = titanium_variable_instance.to_dict()
# create an instance of TitaniumVariable from a dict
titanium_variable_from_dict = TitaniumVariable.from_dict(titanium_variable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


