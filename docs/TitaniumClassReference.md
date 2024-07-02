# TitaniumClassReference

Class reference

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**module_path** | **str** |  | [optional] [readonly] 
**class_name** | **str** |  | [optional] [readonly] 

## Example

```python
from titanium_airflow_client.models.titanium_class_reference import TitaniumClassReference

# TODO update the JSON string below
json = "{}"
# create an instance of TitaniumClassReference from a JSON string
titanium_class_reference_instance = TitaniumClassReference.from_json(json)
# print the JSON string representation of the object
print(TitaniumClassReference.to_json())

# convert the object into a dict
titanium_class_reference_dict = titanium_class_reference_instance.to_dict()
# create an instance of TitaniumClassReference from a dict
titanium_class_reference_from_dict = TitaniumClassReference.from_dict(titanium_class_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


