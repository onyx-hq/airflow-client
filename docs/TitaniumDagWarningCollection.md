# TitaniumDagWarningCollection

Collection of DAG warnings. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_entries** | **int** | Count of total objects in the current result set before pagination parameters (limit, offset) are applied.  | [optional] 
**import_errors** | [**List[TitaniumTitaniumDagWarning]**](TitaniumDagWarning.md) |  | [optional] 

## Example

```python
from titanium_airflow_client.models.titanium_dag_warning_collection import TitaniumDagWarningCollection

# TODO update the JSON string below
json = "{}"
# create an instance of TitaniumDagWarningCollection from a JSON string
titanium_dag_warning_collection_instance = TitaniumDagWarningCollection.from_json(json)
# print the JSON string representation of the object
print(TitaniumDagWarningCollection.to_json())

# convert the object into a dict
titanium_dag_warning_collection_dict = titanium_dag_warning_collection_instance.to_dict()
# create an instance of TitaniumDagWarningCollection from a dict
titanium_dag_warning_collection_from_dict = TitaniumDagWarningCollection.from_dict(titanium_dag_warning_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


