# TitaniumProviderCollection

Collection of providers.  *New in version 2.1.0* 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**providers** | [**List[TitaniumTitaniumProvider]**](TitaniumProvider.md) |  | [optional] 

## Example

```python
from titanium_airflow_client.models.titanium_provider_collection import TitaniumProviderCollection

# TODO update the JSON string below
json = "{}"
# create an instance of TitaniumProviderCollection from a JSON string
titanium_provider_collection_instance = TitaniumProviderCollection.from_json(json)
# print the JSON string representation of the object
print(TitaniumProviderCollection.to_json())

# convert the object into a dict
titanium_provider_collection_dict = titanium_provider_collection_instance.to_dict()
# create an instance of TitaniumProviderCollection from a dict
titanium_provider_collection_from_dict = TitaniumProviderCollection.from_dict(titanium_provider_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


