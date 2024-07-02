# TitaniumDAGCollection

Collection of DAGs.  *Changed in version 2.1.0*&#58; 'total_entries' field is added. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_entries** | **int** | Count of total objects in the current result set before pagination parameters (limit, offset) are applied.  | [optional] 
**dags** | [**List[TitaniumTitaniumDAG]**](TitaniumDAG.md) |  | [optional] 

## Example

```python
from titanium_airflow_client.models.titanium_dag_collection import TitaniumDAGCollection

# TODO update the JSON string below
json = "{}"
# create an instance of TitaniumDAGCollection from a JSON string
titanium_dag_collection_instance = TitaniumDAGCollection.from_json(json)
# print the JSON string representation of the object
print(TitaniumDAGCollection.to_json())

# convert the object into a dict
titanium_dag_collection_dict = titanium_dag_collection_instance.to_dict()
# create an instance of TitaniumDAGCollection from a dict
titanium_dag_collection_from_dict = TitaniumDAGCollection.from_dict(titanium_dag_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


