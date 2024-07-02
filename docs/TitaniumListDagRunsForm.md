# TitaniumListDagRunsForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_by** | **str** | The name of the field to order the results by. Prefix a field name with &#x60;-&#x60; to reverse the sort order.  *New in version 2.1.0*  | [optional] 
**page_offset** | **int** | The number of items to skip before starting to collect the result set. | [optional] 
**page_limit** | **int** | The numbers of items to return. | [optional] [default to 100]
**dag_ids** | **List[str]** | Return objects with specific DAG IDs. The value can be repeated to retrieve multiple matching values (OR condition). | [optional] 
**states** | **List[str]** | Return objects with specific states. The value can be repeated to retrieve multiple matching values (OR condition). | [optional] 
**execution_date_gte** | **datetime** | Returns objects greater or equal to the specified date.  This can be combined with execution_date_lte key to receive only the selected period.  | [optional] 
**execution_date_lte** | **datetime** | Returns objects less than or equal to the specified date.  This can be combined with execution_date_gte key to receive only the selected period.  | [optional] 
**start_date_gte** | **datetime** | Returns objects greater or equal the specified date.  This can be combined with start_date_lte key to receive only the selected period.  | [optional] 
**start_date_lte** | **datetime** | Returns objects less or equal the specified date.  This can be combined with start_date_gte parameter to receive only the selected period  | [optional] 
**end_date_gte** | **datetime** | Returns objects greater or equal the specified date.  This can be combined with end_date_lte parameter to receive only the selected period.  | [optional] 
**end_date_lte** | **datetime** | Returns objects less than or equal to the specified date.  This can be combined with end_date_gte parameter to receive only the selected period.  | [optional] 

## Example

```python
from titanium_airflow_client.models.titanium_list_dag_runs_form import TitaniumListDagRunsForm

# TODO update the JSON string below
json = "{}"
# create an instance of TitaniumListDagRunsForm from a JSON string
titanium_list_dag_runs_form_instance = TitaniumListDagRunsForm.from_json(json)
# print the JSON string representation of the object
print(TitaniumListDagRunsForm.to_json())

# convert the object into a dict
titanium_list_dag_runs_form_dict = titanium_list_dag_runs_form_instance.to_dict()
# create an instance of TitaniumListDagRunsForm from a dict
titanium_list_dag_runs_form_from_dict = TitaniumListDagRunsForm.from_dict(titanium_list_dag_runs_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


