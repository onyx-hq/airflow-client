# TitaniumDatasetEvent

A dataset event.  *New in version 2.4.0* 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset_id** | **int** | The dataset id | [optional] 
**dataset_uri** | **str** | The URI of the dataset | [optional] 
**extra** | **object** | The dataset event extra | [optional] 
**source_dag_id** | **str** | The DAG ID that updated the dataset. | [optional] 
**source_task_id** | **str** | The task ID that updated the dataset. | [optional] 
**source_run_id** | **str** | The DAG run ID that updated the dataset. | [optional] 
**source_map_index** | **int** | The task map index that updated the dataset. | [optional] 
**created_dagruns** | [**List[TitaniumTitaniumBasicDAGRun]**](TitaniumBasicDAGRun.md) |  | [optional] 
**timestamp** | **str** | The dataset event creation time | [optional] 

## Example

```python
from titanium_airflow_client.models.titanium_dataset_event import TitaniumDatasetEvent

# TODO update the JSON string below
json = "{}"
# create an instance of TitaniumDatasetEvent from a JSON string
titanium_dataset_event_instance = TitaniumDatasetEvent.from_json(json)
# print the JSON string representation of the object
print(TitaniumDatasetEvent.to_json())

# convert the object into a dict
titanium_dataset_event_dict = titanium_dataset_event_instance.to_dict()
# create an instance of TitaniumDatasetEvent from a dict
titanium_dataset_event_from_dict = TitaniumDatasetEvent.from_dict(titanium_dataset_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


