# TitaniumPluginCollection

A collection of plugin.  *New in version 2.1.0* 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_entries** | **int** | Count of total objects in the current result set before pagination parameters (limit, offset) are applied.  | [optional] 
**plugins** | [**List[TitaniumTitaniumPluginCollectionItem]**](TitaniumPluginCollectionItem.md) |  | [optional] 

## Example

```python
from titanium_airflow_client.models.titanium_plugin_collection import TitaniumPluginCollection

# TODO update the JSON string below
json = "{}"
# create an instance of TitaniumPluginCollection from a JSON string
titanium_plugin_collection_instance = TitaniumPluginCollection.from_json(json)
# print the JSON string representation of the object
print(TitaniumPluginCollection.to_json())

# convert the object into a dict
titanium_plugin_collection_dict = titanium_plugin_collection_instance.to_dict()
# create an instance of TitaniumPluginCollection from a dict
titanium_plugin_collection_from_dict = TitaniumPluginCollection.from_dict(titanium_plugin_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


