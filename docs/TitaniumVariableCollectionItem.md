# TitaniumVariableCollectionItem

XCom entry collection item. The value field are only available when retrieving a single object due to the sensitivity of this data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**description** | **str** | The description of the variable.  *New in version 2.4.0*  | [optional] 

## Example

```python
from titanium_airflow_client.models.titanium_variable_collection_item import TitaniumVariableCollectionItem

# TODO update the JSON string below
json = "{}"
# create an instance of TitaniumVariableCollectionItem from a JSON string
titanium_variable_collection_item_instance = TitaniumVariableCollectionItem.from_json(json)
# print the JSON string representation of the object
print(TitaniumVariableCollectionItem.to_json())

# convert the object into a dict
titanium_variable_collection_item_dict = titanium_variable_collection_item_instance.to_dict()
# create an instance of TitaniumVariableCollectionItem from a dict
titanium_variable_collection_item_from_dict = TitaniumVariableCollectionItem.from_dict(titanium_variable_collection_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


