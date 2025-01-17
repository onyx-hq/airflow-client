# titanium_airflow_client.PoolApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_pool**](PoolApi.md#delete_pool) | **DELETE** /pools/{pool_name} | Delete a pool
[**get_pool**](PoolApi.md#get_pool) | **GET** /pools/{pool_name} | Get a pool
[**get_pools**](PoolApi.md#get_pools) | **GET** /pools | List pools
[**patch_pool**](PoolApi.md#patch_pool) | **PATCH** /pools/{pool_name} | Update a pool
[**post_pool**](PoolApi.md#post_pool) | **POST** /pools | Create a pool


# **delete_pool**
> delete_pool(pool_name)

Delete a pool

### Example

* Basic Authentication (Basic):

```python
import titanium_airflow_client
from titanium_airflow_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = titanium_airflow_client.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = titanium_airflow_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with titanium_airflow_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = titanium_airflow_client.PoolApi(api_client)
    pool_name = 'pool_name_example' # str | The pool name.

    try:
        # Delete a pool
        api_instance.delete_pool(pool_name)
    except Exception as e:
        print("Exception when calling PoolApi->delete_pool: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_name** | **str**| The pool name. | 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic), [Kerberos](../README.md#Kerberos), [GoogleOpenId](../README.md#GoogleOpenId)

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

# **get_pool**
> Pool get_pool(pool_name)

Get a pool

### Example

* Basic Authentication (Basic):

```python
import titanium_airflow_client
from titanium_airflow_client.models.pool import Pool
from titanium_airflow_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = titanium_airflow_client.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = titanium_airflow_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with titanium_airflow_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = titanium_airflow_client.PoolApi(api_client)
    pool_name = 'pool_name_example' # str | The pool name.

    try:
        # Get a pool
        api_response = api_instance.get_pool(pool_name)
        print("The response of PoolApi->get_pool:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoolApi->get_pool: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_name** | **str**| The pool name. | 

### Return type

[**Pool**](Pool.md)

### Authorization

[Basic](../README.md#Basic), [Kerberos](../README.md#Kerberos), [GoogleOpenId](../README.md#GoogleOpenId)

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

# **get_pools**
> PoolCollection get_pools(limit=limit, offset=offset, order_by=order_by)

List pools

### Example

* Basic Authentication (Basic):

```python
import titanium_airflow_client
from titanium_airflow_client.models.pool_collection import PoolCollection
from titanium_airflow_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = titanium_airflow_client.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = titanium_airflow_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with titanium_airflow_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = titanium_airflow_client.PoolApi(api_client)
    limit = 100 # int | The numbers of items to return. (optional) (default to 100)
    offset = 56 # int | The number of items to skip before starting to collect the result set. (optional)
    order_by = 'order_by_example' # str | The name of the field to order the results by. Prefix a field name with `-` to reverse the sort order.  *New in version 2.1.0*  (optional)

    try:
        # List pools
        api_response = api_instance.get_pools(limit=limit, offset=offset, order_by=order_by)
        print("The response of PoolApi->get_pools:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoolApi->get_pools: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The numbers of items to return. | [optional] [default to 100]
 **offset** | **int**| The number of items to skip before starting to collect the result set. | [optional] 
 **order_by** | **str**| The name of the field to order the results by. Prefix a field name with &#x60;-&#x60; to reverse the sort order.  *New in version 2.1.0*  | [optional] 

### Return type

[**PoolCollection**](PoolCollection.md)

### Authorization

[Basic](../README.md#Basic), [Kerberos](../README.md#Kerberos), [GoogleOpenId](../README.md#GoogleOpenId)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of pools. |  -  |
**401** | Request not authenticated due to missing, invalid, authentication info. |  -  |
**403** | Client does not have sufficient permission. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_pool**
> Pool patch_pool(pool_name, pool, update_mask=update_mask)

Update a pool

### Example

* Basic Authentication (Basic):

```python
import titanium_airflow_client
from titanium_airflow_client.models.pool import Pool
from titanium_airflow_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = titanium_airflow_client.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = titanium_airflow_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with titanium_airflow_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = titanium_airflow_client.PoolApi(api_client)
    pool_name = 'pool_name_example' # str | The pool name.
    pool = titanium_airflow_client.Pool() # Pool | 
    update_mask = ['update_mask_example'] # List[str] | The fields to update on the resource. If absent or empty, all modifiable fields are updated. A comma-separated list of fully qualified names of fields.  (optional)

    try:
        # Update a pool
        api_response = api_instance.patch_pool(pool_name, pool, update_mask=update_mask)
        print("The response of PoolApi->patch_pool:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoolApi->patch_pool: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_name** | **str**| The pool name. | 
 **pool** | [**Pool**](Pool.md)|  | 
 **update_mask** | [**List[str]**](str.md)| The fields to update on the resource. If absent or empty, all modifiable fields are updated. A comma-separated list of fully qualified names of fields.  | [optional] 

### Return type

[**Pool**](Pool.md)

### Authorization

[Basic](../README.md#Basic), [Kerberos](../README.md#Kerberos), [GoogleOpenId](../README.md#GoogleOpenId)

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
**409** | An existing resource conflicts with the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_pool**
> Pool post_pool(pool)

Create a pool

### Example

* Basic Authentication (Basic):

```python
import titanium_airflow_client
from titanium_airflow_client.models.pool import Pool
from titanium_airflow_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = titanium_airflow_client.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = titanium_airflow_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with titanium_airflow_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = titanium_airflow_client.PoolApi(api_client)
    pool = titanium_airflow_client.Pool() # Pool | 

    try:
        # Create a pool
        api_response = api_instance.post_pool(pool)
        print("The response of PoolApi->post_pool:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoolApi->post_pool: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool** | [**Pool**](Pool.md)|  | 

### Return type

[**Pool**](Pool.md)

### Authorization

[Basic](../README.md#Basic), [Kerberos](../README.md#Kerberos), [GoogleOpenId](../README.md#GoogleOpenId)

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

