# TitaniumQueuedEventCollection

A collection of Dataset Dag Run Queues.  *New in version 2.9.0* 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_entries** | **int** | Count of total objects in the current result set before pagination parameters (limit, offset) are applied.  | [optional] 
**datasets** | [**List[TitaniumTitaniumQueuedEvent]**](TitaniumQueuedEvent.md) |  | [optional] 

## Example

```python
from titanium_airflow_client.models.titanium_queued_event_collection import TitaniumQueuedEventCollection

# TODO update the JSON string below
json = "{}"
# create an instance of TitaniumQueuedEventCollection from a JSON string
titanium_queued_event_collection_instance = TitaniumQueuedEventCollection.from_json(json)
# print the JSON string representation of the object
print(TitaniumQueuedEventCollection.to_json())

# convert the object into a dict
titanium_queued_event_collection_dict = titanium_queued_event_collection_instance.to_dict()
# create an instance of TitaniumQueuedEventCollection from a dict
titanium_queued_event_collection_from_dict = TitaniumQueuedEventCollection.from_dict(titanium_queued_event_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


