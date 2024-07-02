# TitaniumVariableCollection

Collection of variables.  *Changed in version 2.1.0*&#58; 'total_entries' field is added. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_entries** | **int** | Count of total objects in the current result set before pagination parameters (limit, offset) are applied.  | [optional] 
**variables** | [**List[TitaniumTitaniumVariableCollectionItem]**](TitaniumVariableCollectionItem.md) |  | [optional] 

## Example

```python
from titanium_airflow_client.models.titanium_variable_collection import TitaniumVariableCollection

# TODO update the JSON string below
json = "{}"
# create an instance of TitaniumVariableCollection from a JSON string
titanium_variable_collection_instance = TitaniumVariableCollection.from_json(json)
# print the JSON string representation of the object
print(TitaniumVariableCollection.to_json())

# convert the object into a dict
titanium_variable_collection_dict = titanium_variable_collection_instance.to_dict()
# create an instance of TitaniumVariableCollection from a dict
titanium_variable_collection_from_dict = TitaniumVariableCollection.from_dict(titanium_variable_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


