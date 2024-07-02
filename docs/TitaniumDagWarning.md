# TitaniumDagWarning


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dag_id** | **str** | The dag_id. | [optional] [readonly] 
**warning_type** | **str** | The warning type for the dag warning. | [optional] [readonly] 
**message** | **str** | The message for the dag warning. | [optional] [readonly] 
**timestamp** | **str** | The time when this warning was logged. | [optional] [readonly] 

## Example

```python
from titanium_airflow_client.models.titanium_dag_warning import TitaniumDagWarning

# TODO update the JSON string below
json = "{}"
# create an instance of TitaniumDagWarning from a JSON string
titanium_dag_warning_instance = TitaniumDagWarning.from_json(json)
# print the JSON string representation of the object
print(TitaniumDagWarning.to_json())

# convert the object into a dict
titanium_dag_warning_dict = titanium_dag_warning_instance.to_dict()
# create an instance of TitaniumDagWarning from a dict
titanium_dag_warning_from_dict = TitaniumDagWarning.from_dict(titanium_dag_warning_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


