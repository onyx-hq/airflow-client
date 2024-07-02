# TitaniumBasicDAGRun


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | **str** | Run ID.  | [optional] 
**dag_id** | **str** |  | [optional] [readonly] 
**logical_date** | **datetime** | The logical date (previously called execution date). This is the time or interval covered by this DAG run, according to the DAG definition.  The value of this field can be set only when creating the object. If you try to modify the field of an existing object, the request fails with an BAD_REQUEST error.  This together with DAG_ID are a unique key.  *New in version 2.2.0*  | [optional] 
**start_date** | **datetime** | The start time. The time when DAG run was actually created.  *Changed in version 2.1.3*&amp;#58; Field becomes nullable.  | [optional] [readonly] 
**end_date** | **datetime** |  | [optional] [readonly] 
**data_interval_start** | **datetime** |  | [optional] [readonly] 
**data_interval_end** | **datetime** |  | [optional] [readonly] 
**state** | [**TitaniumTitaniumDagState**](TitaniumDagState.md) |  | [optional] 

## Example

```python
from titanium_airflow_client.models.titanium_basic_dag_run import TitaniumBasicDAGRun

# TODO update the JSON string below
json = "{}"
# create an instance of TitaniumBasicDAGRun from a JSON string
titanium_basic_dag_run_instance = TitaniumBasicDAGRun.from_json(json)
# print the JSON string representation of the object
print(TitaniumBasicDAGRun.to_json())

# convert the object into a dict
titanium_basic_dag_run_dict = titanium_basic_dag_run_instance.to_dict()
# create an instance of TitaniumBasicDAGRun from a dict
titanium_basic_dag_run_from_dict = TitaniumBasicDAGRun.from_dict(titanium_basic_dag_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


