# titanium_airflow_client.VariableApi

All URIs are relative to *https://airflow.apache.org/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_variable**](VariableApi.md#delete_variable) | **DELETE** /variables/{variable_key} | Delete a variable
[**get_variable**](VariableApi.md#get_variable) | **GET** /variables/{variable_key} | Get a variable
[**get_variables**](VariableApi.md#get_variables) | **GET** /variables | List variables
[**patch_variable**](VariableApi.md#patch_variable) | **PATCH** /variables/{variable_key} | Update a variable
[**post_variables**](VariableApi.md#post_variables) | **POST** /variables | Create a variable


# **delete_variable**
> delete_variable(variable_key)

Delete a variable

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
    api_instance = titanium_airflow_client.VariableApi(api_client)
    variable_key = 'variable_key_example' # str | The variable Key.

    try:
        # Delete a variable
        await api_instance.delete_variable(variable_key)
    except Exception as e:
        print("Exception when calling VariableApi->delete_variable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **variable_key** | **str**| The variable Key. | 

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

# **get_variable**
> TitaniumTitaniumVariable get_variable(variable_key)

Get a variable

Get a variable by key.

### Example


```python
import titanium_airflow_client
from titanium_airflow_client.models.titanium_titanium_variable import TitaniumTitaniumVariable
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
    api_instance = titanium_airflow_client.VariableApi(api_client)
    variable_key = 'variable_key_example' # str | The variable Key.

    try:
        # Get a variable
        api_response = await api_instance.get_variable(variable_key)
        print("The response of VariableApi->get_variable:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VariableApi->get_variable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **variable_key** | **str**| The variable Key. | 

### Return type

[**TitaniumTitaniumVariable**](TitaniumVariable.md)

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

# **get_variables**
> TitaniumTitaniumVariableCollection get_variables(limit=limit, offset=offset, order_by=order_by)

List variables

The collection does not contain data. To get data, you must get a single entity.

### Example


```python
import titanium_airflow_client
from titanium_airflow_client.models.titanium_titanium_variable_collection import TitaniumTitaniumVariableCollection
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
    api_instance = titanium_airflow_client.VariableApi(api_client)
    limit = 100 # int | The numbers of items to return. (optional) (default to 100)
    offset = 56 # int | The number of items to skip before starting to collect the result set. (optional)
    order_by = 'order_by_example' # str | The name of the field to order the results by. Prefix a field name with `-` to reverse the sort order.  *New in version 2.1.0*  (optional)

    try:
        # List variables
        api_response = await api_instance.get_variables(limit=limit, offset=offset, order_by=order_by)
        print("The response of VariableApi->get_variables:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VariableApi->get_variables: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The numbers of items to return. | [optional] [default to 100]
 **offset** | **int**| The number of items to skip before starting to collect the result set. | [optional] 
 **order_by** | **str**| The name of the field to order the results by. Prefix a field name with &#x60;-&#x60; to reverse the sort order.  *New in version 2.1.0*  | [optional] 

### Return type

[**TitaniumTitaniumVariableCollection**](TitaniumVariableCollection.md)

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

# **patch_variable**
> TitaniumTitaniumVariable patch_variable(variable_key, titanium_variable, update_mask=update_mask)

Update a variable

Update a variable by key.

### Example


```python
import titanium_airflow_client
from titanium_airflow_client.models.titanium_titanium_variable import TitaniumTitaniumVariable
from titanium_airflow_client.models.titanium_variable import TitaniumVariable
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
    api_instance = titanium_airflow_client.VariableApi(api_client)
    variable_key = 'variable_key_example' # str | The variable Key.
    titanium_variable = titanium_airflow_client.TitaniumVariable() # TitaniumVariable | 
    update_mask = ['update_mask_example'] # List[str] | The fields to update on the resource. If absent or empty, all modifiable fields are updated. A comma-separated list of fully qualified names of fields.  (optional)

    try:
        # Update a variable
        api_response = await api_instance.patch_variable(variable_key, titanium_variable, update_mask=update_mask)
        print("The response of VariableApi->patch_variable:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VariableApi->patch_variable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **variable_key** | **str**| The variable Key. | 
 **titanium_variable** | [**TitaniumVariable**](TitaniumVariable.md)|  | 
 **update_mask** | [**List[str]**](str.md)| The fields to update on the resource. If absent or empty, all modifiable fields are updated. A comma-separated list of fully qualified names of fields.  | [optional] 

### Return type

[**TitaniumTitaniumVariable**](TitaniumVariable.md)

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

# **post_variables**
> TitaniumTitaniumVariable post_variables(titanium_variable)

Create a variable

### Example


```python
import titanium_airflow_client
from titanium_airflow_client.models.titanium_titanium_variable import TitaniumTitaniumVariable
from titanium_airflow_client.models.titanium_variable import TitaniumVariable
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
    api_instance = titanium_airflow_client.VariableApi(api_client)
    titanium_variable = titanium_airflow_client.TitaniumVariable() # TitaniumVariable | 

    try:
        # Create a variable
        api_response = await api_instance.post_variables(titanium_variable)
        print("The response of VariableApi->post_variables:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VariableApi->post_variables: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **titanium_variable** | [**TitaniumVariable**](TitaniumVariable.md)|  | 

### Return type

[**TitaniumTitaniumVariable**](TitaniumVariable.md)

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
