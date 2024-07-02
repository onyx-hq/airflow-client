# TitaniumSLAMiss


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** | The task ID. | [optional] [readonly] 
**dag_id** | **str** | The DAG ID. | [optional] 
**execution_date** | **str** |  | [optional] 
**email_sent** | **bool** |  | [optional] 
**timestamp** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**notification_sent** | **bool** |  | [optional] 

## Example

```python
from titanium_airflow_client.models.titanium_sla_miss import TitaniumSLAMiss

# TODO update the JSON string below
json = "{}"
# create an instance of TitaniumSLAMiss from a JSON string
titanium_sla_miss_instance = TitaniumSLAMiss.from_json(json)
# print the JSON string representation of the object
print(TitaniumSLAMiss.to_json())

# convert the object into a dict
titanium_sla_miss_dict = titanium_sla_miss_instance.to_dict()
# create an instance of TitaniumSLAMiss from a dict
titanium_sla_miss_from_dict = TitaniumSLAMiss.from_dict(titanium_sla_miss_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


