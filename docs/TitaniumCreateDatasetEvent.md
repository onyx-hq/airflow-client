# TitaniumCreateDatasetEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset_uri** | **str** | The URI of the dataset | 
**extra** | **object** | The dataset event extra | [optional] 

## Example

```python
from titanium_airflow_client.models.titanium_create_dataset_event import TitaniumCreateDatasetEvent

# TODO update the JSON string below
json = "{}"
# create an instance of TitaniumCreateDatasetEvent from a JSON string
titanium_create_dataset_event_instance = TitaniumCreateDatasetEvent.from_json(json)
# print the JSON string representation of the object
print(TitaniumCreateDatasetEvent.to_json())

# convert the object into a dict
titanium_create_dataset_event_dict = titanium_create_dataset_event_instance.to_dict()
# create an instance of TitaniumCreateDatasetEvent from a dict
titanium_create_dataset_event_from_dict = TitaniumCreateDatasetEvent.from_dict(titanium_create_dataset_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


