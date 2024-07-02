# TitaniumPoolCollection

Collection of pools.  *Changed in version 2.1.0*&#58; 'total_entries' field is added. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_entries** | **int** | Count of total objects in the current result set before pagination parameters (limit, offset) are applied.  | [optional] 
**pools** | [**List[TitaniumTitaniumPool]**](TitaniumPool.md) |  | [optional] 

## Example

```python
from titanium_airflow_client.models.titanium_pool_collection import TitaniumPoolCollection

# TODO update the JSON string below
json = "{}"
# create an instance of TitaniumPoolCollection from a JSON string
titanium_pool_collection_instance = TitaniumPoolCollection.from_json(json)
# print the JSON string representation of the object
print(TitaniumPoolCollection.to_json())

# convert the object into a dict
titanium_pool_collection_dict = titanium_pool_collection_instance.to_dict()
# create an instance of TitaniumPoolCollection from a dict
titanium_pool_collection_from_dict = TitaniumPoolCollection.from_dict(titanium_pool_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


