# TitaniumTaskOutletDatasetReference

A datasets reference to an upstream task.  *New in version 2.4.0* 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dag_id** | **str** | The DAG ID that updates the dataset. | [optional] 
**task_id** | **str** | The task ID that updates the dataset. | [optional] 
**created_at** | **str** | The dataset creation time | [optional] 
**updated_at** | **str** | The dataset update time | [optional] 

## Example

```python
from titanium_airflow_client.models.titanium_task_outlet_dataset_reference import TitaniumTaskOutletDatasetReference

# TODO update the JSON string below
json = "{}"
# create an instance of TitaniumTaskOutletDatasetReference from a JSON string
titanium_task_outlet_dataset_reference_instance = TitaniumTaskOutletDatasetReference.from_json(json)
# print the JSON string representation of the object
print(TitaniumTaskOutletDatasetReference.to_json())

# convert the object into a dict
titanium_task_outlet_dataset_reference_dict = titanium_task_outlet_dataset_reference_instance.to_dict()
# create an instance of TitaniumTaskOutletDatasetReference from a dict
titanium_task_outlet_dataset_reference_from_dict = TitaniumTaskOutletDatasetReference.from_dict(titanium_task_outlet_dataset_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


