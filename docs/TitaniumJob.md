# TitaniumJob


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**dag_id** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**job_type** | **str** |  | [optional] 
**start_date** | **str** |  | [optional] 
**end_date** | **str** |  | [optional] 
**latest_heartbeat** | **str** |  | [optional] 
**executor_class** | **str** |  | [optional] 
**hostname** | **str** |  | [optional] 
**unixname** | **str** |  | [optional] 

## Example

```python
from titanium_airflow_client.models.titanium_job import TitaniumJob

# TODO update the JSON string below
json = "{}"
# create an instance of TitaniumJob from a JSON string
titanium_job_instance = TitaniumJob.from_json(json)
# print the JSON string representation of the object
print(TitaniumJob.to_json())

# convert the object into a dict
titanium_job_dict = titanium_job_instance.to_dict()
# create an instance of TitaniumJob from a dict
titanium_job_from_dict = TitaniumJob.from_dict(titanium_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


