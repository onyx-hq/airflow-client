# TitaniumUpdateDagRunState

Modify the state of a DAG run.  *New in version 2.2.0* 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | The state to set this DagRun | [optional] 

## Example

```python
from titanium_airflow_client.models.titanium_update_dag_run_state import TitaniumUpdateDagRunState

# TODO update the JSON string below
json = "{}"
# create an instance of TitaniumUpdateDagRunState from a JSON string
titanium_update_dag_run_state_instance = TitaniumUpdateDagRunState.from_json(json)
# print the JSON string representation of the object
print(TitaniumUpdateDagRunState.to_json())

# convert the object into a dict
titanium_update_dag_run_state_dict = titanium_update_dag_run_state_instance.to_dict()
# create an instance of TitaniumUpdateDagRunState from a dict
titanium_update_dag_run_state_from_dict = TitaniumUpdateDagRunState.from_dict(titanium_update_dag_run_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


