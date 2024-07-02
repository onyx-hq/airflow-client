# titanium_airflow_client.RoleApi

All URIs are relative to *https://airflow.apache.org/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_role**](RoleApi.md#delete_role) | **DELETE** /roles/{role_name} | Delete a role
[**get_role**](RoleApi.md#get_role) | **GET** /roles/{role_name} | Get a role
[**get_roles**](RoleApi.md#get_roles) | **GET** /roles | List roles
[**patch_role**](RoleApi.md#patch_role) | **PATCH** /roles/{role_name} | Update a role
[**post_role**](RoleApi.md#post_role) | **POST** /roles | Create a role


# **delete_role**
> delete_role(role_name)

Delete a role

Delete a role.  *This API endpoint is deprecated, please use the endpoint `/auth/fab/v1` for this operation instead.* 

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
    api_instance = titanium_airflow_client.RoleApi(api_client)
    role_name = 'role_name_example' # str | The role name

    try:
        # Delete a role
        await api_instance.delete_role(role_name)
    except Exception as e:
        print("Exception when calling RoleApi->delete_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| The role name | 

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

# **get_role**
> TitaniumTitaniumRole get_role(role_name)

Get a role

Get a role.  *This API endpoint is deprecated, please use the endpoint `/auth/fab/v1` for this operation instead.* 

### Example


```python
import titanium_airflow_client
from titanium_airflow_client.models.titanium_titanium_role import TitaniumTitaniumRole
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
    api_instance = titanium_airflow_client.RoleApi(api_client)
    role_name = 'role_name_example' # str | The role name

    try:
        # Get a role
        api_response = await api_instance.get_role(role_name)
        print("The response of RoleApi->get_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleApi->get_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| The role name | 

### Return type

[**TitaniumTitaniumRole**](TitaniumRole.md)

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

# **get_roles**
> TitaniumTitaniumRoleCollection get_roles(limit=limit, offset=offset, order_by=order_by)

List roles

Get a list of roles.  *This API endpoint is deprecated, please use the endpoint `/auth/fab/v1` for this operation instead.* 

### Example


```python
import titanium_airflow_client
from titanium_airflow_client.models.titanium_titanium_role_collection import TitaniumTitaniumRoleCollection
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
    api_instance = titanium_airflow_client.RoleApi(api_client)
    limit = 100 # int | The numbers of items to return. (optional) (default to 100)
    offset = 56 # int | The number of items to skip before starting to collect the result set. (optional)
    order_by = 'order_by_example' # str | The name of the field to order the results by. Prefix a field name with `-` to reverse the sort order.  *New in version 2.1.0*  (optional)

    try:
        # List roles
        api_response = await api_instance.get_roles(limit=limit, offset=offset, order_by=order_by)
        print("The response of RoleApi->get_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleApi->get_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The numbers of items to return. | [optional] [default to 100]
 **offset** | **int**| The number of items to skip before starting to collect the result set. | [optional] 
 **order_by** | **str**| The name of the field to order the results by. Prefix a field name with &#x60;-&#x60; to reverse the sort order.  *New in version 2.1.0*  | [optional] 

### Return type

[**TitaniumTitaniumRoleCollection**](TitaniumRoleCollection.md)

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

# **patch_role**
> TitaniumTitaniumRole patch_role(role_name, titanium_role, update_mask=update_mask)

Update a role

Update a role.  *This API endpoint is deprecated, please use the endpoint `/auth/fab/v1` for this operation instead.* 

### Example


```python
import titanium_airflow_client
from titanium_airflow_client.models.titanium_role import TitaniumRole
from titanium_airflow_client.models.titanium_titanium_role import TitaniumTitaniumRole
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
    api_instance = titanium_airflow_client.RoleApi(api_client)
    role_name = 'role_name_example' # str | The role name
    titanium_role = titanium_airflow_client.TitaniumRole() # TitaniumRole | 
    update_mask = ['update_mask_example'] # List[str] | The fields to update on the resource. If absent or empty, all modifiable fields are updated. A comma-separated list of fully qualified names of fields.  (optional)

    try:
        # Update a role
        api_response = await api_instance.patch_role(role_name, titanium_role, update_mask=update_mask)
        print("The response of RoleApi->patch_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleApi->patch_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| The role name | 
 **titanium_role** | [**TitaniumRole**](TitaniumRole.md)|  | 
 **update_mask** | [**List[str]**](str.md)| The fields to update on the resource. If absent or empty, all modifiable fields are updated. A comma-separated list of fully qualified names of fields.  | [optional] 

### Return type

[**TitaniumTitaniumRole**](TitaniumRole.md)

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

# **post_role**
> TitaniumTitaniumRole post_role(titanium_role)

Create a role

Create a new role.  *This API endpoint is deprecated, please use the endpoint `/auth/fab/v1` for this operation instead.* 

### Example


```python
import titanium_airflow_client
from titanium_airflow_client.models.titanium_role import TitaniumRole
from titanium_airflow_client.models.titanium_titanium_role import TitaniumTitaniumRole
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
    api_instance = titanium_airflow_client.RoleApi(api_client)
    titanium_role = titanium_airflow_client.TitaniumRole() # TitaniumRole | 

    try:
        # Create a role
        api_response = await api_instance.post_role(titanium_role)
        print("The response of RoleApi->post_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleApi->post_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **titanium_role** | [**TitaniumRole**](TitaniumRole.md)|  | 

### Return type

[**TitaniumTitaniumRole**](TitaniumRole.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

