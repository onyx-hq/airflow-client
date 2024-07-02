# Action

An action Item.  *New in version 2.1.0* 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the permission \&quot;action\&quot; | [optional] 

## Example

```python
from titanium_airflow_client.models.action import Action

# TODO update the JSON string below
json = "{}"
# create an instance of Action from a JSON string
action_instance = Action.from_json(json)
# print the JSON string representation of the object
print(Action.to_json())

# convert the object into a dict
action_dict = action_instance.to_dict()
# create an instance of Action from a dict
action_from_dict = Action.from_dict(action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

