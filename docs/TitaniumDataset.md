# TitaniumDataset

A dataset item.  *New in version 2.4.0* 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The dataset id | [optional] 
**uri** | **str** | The dataset uri | [optional] 
**extra** | **object** | The dataset extra | [optional] 
**created_at** | **str** | The dataset creation time | [optional] 
**updated_at** | **str** | The dataset update time | [optional] 
**consuming_dags** | [**List[TitaniumTitaniumDagScheduleDatasetReference]**](TitaniumDagScheduleDatasetReference.md) |  | [optional] 
**producing_tasks** | [**List[TitaniumTitaniumTaskOutletDatasetReference]**](TitaniumTaskOutletDatasetReference.md) |  | [optional] 

## Example

```python
from titanium_airflow_client.models.titanium_dataset import TitaniumDataset

# TODO update the JSON string below
json = "{}"
# create an instance of TitaniumDataset from a JSON string
titanium_dataset_instance = TitaniumDataset.from_json(json)
# print the JSON string representation of the object
print(TitaniumDataset.to_json())

# convert the object into a dict
titanium_dataset_dict = titanium_dataset_instance.to_dict()
# create an instance of TitaniumDataset from a dict
titanium_dataset_from_dict = TitaniumDataset.from_dict(titanium_dataset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


