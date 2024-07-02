# TitaniumClearDagRun


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dry_run** | **bool** | If set, don&#39;t actually run this operation. The response will contain a list of task instances planned to be cleaned, but not modified in any way.  | [optional] [default to True]

## Example

```python
from titanium_airflow_client.models.titanium_clear_dag_run import TitaniumClearDagRun

# TODO update the JSON string below
json = "{}"
# create an instance of TitaniumClearDagRun from a JSON string
titanium_clear_dag_run_instance = TitaniumClearDagRun.from_json(json)
# print the JSON string representation of the object
print(TitaniumClearDagRun.to_json())

# convert the object into a dict
titanium_clear_dag_run_dict = titanium_clear_dag_run_instance.to_dict()
# create an instance of TitaniumClearDagRun from a dict
titanium_clear_dag_run_from_dict = TitaniumClearDagRun.from_dict(titanium_clear_dag_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


