# TitaniumGetProviders200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**providers** | [**List[TitaniumTitaniumProvider]**](TitaniumProvider.md) |  | [optional] 
**total_entries** | **int** | Count of total objects in the current result set before pagination parameters (limit, offset) are applied.  | [optional] 

## Example

```python
from titanium_airflow_client.models.titanium_get_providers200_response import TitaniumGetProviders200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TitaniumGetProviders200Response from a JSON string
titanium_get_providers200_response_instance = TitaniumGetProviders200Response.from_json(json)
# print the JSON string representation of the object
print(TitaniumGetProviders200Response.to_json())

# convert the object into a dict
titanium_get_providers200_response_dict = titanium_get_providers200_response_instance.to_dict()
# create an instance of TitaniumGetProviders200Response from a dict
titanium_get_providers200_response_from_dict = TitaniumGetProviders200Response.from_dict(titanium_get_providers200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


