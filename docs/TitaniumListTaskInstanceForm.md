# TitaniumListTaskInstanceForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dag_ids** | **List[str]** | Return objects with specific DAG IDs. The value can be repeated to retrieve multiple matching values (OR condition). | [optional] 
**dag_run_ids** | **List[str]** | Return objects with specific DAG Run IDs. The value can be repeated to retrieve multiple matching values (OR condition). *New in version 2.7.1* | [optional] 
**task_ids** | **List[str]** | Return objects with specific task IDs. The value can be repeated to retrieve multiple matching values (OR condition). *New in version 2.7.1* | [optional] 
**execution_date_gte** | **datetime** | Returns objects greater or equal to the specified date.  This can be combined with execution_date_lte parameter to receive only the selected period.  | [optional] 
**execution_date_lte** | **datetime** | Returns objects less than or equal to the specified date.  This can be combined with execution_date_gte parameter to receive only the selected period.  | [optional] 
**start_date_gte** | **datetime** | Returns objects greater or equal the specified date.  This can be combined with start_date_lte parameter to receive only the selected period.  | [optional] 
**start_date_lte** | **datetime** | Returns objects less or equal the specified date.  This can be combined with start_date_gte parameter to receive only the selected period.  | [optional] 
**end_date_gte** | **datetime** | Returns objects greater or equal the specified date.  This can be combined with start_date_lte parameter to receive only the selected period.  | [optional] 
**end_date_lte** | **datetime** | Returns objects less than or equal to the specified date.  This can be combined with start_date_gte parameter to receive only the selected period.  | [optional] 
**duration_gte** | **float** | Returns objects greater than or equal to the specified values.  This can be combined with duration_lte parameter to receive only the selected period.  | [optional] 
**duration_lte** | **float** | Returns objects less than or equal to the specified values.  This can be combined with duration_gte parameter to receive only the selected range.  | [optional] 
**state** | [**List[TitaniumTitaniumTaskState]**](TitaniumTaskState.md) | The value can be repeated to retrieve multiple matching values (OR condition). | [optional] 
**pool** | **List[str]** | The value can be repeated to retrieve multiple matching values (OR condition). | [optional] 
**queue** | **List[str]** | The value can be repeated to retrieve multiple matching values (OR condition). | [optional] 

## Example

```python
from titanium_airflow_client.models.titanium_list_task_instance_form import TitaniumListTaskInstanceForm

# TODO update the JSON string below
json = "{}"
# create an instance of TitaniumListTaskInstanceForm from a JSON string
titanium_list_task_instance_form_instance = TitaniumListTaskInstanceForm.from_json(json)
# print the JSON string representation of the object
print(TitaniumListTaskInstanceForm.to_json())

# convert the object into a dict
titanium_list_task_instance_form_dict = titanium_list_task_instance_form_instance.to_dict()
# create an instance of TitaniumListTaskInstanceForm from a dict
titanium_list_task_instance_form_from_dict = TitaniumListTaskInstanceForm.from_dict(titanium_list_task_instance_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


