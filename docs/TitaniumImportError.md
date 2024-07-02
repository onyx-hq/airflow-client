# TitaniumImportError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**import_error_id** | **int** | The import error ID. | [optional] [readonly] 
**timestamp** | **str** | The time when this error was created. | [optional] [readonly] 
**filename** | **str** | The filename | [optional] [readonly] 
**stack_trace** | **str** | The full stackstrace.. | [optional] [readonly] 

## Example

```python
from titanium_airflow_client.models.titanium_import_error import TitaniumImportError

# TODO update the JSON string below
json = "{}"
# create an instance of TitaniumImportError from a JSON string
titanium_import_error_instance = TitaniumImportError.from_json(json)
# print the JSON string representation of the object
print(TitaniumImportError.to_json())

# convert the object into a dict
titanium_import_error_dict = titanium_import_error_instance.to_dict()
# create an instance of TitaniumImportError from a dict
titanium_import_error_from_dict = TitaniumImportError.from_dict(titanium_import_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


