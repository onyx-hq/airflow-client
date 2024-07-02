# TitaniumDatasetCollection

A collection of datasets.  *New in version 2.4.0* 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_entries** | **int** | Count of total objects in the current result set before pagination parameters (limit, offset) are applied.  | [optional] 
**datasets** | [**List[TitaniumTitaniumDataset]**](TitaniumDataset.md) |  | [optional] 

## Example

```python
from titanium_airflow_client.models.titanium_dataset_collection import TitaniumDatasetCollection

# TODO update the JSON string below
json = "{}"
# create an instance of TitaniumDatasetCollection from a JSON string
titanium_dataset_collection_instance = TitaniumDatasetCollection.from_json(json)
# print the JSON string representation of the object
print(TitaniumDatasetCollection.to_json())

# convert the object into a dict
titanium_dataset_collection_dict = titanium_dataset_collection_instance.to_dict()
# create an instance of TitaniumDatasetCollection from a dict
titanium_dataset_collection_from_dict = TitaniumDatasetCollection.from_dict(titanium_dataset_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


