# GetLog200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**continuation_token** | **str** |  | [optional] 
**content** | **str** |  | [optional] 

## Example

```python
from titanium_airflow_client.models.get_log200_response import GetLog200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetLog200Response from a JSON string
get_log200_response_instance = GetLog200Response.from_json(json)
# print the JSON string representation of the object
print(GetLog200Response.to_json())

# convert the object into a dict
get_log200_response_dict = get_log200_response_instance.to_dict()
# create an instance of GetLog200Response from a dict
get_log200_response_from_dict = GetLog200Response.from_dict(get_log200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


