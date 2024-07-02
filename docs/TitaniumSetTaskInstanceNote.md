# TitaniumSetTaskInstanceNote


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**note** | **str** | The custom note to set for this Task Instance. | 

## Example

```python
from titanium_airflow_client.models.titanium_set_task_instance_note import TitaniumSetTaskInstanceNote

# TODO update the JSON string below
json = "{}"
# create an instance of TitaniumSetTaskInstanceNote from a JSON string
titanium_set_task_instance_note_instance = TitaniumSetTaskInstanceNote.from_json(json)
# print the JSON string representation of the object
print(TitaniumSetTaskInstanceNote.to_json())

# convert the object into a dict
titanium_set_task_instance_note_dict = titanium_set_task_instance_note_instance.to_dict()
# create an instance of TitaniumSetTaskInstanceNote from a dict
titanium_set_task_instance_note_from_dict = TitaniumSetTaskInstanceNote.from_dict(titanium_set_task_instance_note_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


