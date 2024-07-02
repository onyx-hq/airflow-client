# TitaniumTaskInstance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** |  | [optional] 
**task_display_name** | **str** | Human centric display text for the task.  *New in version 2.9.0*  | [optional] 
**dag_id** | **str** |  | [optional] 
**dag_run_id** | **str** | The DagRun ID for this task instance  *New in version 2.3.0*  | [optional] 
**execution_date** | **str** |  | [optional] 
**start_date** | **str** |  | [optional] 
**end_date** | **str** |  | [optional] 
**duration** | **float** |  | [optional] 
**state** | [**TitaniumTitaniumTaskState**](TitaniumTaskState.md) |  | [optional] 
**try_number** | **int** |  | [optional] 
**map_index** | **int** |  | [optional] 
**max_tries** | **int** |  | [optional] 
**hostname** | **str** |  | [optional] 
**unixname** | **str** |  | [optional] 
**pool** | **str** |  | [optional] 
**pool_slots** | **int** |  | [optional] 
**queue** | **str** |  | [optional] 
**priority_weight** | **int** |  | [optional] 
**operator** | **str** | *Changed in version 2.1.1*&amp;#58; Field becomes nullable.  | [optional] 
**queued_when** | **str** | The datetime that the task enter the state QUEUE, also known as queue_at  | [optional] 
**pid** | **int** |  | [optional] 
**executor_config** | **str** |  | [optional] 
**sla_miss** | [**TitaniumTitaniumSLAMiss**](TitaniumSLAMiss.md) |  | [optional] 
**rendered_map_index** | **str** | Rendered name of an expanded task instance, if the task is mapped.  *New in version 2.9.0*  | [optional] 
**rendered_fields** | **object** | JSON object describing rendered fields.  *New in version 2.3.0*  | [optional] 
**trigger** | [**TitaniumTitaniumTrigger**](TitaniumTrigger.md) |  | [optional] 
**triggerer_job** | [**TitaniumTitaniumJob**](TitaniumJob.md) |  | [optional] 
**note** | **str** | Contains manually entered notes by the user about the TaskInstance.  *New in version 2.5.0*  | [optional] 

## Example

```python
from titanium_airflow_client.models.titanium_task_instance import TitaniumTaskInstance

# TODO update the JSON string below
json = "{}"
# create an instance of TitaniumTaskInstance from a JSON string
titanium_task_instance_instance = TitaniumTaskInstance.from_json(json)
# print the JSON string representation of the object
print(TitaniumTaskInstance.to_json())

# convert the object into a dict
titanium_task_instance_dict = titanium_task_instance_instance.to_dict()
# create an instance of TitaniumTaskInstance from a dict
titanium_task_instance_from_dict = TitaniumTaskInstance.from_dict(titanium_task_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


