# TitaniumTimeDelta

Time delta

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**days** | **int** |  | 
**seconds** | **int** |  | 
**microseconds** | **int** |  | 

## Example

```python
from titanium_airflow_client.models.titanium_time_delta import TitaniumTimeDelta

# TODO update the JSON string below
json = "{}"
# create an instance of TitaniumTimeDelta from a JSON string
titanium_time_delta_instance = TitaniumTimeDelta.from_json(json)
# print the JSON string representation of the object
print(TitaniumTimeDelta.to_json())

# convert the object into a dict
titanium_time_delta_dict = titanium_time_delta_instance.to_dict()
# create an instance of TitaniumTimeDelta from a dict
titanium_time_delta_from_dict = TitaniumTimeDelta.from_dict(titanium_time_delta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


