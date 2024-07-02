# TitaniumSchedulerStatus

The status and the latest scheduler heartbeat.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**TitaniumTitaniumHealthStatus**](TitaniumHealthStatus.md) |  | [optional] 
**latest_scheduler_heartbeat** | **str** | The time the scheduler last did a heartbeat. | [optional] [readonly] 

## Example

```python
from titanium_airflow_client.models.titanium_scheduler_status import TitaniumSchedulerStatus

# TODO update the JSON string below
json = "{}"
# create an instance of TitaniumSchedulerStatus from a JSON string
titanium_scheduler_status_instance = TitaniumSchedulerStatus.from_json(json)
# print the JSON string representation of the object
print(TitaniumSchedulerStatus.to_json())

# convert the object into a dict
titanium_scheduler_status_dict = titanium_scheduler_status_instance.to_dict()
# create an instance of TitaniumSchedulerStatus from a dict
titanium_scheduler_status_from_dict = TitaniumSchedulerStatus.from_dict(titanium_scheduler_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


