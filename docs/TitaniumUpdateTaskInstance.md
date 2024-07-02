# TitaniumUpdateTaskInstance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dry_run** | **bool** | If set, don&#39;t actually run this operation. The response will contain the task instance planned to be affected, but won&#39;t be modified in any way.  | [optional] [default to True]
**new_state** | [**TitaniumTitaniumUpdateTaskState**](TitaniumUpdateTaskState.md) |  | [optional] 

## Example

```python
from titanium_airflow_client.models.titanium_update_task_instance import TitaniumUpdateTaskInstance

# TODO update the JSON string below
json = "{}"
# create an instance of TitaniumUpdateTaskInstance from a JSON string
titanium_update_task_instance_instance = TitaniumUpdateTaskInstance.from_json(json)
# print the JSON string representation of the object
print(TitaniumUpdateTaskInstance.to_json())

# convert the object into a dict
titanium_update_task_instance_dict = titanium_update_task_instance_instance.to_dict()
# create an instance of TitaniumUpdateTaskInstance from a dict
titanium_update_task_instance_from_dict = TitaniumUpdateTaskInstance.from_dict(titanium_update_task_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


