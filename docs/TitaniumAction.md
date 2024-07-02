# TitaniumAction

An action Item.  *New in version 2.1.0* 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the permission \&quot;action\&quot; | [optional] 

## Example

```python
from titanium_airflow_client.models.titanium_action import TitaniumAction

# TODO update the JSON string below
json = "{}"
# create an instance of TitaniumAction from a JSON string
titanium_action_instance = TitaniumAction.from_json(json)
# print the JSON string representation of the object
print(TitaniumAction.to_json())

# convert the object into a dict
titanium_action_dict = titanium_action_instance.to_dict()
# create an instance of TitaniumAction from a dict
titanium_action_from_dict = TitaniumAction.from_dict(titanium_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


