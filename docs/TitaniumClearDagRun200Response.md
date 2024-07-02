# TitaniumClearDagRun200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dag_run_id** | **str** | Run ID.  The value of this field can be set only when creating the object. If you try to modify the field of an existing object, the request fails with an BAD_REQUEST error.  If not provided, a value will be generated based on execution_date.  If the specified dag_run_id is in use, the creation request fails with an ALREADY_EXISTS error.  This together with DAG_ID are a unique key.  | [optional] 
**dag_id** | **str** |  | [optional] [readonly] 
**logical_date** | **datetime** | The logical date (previously called execution date). This is the time or interval covered by this DAG run, according to the DAG definition.  The value of this field can be set only when creating the object. If you try to modify the field of an existing object, the request fails with an BAD_REQUEST error.  This together with DAG_ID are a unique key.  *New in version 2.2.0*  | [optional] 
**execution_date** | **datetime** | The execution date. This is the same as logical_date, kept for backwards compatibility. If both this field and logical_date are provided but with different values, the request will fail with an BAD_REQUEST error.  *Changed in version 2.2.0*&amp;#58; Field becomes nullable.  *Deprecated since version 2.2.0*&amp;#58; Use &#39;logical_date&#39; instead.  | [optional] 
**start_date** | **datetime** | The start time. The time when DAG run was actually created.  *Changed in version 2.1.3*&amp;#58; Field becomes nullable.  | [optional] [readonly] 
**end_date** | **datetime** |  | [optional] [readonly] 
**data_interval_start** | **datetime** | The beginning of the interval the DAG run covers.  | [optional] 
**data_interval_end** | **datetime** | The end of the interval the DAG run covers.  | [optional] 
**last_scheduling_decision** | **datetime** |  | [optional] [readonly] 
**run_type** | **str** |  | [optional] [readonly] 
**state** | [**TitaniumTitaniumDagState**](TitaniumDagState.md) |  | [optional] 
**external_trigger** | **bool** |  | [optional] [readonly] 
**conf** | **object** | JSON object describing additional configuration parameters.  The value of this field can be set only when creating the object. If you try to modify the field of an existing object, the request fails with an BAD_REQUEST error.  | [optional] 
**note** | **str** | Contains manually entered notes by the user about the DagRun.  *New in version 2.5.0*  | [optional] 
**task_instances** | [**List[TitaniumTitaniumTaskInstance]**](TitaniumTaskInstance.md) |  | [optional] 
**total_entries** | **int** | Count of total objects in the current result set before pagination parameters (limit, offset) are applied.  | [optional] 

## Example

```python
from titanium_airflow_client.models.titanium_clear_dag_run200_response import TitaniumClearDagRun200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TitaniumClearDagRun200Response from a JSON string
titanium_clear_dag_run200_response_instance = TitaniumClearDagRun200Response.from_json(json)
# print the JSON string representation of the object
print(TitaniumClearDagRun200Response.to_json())

# convert the object into a dict
titanium_clear_dag_run200_response_dict = titanium_clear_dag_run200_response_instance.to_dict()
# create an instance of TitaniumClearDagRun200Response from a dict
titanium_clear_dag_run200_response_from_dict = TitaniumClearDagRun200Response.from_dict(titanium_clear_dag_run200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


