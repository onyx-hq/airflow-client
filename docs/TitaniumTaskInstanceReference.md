# TitaniumTaskInstanceReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** | The task ID. | [optional] [readonly] 
**dag_id** | **str** | The DAG ID. | [optional] [readonly] 
**execution_date** | **str** |  | [optional] [readonly] 
**dag_run_id** | **str** | The DAG run ID. | [optional] [readonly] 

## Example

```python
from titanium_airflow_client.models.titanium_task_instance_reference import TitaniumTaskInstanceReference

# TODO update the JSON string below
json = "{}"
# create an instance of TitaniumTaskInstanceReference from a JSON string
titanium_task_instance_reference_instance = TitaniumTaskInstanceReference.from_json(json)
# print the JSON string representation of the object
print(TitaniumTaskInstanceReference.to_json())

# convert the object into a dict
titanium_task_instance_reference_dict = titanium_task_instance_reference_instance.to_dict()
# create an instance of TitaniumTaskInstanceReference from a dict
titanium_task_instance_reference_from_dict = TitaniumTaskInstanceReference.from_dict(titanium_task_instance_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


