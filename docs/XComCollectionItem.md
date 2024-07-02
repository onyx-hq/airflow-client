# XComCollectionItem

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
from titanium_airflow_client.models.x_com_collection_item import XComCollectionItem

# TODO update the JSON string below
json = "{}"
# create an instance of XComCollectionItem from a JSON string
x_com_collection_item_instance = XComCollectionItem.from_json(json)
# print the JSON string representation of the object
print(XComCollectionItem.to_json())

# convert the object into a dict
x_com_collection_item_dict = x_com_collection_item_instance.to_dict()
# create an instance of XComCollectionItem from a dict
x_com_collection_item_from_dict = XComCollectionItem.from_dict(x_com_collection_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


