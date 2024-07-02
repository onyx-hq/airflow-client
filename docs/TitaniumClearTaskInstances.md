# TitaniumClearTaskInstances


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dry_run** | **bool** | If set, don&#39;t actually run this operation. The response will contain a list of task instances planned to be cleaned, but not modified in any way.  | [optional] [default to True]
**task_ids** | **List[str]** | A list of task ids to clear.  *New in version 2.1.0*  | [optional] 
**start_date** | **str** | The minimum execution date to clear. | [optional] 
**end_date** | **str** | The maximum execution date to clear. | [optional] 
**only_failed** | **bool** | Only clear failed tasks. | [optional] [default to True]
**only_running** | **bool** | Only clear running tasks. | [optional] [default to False]
**include_subdags** | **bool** | Clear tasks in subdags and clear external tasks indicated by ExternalTaskMarker. | [optional] 
**include_parentdag** | **bool** | Clear tasks in the parent dag of the subdag. | [optional] 
**reset_dag_runs** | **bool** | Set state of DAG runs to RUNNING. | [optional] 
**dag_run_id** | **str** | The DagRun ID for this task instance | [optional] 
**include_upstream** | **bool** | If set to true, upstream tasks are also affected. | [optional] [default to False]
**include_downstream** | **bool** | If set to true, downstream tasks are also affected. | [optional] [default to False]
**include_future** | **bool** | If set to True, also tasks from future DAG Runs are affected. | [optional] [default to False]
**include_past** | **bool** | If set to True, also tasks from past DAG Runs are affected. | [optional] [default to False]

## Example

```python
from titanium_airflow_client.models.titanium_clear_task_instances import TitaniumClearTaskInstances

# TODO update the JSON string below
json = "{}"
# create an instance of TitaniumClearTaskInstances from a JSON string
titanium_clear_task_instances_instance = TitaniumClearTaskInstances.from_json(json)
# print the JSON string representation of the object
print(TitaniumClearTaskInstances.to_json())

# convert the object into a dict
titanium_clear_task_instances_dict = titanium_clear_task_instances_instance.to_dict()
# create an instance of TitaniumClearTaskInstances from a dict
titanium_clear_task_instances_from_dict = TitaniumClearTaskInstances.from_dict(titanium_clear_task_instances_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


