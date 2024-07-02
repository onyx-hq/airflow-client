# TitaniumConnectionTest

Connection test results.  *New in version 2.2.0* 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** | The status of the request. | [optional] 
**message** | **str** | The success or failure message of the request. | [optional] 

## Example

```python
from titanium_airflow_client.models.titanium_connection_test import TitaniumConnectionTest

# TODO update the JSON string below
json = "{}"
# create an instance of TitaniumConnectionTest from a JSON string
titanium_connection_test_instance = TitaniumConnectionTest.from_json(json)
# print the JSON string representation of the object
print(TitaniumConnectionTest.to_json())

# convert the object into a dict
titanium_connection_test_dict = titanium_connection_test_instance.to_dict()
# create an instance of TitaniumConnectionTest from a dict
titanium_connection_test_from_dict = TitaniumConnectionTest.from_dict(titanium_connection_test_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


