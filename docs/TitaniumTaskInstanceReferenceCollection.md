# TitaniumTaskInstanceReferenceCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_instances** | [**List[TitaniumTitaniumTaskInstanceReference]**](TitaniumTaskInstanceReference.md) |  | [optional] 

## Example

```python
from titanium_airflow_client.models.titanium_task_instance_reference_collection import TitaniumTaskInstanceReferenceCollection

# TODO update the JSON string below
json = "{}"
# create an instance of TitaniumTaskInstanceReferenceCollection from a JSON string
titanium_task_instance_reference_collection_instance = TitaniumTaskInstanceReferenceCollection.from_json(json)
# print the JSON string representation of the object
print(TitaniumTaskInstanceReferenceCollection.to_json())

# convert the object into a dict
titanium_task_instance_reference_collection_dict = titanium_task_instance_reference_collection_instance.to_dict()
# create an instance of TitaniumTaskInstanceReferenceCollection from a dict
titanium_task_instance_reference_collection_from_dict = TitaniumTaskInstanceReferenceCollection.from_dict(titanium_task_instance_reference_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


