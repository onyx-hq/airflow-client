# TitaniumMetadatabaseStatus

The status of the metadatabase.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**TitaniumTitaniumHealthStatus**](TitaniumHealthStatus.md) |  | [optional] 

## Example

```python
from titanium_airflow_client.models.titanium_metadatabase_status import TitaniumMetadatabaseStatus

# TODO update the JSON string below
json = "{}"
# create an instance of TitaniumMetadatabaseStatus from a JSON string
titanium_metadatabase_status_instance = TitaniumMetadatabaseStatus.from_json(json)
# print the JSON string representation of the object
print(TitaniumMetadatabaseStatus.to_json())

# convert the object into a dict
titanium_metadatabase_status_dict = titanium_metadatabase_status_instance.to_dict()
# create an instance of TitaniumMetadatabaseStatus from a dict
titanium_metadatabase_status_from_dict = TitaniumMetadatabaseStatus.from_dict(titanium_metadatabase_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


