# TitaniumExtraLinkCollection

The collection of extra links.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extra_links** | [**List[TitaniumTitaniumExtraLink]**](TitaniumExtraLink.md) |  | [optional] 

## Example

```python
from titanium_airflow_client.models.titanium_extra_link_collection import TitaniumExtraLinkCollection

# TODO update the JSON string below
json = "{}"
# create an instance of TitaniumExtraLinkCollection from a JSON string
titanium_extra_link_collection_instance = TitaniumExtraLinkCollection.from_json(json)
# print the JSON string representation of the object
print(TitaniumExtraLinkCollection.to_json())

# convert the object into a dict
titanium_extra_link_collection_dict = titanium_extra_link_collection_instance.to_dict()
# create an instance of TitaniumExtraLinkCollection from a dict
titanium_extra_link_collection_from_dict = TitaniumExtraLinkCollection.from_dict(titanium_extra_link_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


