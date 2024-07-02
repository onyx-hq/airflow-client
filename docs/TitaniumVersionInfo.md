# TitaniumVersionInfo

Version information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | The version of Airflow | [optional] 
**git_version** | **str** | The git version (including git commit hash) | [optional] 

## Example

```python
from titanium_airflow_client.models.titanium_version_info import TitaniumVersionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TitaniumVersionInfo from a JSON string
titanium_version_info_instance = TitaniumVersionInfo.from_json(json)
# print the JSON string representation of the object
print(TitaniumVersionInfo.to_json())

# convert the object into a dict
titanium_version_info_dict = titanium_version_info_instance.to_dict()
# create an instance of TitaniumVersionInfo from a dict
titanium_version_info_from_dict = TitaniumVersionInfo.from_dict(titanium_version_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


