# TitaniumTask

For details see: [airflow.models.baseoperator.BaseOperator](https://airflow.apache.org/docs/apache-airflow/stable/_api/airflow/models/baseoperator/index.html#airflow.models.baseoperator.BaseOperator) 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_ref** | [**TitaniumTitaniumClassReference**](TitaniumClassReference.md) |  | [optional] 
**task_id** | **str** |  | [optional] [readonly] 
**task_display_name** | **str** |  | [optional] [readonly] 
**owner** | **str** |  | [optional] [readonly] 
**start_date** | **datetime** |  | [optional] [readonly] 
**end_date** | **datetime** |  | [optional] [readonly] 
**trigger_rule** | [**TitaniumTitaniumTriggerRule**](TitaniumTriggerRule.md) |  | [optional] 
**extra_links** | [**List[TitaniumTitaniumTaskExtraLinksInner]**](TitaniumTaskExtraLinksInner.md) |  | [optional] [readonly] 
**depends_on_past** | **bool** |  | [optional] [readonly] 
**is_mapped** | **bool** |  | [optional] [readonly] 
**wait_for_downstream** | **bool** |  | [optional] [readonly] 
**retries** | **float** |  | [optional] [readonly] 
**queue** | **str** |  | [optional] [readonly] 
**pool** | **str** |  | [optional] [readonly] 
**pool_slots** | **float** |  | [optional] [readonly] 
**execution_timeout** | [**TitaniumTitaniumTimeDelta**](TitaniumTimeDelta.md) |  | [optional] 
**retry_delay** | [**TitaniumTitaniumTimeDelta**](TitaniumTimeDelta.md) |  | [optional] 
**retry_exponential_backoff** | **bool** |  | [optional] [readonly] 
**priority_weight** | **float** |  | [optional] [readonly] 
**weight_rule** | [**TitaniumTitaniumWeightRule**](TitaniumWeightRule.md) |  | [optional] 
**ui_color** | **str** | Color in hexadecimal notation. | [optional] 
**ui_fgcolor** | **str** | Color in hexadecimal notation. | [optional] 
**template_fields** | **List[str]** |  | [optional] [readonly] 
**sub_dag** | [**TitaniumTitaniumDAG**](TitaniumDAG.md) |  | [optional] 
**downstream_task_ids** | **List[str]** |  | [optional] [readonly] 

## Example

```python
from titanium_airflow_client.models.titanium_task import TitaniumTask

# TODO update the JSON string below
json = "{}"
# create an instance of TitaniumTask from a JSON string
titanium_task_instance = TitaniumTask.from_json(json)
# print the JSON string representation of the object
print(TitaniumTask.to_json())

# convert the object into a dict
titanium_task_dict = titanium_task_instance.to_dict()
# create an instance of TitaniumTask from a dict
titanium_task_from_dict = TitaniumTask.from_dict(titanium_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


