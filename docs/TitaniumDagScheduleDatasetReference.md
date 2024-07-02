# TitaniumDagScheduleDatasetReference

A datasets reference to a downstream DAG.  *New in version 2.4.0* 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dag_id** | **str** | The DAG ID that depends on the dataset. | [optional] 
**created_at** | **str** | The dataset reference creation time | [optional] 
**updated_at** | **str** | The dataset reference update time | [optional] 

## Example

```python
from titanium_airflow_client.models.titanium_dag_schedule_dataset_reference import TitaniumDagScheduleDatasetReference

# TODO update the JSON string below
json = "{}"
# create an instance of TitaniumDagScheduleDatasetReference from a JSON string
titanium_dag_schedule_dataset_reference_instance = TitaniumDagScheduleDatasetReference.from_json(json)
# print the JSON string representation of the object
print(TitaniumDagScheduleDatasetReference.to_json())

# convert the object into a dict
titanium_dag_schedule_dataset_reference_dict = titanium_dag_schedule_dataset_reference_instance.to_dict()
# create an instance of TitaniumDagScheduleDatasetReference from a dict
titanium_dag_schedule_dataset_reference_from_dict = TitaniumDagScheduleDatasetReference.from_dict(titanium_dag_schedule_dataset_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


