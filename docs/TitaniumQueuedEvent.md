# TitaniumQueuedEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uri** | **str** | The datata uri. | [optional] 
**dag_id** | **str** | The DAG ID. | [optional] 
**created_at** | **datetime** | The creation time of QueuedEvent | [optional] 

## Example

```python
from titanium_airflow_client.models.titanium_queued_event import TitaniumQueuedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of TitaniumQueuedEvent from a JSON string
titanium_queued_event_instance = TitaniumQueuedEvent.from_json(json)
# print the JSON string representation of the object
print(TitaniumQueuedEvent.to_json())

# convert the object into a dict
titanium_queued_event_dict = titanium_queued_event_instance.to_dict()
# create an instance of TitaniumQueuedEvent from a dict
titanium_queued_event_from_dict = TitaniumQueuedEvent.from_dict(titanium_queued_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


