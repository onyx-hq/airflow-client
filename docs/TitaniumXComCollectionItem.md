# TitaniumXComCollectionItem

XCom entry collection item.  The value field is only available when reading a single object due to the size of the value. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**timestamp** | **str** |  | [optional] 
**execution_date** | **str** |  | [optional] 
**map_index** | **int** |  | [optional] 
**task_id** | **str** |  | [optional] 
**dag_id** | **str** |  | [optional] 

## Example

```python
from titanium_airflow_client.models.titanium_x_com_collection_item import TitaniumXComCollectionItem

# TODO update the JSON string below
json = "{}"
# create an instance of TitaniumXComCollectionItem from a JSON string
titanium_x_com_collection_item_instance = TitaniumXComCollectionItem.from_json(json)
# print the JSON string representation of the object
print(TitaniumXComCollectionItem.to_json())

# convert the object into a dict
titanium_x_com_collection_item_dict = titanium_x_com_collection_item_instance.to_dict()
# create an instance of TitaniumXComCollectionItem from a dict
titanium_x_com_collection_item_from_dict = TitaniumXComCollectionItem.from_dict(titanium_x_com_collection_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


