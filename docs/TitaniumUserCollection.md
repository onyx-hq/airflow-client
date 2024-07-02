# TitaniumUserCollection

Collection of users.  *New in version 2.1.0* 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_entries** | **int** | Count of total objects in the current result set before pagination parameters (limit, offset) are applied.  | [optional] 
**users** | [**List[TitaniumTitaniumUserCollectionItem]**](TitaniumUserCollectionItem.md) |  | [optional] 

## Example

```python
from titanium_airflow_client.models.titanium_user_collection import TitaniumUserCollection

# TODO update the JSON string below
json = "{}"
# create an instance of TitaniumUserCollection from a JSON string
titanium_user_collection_instance = TitaniumUserCollection.from_json(json)
# print the JSON string representation of the object
print(TitaniumUserCollection.to_json())

# convert the object into a dict
titanium_user_collection_dict = titanium_user_collection_instance.to_dict()
# create an instance of TitaniumUserCollection from a dict
titanium_user_collection_from_dict = TitaniumUserCollection.from_dict(titanium_user_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


