# TitaniumTaskInstanceCollection

Collection of task instances.  *Changed in version 2.1.0*&#58; 'total_entries' field is added. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_entries** | **int** | Count of total objects in the current result set before pagination parameters (limit, offset) are applied.  | [optional] 
**task_instances** | [**List[TitaniumTitaniumTaskInstance]**](TitaniumTaskInstance.md) |  | [optional] 

## Example

```python
from titanium_airflow_client.models.titanium_task_instance_collection import TitaniumTaskInstanceCollection

# TODO update the JSON string below
json = "{}"
# create an instance of TitaniumTaskInstanceCollection from a JSON string
titanium_task_instance_collection_instance = TitaniumTaskInstanceCollection.from_json(json)
# print the JSON string representation of the object
print(TitaniumTaskInstanceCollection.to_json())

# convert the object into a dict
titanium_task_instance_collection_dict = titanium_task_instance_collection_instance.to_dict()
# create an instance of TitaniumTaskInstanceCollection from a dict
titanium_task_instance_collection_from_dict = TitaniumTaskInstanceCollection.from_dict(titanium_task_instance_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


