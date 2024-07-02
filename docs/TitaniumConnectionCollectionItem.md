# TitaniumConnectionCollectionItem

Connection collection item. The password and extra fields are only available when retrieving a single object due to the sensitivity of this data. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_id** | **str** | The connection ID. | [optional] 
**conn_type** | **str** | The connection type. | [optional] 
**description** | **str** | The description of the connection. | [optional] 
**host** | **str** | Host of the connection. | [optional] 
**login** | **str** | Login of the connection. | [optional] 
**var_schema** | **str** | Schema of the connection. | [optional] 
**port** | **int** | Port of the connection. | [optional] 

## Example

```python
from titanium_airflow_client.models.titanium_connection_collection_item import TitaniumConnectionCollectionItem

# TODO update the JSON string below
json = "{}"
# create an instance of TitaniumConnectionCollectionItem from a JSON string
titanium_connection_collection_item_instance = TitaniumConnectionCollectionItem.from_json(json)
# print the JSON string representation of the object
print(TitaniumConnectionCollectionItem.to_json())

# convert the object into a dict
titanium_connection_collection_item_dict = titanium_connection_collection_item_instance.to_dict()
# create an instance of TitaniumConnectionCollectionItem from a dict
titanium_connection_collection_item_from_dict = TitaniumConnectionCollectionItem.from_dict(titanium_connection_collection_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


