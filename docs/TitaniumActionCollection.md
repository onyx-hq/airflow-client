# TitaniumActionCollection

A collection of actions.  *New in version 2.1.0* 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_entries** | **int** | Count of total objects in the current result set before pagination parameters (limit, offset) are applied.  | [optional] 
**actions** | [**List[TitaniumTitaniumAction]**](TitaniumAction.md) |  | [optional] 

## Example

```python
from titanium_airflow_client.models.titanium_action_collection import TitaniumActionCollection

# TODO update the JSON string below
json = "{}"
# create an instance of TitaniumActionCollection from a JSON string
titanium_action_collection_instance = TitaniumActionCollection.from_json(json)
# print the JSON string representation of the object
print(TitaniumActionCollection.to_json())

# convert the object into a dict
titanium_action_collection_dict = titanium_action_collection_instance.to_dict()
# create an instance of TitaniumActionCollection from a dict
titanium_action_collection_from_dict = TitaniumActionCollection.from_dict(titanium_action_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


