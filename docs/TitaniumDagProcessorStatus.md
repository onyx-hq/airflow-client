# TitaniumDagProcessorStatus

The status and the latest dag processor heartbeat.  *New in version 2.6.3* 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**TitaniumTitaniumHealthStatus**](TitaniumHealthStatus.md) |  | [optional] 
**latest_dag_processor_heartbeat** | **str** | The time the dag processor last did a heartbeat. | [optional] [readonly] 

## Example

```python
from titanium_airflow_client.models.titanium_dag_processor_status import TitaniumDagProcessorStatus

# TODO update the JSON string below
json = "{}"
# create an instance of TitaniumDagProcessorStatus from a JSON string
titanium_dag_processor_status_instance = TitaniumDagProcessorStatus.from_json(json)
# print the JSON string representation of the object
print(TitaniumDagProcessorStatus.to_json())

# convert the object into a dict
titanium_dag_processor_status_dict = titanium_dag_processor_status_instance.to_dict()
# create an instance of TitaniumDagProcessorStatus from a dict
titanium_dag_processor_status_from_dict = TitaniumDagProcessorStatus.from_dict(titanium_dag_processor_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


