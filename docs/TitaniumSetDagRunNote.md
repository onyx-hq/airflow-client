# TitaniumSetDagRunNote


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**note** | **str** | Custom notes left by users for this Dag Run. | [optional] 

## Example

```python
from titanium_airflow_client.models.titanium_set_dag_run_note import TitaniumSetDagRunNote

# TODO update the JSON string below
json = "{}"
# create an instance of TitaniumSetDagRunNote from a JSON string
titanium_set_dag_run_note_instance = TitaniumSetDagRunNote.from_json(json)
# print the JSON string representation of the object
print(TitaniumSetDagRunNote.to_json())

# convert the object into a dict
titanium_set_dag_run_note_dict = titanium_set_dag_run_note_instance.to_dict()
# create an instance of TitaniumSetDagRunNote from a dict
titanium_set_dag_run_note_from_dict = TitaniumSetDagRunNote.from_dict(titanium_set_dag_run_note_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


