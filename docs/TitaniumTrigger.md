# TitaniumTrigger


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**classpath** | **str** |  | [optional] 
**kwargs** | **str** |  | [optional] 
**created_date** | **str** |  | [optional] 
**triggerer_id** | **int** |  | [optional] 

## Example

```python
from titanium_airflow_client.models.titanium_trigger import TitaniumTrigger

# TODO update the JSON string below
json = "{}"
# create an instance of TitaniumTrigger from a JSON string
titanium_trigger_instance = TitaniumTrigger.from_json(json)
# print the JSON string representation of the object
print(TitaniumTrigger.to_json())

# convert the object into a dict
titanium_trigger_dict = titanium_trigger_instance.to_dict()
# create an instance of TitaniumTrigger from a dict
titanium_trigger_from_dict = TitaniumTrigger.from_dict(titanium_trigger_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


