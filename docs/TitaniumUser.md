# TitaniumUser

A user object with sensitive data.  *New in version 2.1.0* 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | The user&#39;s first name.  *Changed in version 2.4.0*&amp;#58; The requirement for this to be non-empty was removed.  | [optional] 
**last_name** | **str** | The user&#39;s last name.  *Changed in version 2.4.0*&amp;#58; The requirement for this to be non-empty was removed.  | [optional] 
**username** | **str** | The username.  *Changed in version 2.2.0*&amp;#58; A minimum character length requirement (&#39;minLength&#39;) is added.  | [optional] 
**email** | **str** | The user&#39;s email.  *Changed in version 2.2.0*&amp;#58; A minimum character length requirement (&#39;minLength&#39;) is added.  | [optional] 
**active** | **bool** | Whether the user is active | [optional] [readonly] 
**last_login** | **str** | The last user login | [optional] [readonly] 
**login_count** | **int** | The login count | [optional] [readonly] 
**failed_login_count** | **int** | The number of times the login failed | [optional] [readonly] 
**roles** | [**List[TitaniumTitaniumUserCollectionItemRolesInner]**](TitaniumUserCollectionItemRolesInner.md) | User roles.  *Changed in version 2.2.0*&amp;#58; Field is no longer read-only.  | [optional] 
**created_on** | **str** | The date user was created | [optional] [readonly] 
**changed_on** | **str** | The date user was changed | [optional] [readonly] 
**password** | **str** |  | [optional] 

## Example

```python
from titanium_airflow_client.models.titanium_user import TitaniumUser

# TODO update the JSON string below
json = "{}"
# create an instance of TitaniumUser from a JSON string
titanium_user_instance = TitaniumUser.from_json(json)
# print the JSON string representation of the object
print(TitaniumUser.to_json())

# convert the object into a dict
titanium_user_dict = titanium_user_instance.to_dict()
# create an instance of TitaniumUser from a dict
titanium_user_from_dict = TitaniumUser.from_dict(titanium_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


