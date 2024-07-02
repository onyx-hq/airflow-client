# TitaniumCollectionInfo

Metadata about collection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_entries** | **int** | Count of total objects in the current result set before pagination parameters (limit, offset) are applied.  | [optional] 

## Example

```python
from titanium_airflow_client.models.titanium_collection_info import TitaniumCollectionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TitaniumCollectionInfo from a JSON string
titanium_collection_info_instance = TitaniumCollectionInfo.from_json(json)
# print the JSON string representation of the object
print(TitaniumCollectionInfo.to_json())

# convert the object into a dict
titanium_collection_info_dict = titanium_collection_info_instance.to_dict()
# create an instance of TitaniumCollectionInfo from a dict
titanium_collection_info_from_dict = TitaniumCollectionInfo.from_dict(titanium_collection_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


