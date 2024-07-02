# TitaniumCronExpression

Cron expression

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from titanium_airflow_client.models.titanium_cron_expression import TitaniumCronExpression

# TODO update the JSON string below
json = "{}"
# create an instance of TitaniumCronExpression from a JSON string
titanium_cron_expression_instance = TitaniumCronExpression.from_json(json)
# print the JSON string representation of the object
print(TitaniumCronExpression.to_json())

# convert the object into a dict
titanium_cron_expression_dict = titanium_cron_expression_instance.to_dict()
# create an instance of TitaniumCronExpression from a dict
titanium_cron_expression_from_dict = TitaniumCronExpression.from_dict(titanium_cron_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


