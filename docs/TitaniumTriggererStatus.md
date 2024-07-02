# TitaniumTriggererStatus

The status and the latest triggerer heartbeat.  *New in version 2.6.2* 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**TitaniumTitaniumHealthStatus**](TitaniumHealthStatus.md) |  | [optional] 
**latest_triggerer_heartbeat** | **str** | The time the triggerer last did a heartbeat. | [optional] [readonly] 

## Example

```python
from titanium_airflow_client.models.titanium_triggerer_status import TitaniumTriggererStatus

# TODO update the JSON string below
json = "{}"
# create an instance of TitaniumTriggererStatus from a JSON string
titanium_triggerer_status_instance = TitaniumTriggererStatus.from_json(json)
# print the JSON string representation of the object
print(TitaniumTriggererStatus.to_json())

# convert the object into a dict
titanium_triggerer_status_dict = titanium_triggerer_status_instance.to_dict()
# create an instance of TitaniumTriggererStatus from a dict
titanium_triggerer_status_from_dict = TitaniumTriggererStatus.from_dict(titanium_triggerer_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


