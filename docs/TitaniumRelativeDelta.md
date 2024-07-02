# TitaniumRelativeDelta

Relative delta

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**years** | **int** |  | 
**months** | **int** |  | 
**days** | **int** |  | 
**leapdays** | **int** |  | 
**hours** | **int** |  | 
**minutes** | **int** |  | 
**seconds** | **int** |  | 
**microseconds** | **int** |  | 
**year** | **int** |  | 
**month** | **int** |  | 
**day** | **int** |  | 
**hour** | **int** |  | 
**minute** | **int** |  | 
**second** | **int** |  | 
**microsecond** | **int** |  | 

## Example

```python
from titanium_airflow_client.models.titanium_relative_delta import TitaniumRelativeDelta

# TODO update the JSON string below
json = "{}"
# create an instance of TitaniumRelativeDelta from a JSON string
titanium_relative_delta_instance = TitaniumRelativeDelta.from_json(json)
# print the JSON string representation of the object
print(TitaniumRelativeDelta.to_json())

# convert the object into a dict
titanium_relative_delta_dict = titanium_relative_delta_instance.to_dict()
# create an instance of TitaniumRelativeDelta from a dict
titanium_relative_delta_from_dict = TitaniumRelativeDelta.from_dict(titanium_relative_delta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


