# TitaniumExtraLink

Additional links containing additional information about the task.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_ref** | [**TitaniumTitaniumClassReference**](TitaniumClassReference.md) |  | [optional] 
**name** | **str** |  | [optional] [readonly] 
**href** | **str** |  | [optional] [readonly] 

## Example

```python
from titanium_airflow_client.models.titanium_extra_link import TitaniumExtraLink

# TODO update the JSON string below
json = "{}"
# create an instance of TitaniumExtraLink from a JSON string
titanium_extra_link_instance = TitaniumExtraLink.from_json(json)
# print the JSON string representation of the object
print(TitaniumExtraLink.to_json())

# convert the object into a dict
titanium_extra_link_dict = titanium_extra_link_instance.to_dict()
# create an instance of TitaniumExtraLink from a dict
titanium_extra_link_from_dict = TitaniumExtraLink.from_dict(titanium_extra_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


