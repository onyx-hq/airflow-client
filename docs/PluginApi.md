# titanium_airflow_client.PluginApi

All URIs are relative to *https://airflow.apache.org/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_plugins**](PluginApi.md#get_plugins) | **GET** /plugins | Get a list of loaded plugins


# **get_plugins**
> TitaniumTitaniumPluginCollection get_plugins(limit=limit, offset=offset)

Get a list of loaded plugins

Get a list of loaded plugins.  *New in version 2.1.0* 

### Example


```python
import titanium_airflow_client
from titanium_airflow_client.models.titanium_titanium_plugin_collection import TitaniumTitaniumPluginCollection
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
    api_instance = titanium_airflow_client.PluginApi(api_client)
    limit = 100 # int | The numbers of items to return. (optional) (default to 100)
    offset = 56 # int | The number of items to skip before starting to collect the result set. (optional)

    try:
        # Get a list of loaded plugins
        api_response = await api_instance.get_plugins(limit=limit, offset=offset)
        print("The response of PluginApi->get_plugins:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginApi->get_plugins: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The numbers of items to return. | [optional] [default to 100]
 **offset** | **int**| The number of items to skip before starting to collect the result set. | [optional] 

### Return type

[**TitaniumTitaniumPluginCollection**](TitaniumPluginCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Request not authenticated due to missing, invalid, authentication info. |  -  |
**403** | Client does not have sufficient permission. |  -  |
**404** | A specified resource is not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

