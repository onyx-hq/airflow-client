# TitaniumImportErrorCollection

Collection of import errors.  *Changed in version 2.1.0*&#58; 'total_entries' field is added. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_entries** | **int** | Count of total objects in the current result set before pagination parameters (limit, offset) are applied.  | [optional] 
**import_errors** | [**List[TitaniumTitaniumImportError]**](TitaniumImportError.md) |  | [optional] 

## Example

```python
from titanium_airflow_client.models.titanium_import_error_collection import TitaniumImportErrorCollection

# TODO update the JSON string below
json = "{}"
# create an instance of TitaniumImportErrorCollection from a JSON string
titanium_import_error_collection_instance = TitaniumImportErrorCollection.from_json(json)
# print the JSON string representation of the object
print(TitaniumImportErrorCollection.to_json())

# convert the object into a dict
titanium_import_error_collection_dict = titanium_import_error_collection_instance.to_dict()
# create an instance of TitaniumImportErrorCollection from a dict
titanium_import_error_collection_from_dict = TitaniumImportErrorCollection.from_dict(titanium_import_error_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


