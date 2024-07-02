# TitaniumHealthInfo

Instance status information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadatabase** | [**TitaniumTitaniumMetadatabaseStatus**](TitaniumMetadatabaseStatus.md) |  | [optional] 
**scheduler** | [**TitaniumTitaniumSchedulerStatus**](TitaniumSchedulerStatus.md) |  | [optional] 
**triggerer** | [**TitaniumTitaniumTriggererStatus**](TitaniumTriggererStatus.md) |  | [optional] 
**dag_processor** | [**TitaniumTitaniumDagProcessorStatus**](TitaniumDagProcessorStatus.md) |  | [optional] 

## Example

```python
from titanium_airflow_client.models.titanium_health_info import TitaniumHealthInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TitaniumHealthInfo from a JSON string
titanium_health_info_instance = TitaniumHealthInfo.from_json(json)
# print the JSON string representation of the object
print(TitaniumHealthInfo.to_json())

# convert the object into a dict
titanium_health_info_dict = titanium_health_info_instance.to_dict()
# create an instance of TitaniumHealthInfo from a dict
titanium_health_info_from_dict = TitaniumHealthInfo.from_dict(titanium_health_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


