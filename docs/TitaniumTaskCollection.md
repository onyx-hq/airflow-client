# TitaniumTaskCollection

Collection of tasks.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tasks** | [**List[TitaniumTitaniumTask]**](TitaniumTask.md) |  | [optional] 

## Example

```python
from titanium_airflow_client.models.titanium_task_collection import TitaniumTaskCollection

# TODO update the JSON string below
json = "{}"
# create an instance of TitaniumTaskCollection from a JSON string
titanium_task_collection_instance = TitaniumTaskCollection.from_json(json)
# print the JSON string representation of the object
print(TitaniumTaskCollection.to_json())

# convert the object into a dict
titanium_task_collection_dict = titanium_task_collection_instance.to_dict()
# create an instance of TitaniumTaskCollection from a dict
titanium_task_collection_from_dict = TitaniumTaskCollection.from_dict(titanium_task_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


