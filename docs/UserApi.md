# titanium_airflow_client.UserApi

All URIs are relative to *https://airflow.apache.org/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_user**](UserApi.md#delete_user) | **DELETE** /users/{username} | Delete a user
[**get_user**](UserApi.md#get_user) | **GET** /users/{username} | Get a user
[**get_users**](UserApi.md#get_users) | **GET** /users | List users
[**patch_user**](UserApi.md#patch_user) | **PATCH** /users/{username} | Update a user
[**post_user**](UserApi.md#post_user) | **POST** /users | Create a user


# **delete_user**
> delete_user(username)

Delete a user

Delete a user with a specific username.  *This API endpoint is deprecated, please use the endpoint `/auth/fab/v1` for this operation instead.* 

### Example


```python
import titanium_airflow_client
from titanium_airflow_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://airflow.apache.org/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = titanium_airflow_client.Configuration(
    host = "https://airflow.apache.org/api/v1"
)


# Enter a context with an instance of the API client
async with titanium_airflow_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = titanium_airflow_client.UserApi(api_client)
    username = 'username_example' # str | The username of the user.  *New in version 2.1.0* 

    try:
        # Delete a user
        await api_instance.delete_user(username)
    except Exception as e:
        print("Exception when calling UserApi->delete_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username of the user.  *New in version 2.1.0*  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success. |  -  |
**400** | Client specified an invalid argument. |  -  |
**401** | Request not authenticated due to missing, invalid, authentication info. |  -  |
**403** | Client does not have sufficient permission. |  -  |
**404** | A specified resource is not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> TitaniumTitaniumUserCollectionItem get_user(username)

Get a user

Get a user with a specific username.  *This API endpoint is deprecated, please use the endpoint `/auth/fab/v1` for this operation instead.* 

### Example


```python
import titanium_airflow_client
from titanium_airflow_client.models.titanium_titanium_user_collection_item import TitaniumTitaniumUserCollectionItem
from titanium_airflow_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://airflow.apache.org/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = titanium_airflow_client.Configuration(
    host = "https://airflow.apache.org/api/v1"
)


# Enter a context with an instance of the API client
async with titanium_airflow_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = titanium_airflow_client.UserApi(api_client)
    username = 'username_example' # str | The username of the user.  *New in version 2.1.0* 

    try:
        # Get a user
        api_response = await api_instance.get_user(username)
        print("The response of UserApi->get_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username of the user.  *New in version 2.1.0*  | 

### Return type

[**TitaniumTitaniumUserCollectionItem**](TitaniumUserCollectionItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Request not authenticated due to missing, invalid, authentication info. |  -  |
**403** | Client does not have sufficient permission. |  -  |
**404** | A specified resource is not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users**
> TitaniumTitaniumUserCollection get_users(limit=limit, offset=offset, order_by=order_by)

List users

Get a list of users.  *This API endpoint is deprecated, please use the endpoint `/auth/fab/v1` for this operation instead.* 

### Example


```python
import titanium_airflow_client
from titanium_airflow_client.models.titanium_titanium_user_collection import TitaniumTitaniumUserCollection
from titanium_airflow_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://airflow.apache.org/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = titanium_airflow_client.Configuration(
    host = "https://airflow.apache.org/api/v1"
)


# Enter a context with an instance of the API client
async with titanium_airflow_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = titanium_airflow_client.UserApi(api_client)
    limit = 100 # int | The numbers of items to return. (optional) (default to 100)
    offset = 56 # int | The number of items to skip before starting to collect the result set. (optional)
    order_by = 'order_by_example' # str | The name of the field to order the results by. Prefix a field name with `-` to reverse the sort order.  *New in version 2.1.0*  (optional)

    try:
        # List users
        api_response = await api_instance.get_users(limit=limit, offset=offset, order_by=order_by)
        print("The response of UserApi->get_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The numbers of items to return. | [optional] [default to 100]
 **offset** | **int**| The number of items to skip before starting to collect the result set. | [optional] 
 **order_by** | **str**| The name of the field to order the results by. Prefix a field name with &#x60;-&#x60; to reverse the sort order.  *New in version 2.1.0*  | [optional] 

### Return type

[**TitaniumTitaniumUserCollection**](TitaniumUserCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Request not authenticated due to missing, invalid, authentication info. |  -  |
**403** | Client does not have sufficient permission. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_user**
> TitaniumTitaniumUserCollectionItem patch_user(username, titanium_user, update_mask=update_mask)

Update a user

Update fields for a user.  *This API endpoint is deprecated, please use the endpoint `/auth/fab/v1` for this operation instead.* 

### Example


```python
import titanium_airflow_client
from titanium_airflow_client.models.titanium_titanium_user_collection_item import TitaniumTitaniumUserCollectionItem
from titanium_airflow_client.models.titanium_user import TitaniumUser
from titanium_airflow_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://airflow.apache.org/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = titanium_airflow_client.Configuration(
    host = "https://airflow.apache.org/api/v1"
)


# Enter a context with an instance of the API client
async with titanium_airflow_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = titanium_airflow_client.UserApi(api_client)
    username = 'username_example' # str | The username of the user.  *New in version 2.1.0* 
    titanium_user = titanium_airflow_client.TitaniumUser() # TitaniumUser | 
    update_mask = ['update_mask_example'] # List[str] | The fields to update on the resource. If absent or empty, all modifiable fields are updated. A comma-separated list of fully qualified names of fields.  (optional)

    try:
        # Update a user
        api_response = await api_instance.patch_user(username, titanium_user, update_mask=update_mask)
        print("The response of UserApi->patch_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->patch_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username of the user.  *New in version 2.1.0*  | 
 **titanium_user** | [**TitaniumUser**](TitaniumUser.md)|  | 
 **update_mask** | [**List[str]**](str.md)| The fields to update on the resource. If absent or empty, all modifiable fields are updated. A comma-separated list of fully qualified names of fields.  | [optional] 

### Return type

[**TitaniumTitaniumUserCollectionItem**](TitaniumUserCollectionItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**400** | Client specified an invalid argument. |  -  |
**401** | Request not authenticated due to missing, invalid, authentication info. |  -  |
**403** | Client does not have sufficient permission. |  -  |
**404** | A specified resource is not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_user**
> TitaniumTitaniumUser post_user(titanium_user)

Create a user

Create a new user with unique username and email.  *This API endpoint is deprecated, please use the endpoint `/auth/fab/v1` for this operation instead.* 

### Example


```python
import titanium_airflow_client
from titanium_airflow_client.models.titanium_titanium_user import TitaniumTitaniumUser
from titanium_airflow_client.models.titanium_user import TitaniumUser
from titanium_airflow_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://airflow.apache.org/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = titanium_airflow_client.Configuration(
    host = "https://airflow.apache.org/api/v1"
)


# Enter a context with an instance of the API client
async with titanium_airflow_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = titanium_airflow_client.UserApi(api_client)
    titanium_user = titanium_airflow_client.TitaniumUser() # TitaniumUser | 

    try:
        # Create a user
        api_response = await api_instance.post_user(titanium_user)
        print("The response of UserApi->post_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->post_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **titanium_user** | [**TitaniumUser**](TitaniumUser.md)|  | 

### Return type

[**TitaniumTitaniumUser**](TitaniumUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**400** | Client specified an invalid argument. |  -  |
**401** | Request not authenticated due to missing, invalid, authentication info. |  -  |
**403** | Client does not have sufficient permission. |  -  |
**409** | An existing resource conflicts with the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
