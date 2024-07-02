# TitaniumEventLogCollection

Collection of event logs.  *Changed in version 2.1.0*&#58; 'total_entries' field is added. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_entries** | **int** | Count of total objects in the current result set before pagination parameters (limit, offset) are applied.  | [optional] 
**event_logs** | [**List[TitaniumTitaniumEventLog]**](TitaniumEventLog.md) |  | [optional] 

## Example

```python
from titanium_airflow_client.models.titanium_event_log_collection import TitaniumEventLogCollection

# TODO update the JSON string below
json = "{}"
# create an instance of TitaniumEventLogCollection from a JSON string
titanium_event_log_collection_instance = TitaniumEventLogCollection.from_json(json)
# print the JSON string representation of the object
print(TitaniumEventLogCollection.to_json())

# convert the object into a dict
titanium_event_log_collection_dict = titanium_event_log_collection_instance.to_dict()
# create an instance of TitaniumEventLogCollection from a dict
titanium_event_log_collection_from_dict = TitaniumEventLogCollection.from_dict(titanium_event_log_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


