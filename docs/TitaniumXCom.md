# TitaniumXCom

Full representations of XCom entry.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**timestamp** | **str** |  | [optional] 
**execution_date** | **str** |  | [optional] 
**map_index** | **int** |  | [optional] 
**task_id** | **str** |  | [optional] 
**dag_id** | **str** |  | [optional] 
**value** | **str** | The value | [optional] 

## Example

```python
from titanium_airflow_client.models.titanium_x_com import TitaniumXCom

# TODO update the JSON string below
json = "{}"
# create an instance of TitaniumXCom from a JSON string
titanium_x_com_instance = TitaniumXCom.from_json(json)
# print the JSON string representation of the object
print(TitaniumXCom.to_json())

# convert the object into a dict
titanium_x_com_dict = titanium_x_com_instance.to_dict()
# create an instance of TitaniumXCom from a dict
titanium_x_com_from_dict = TitaniumXCom.from_dict(titanium_x_com_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


