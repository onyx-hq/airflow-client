# TitaniumGetLog200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**continuation_token** | **str** |  | [optional] 
**content** | **str** |  | [optional] 

## Example

```python
from titanium_airflow_client.models.titanium_get_log200_response import TitaniumGetLog200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TitaniumGetLog200Response from a JSON string
titanium_get_log200_response_instance = TitaniumGetLog200Response.from_json(json)
# print the JSON string representation of the object
print(TitaniumGetLog200Response.to_json())

# convert the object into a dict
titanium_get_log200_response_dict = titanium_get_log200_response_instance.to_dict()
# create an instance of TitaniumGetLog200Response from a dict
titanium_get_log200_response_from_dict = TitaniumGetLog200Response.from_dict(titanium_get_log200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


