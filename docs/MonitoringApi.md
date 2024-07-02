# titanium_airflow_client.MonitoringApi

All URIs are relative to *https://airflow.apache.org/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_health**](MonitoringApi.md#get_health) | **GET** /health | Get instance status
[**get_version**](MonitoringApi.md#get_version) | **GET** /version | Get version information


# **get_health**
> TitaniumTitaniumHealthInfo get_health()

Get instance status

Get the status of Airflow's metadatabase, triggerer and scheduler. It includes info about metadatabase and last heartbeat of scheduler and triggerer. 

### Example


```python
import titanium_airflow_client
from titanium_airflow_client.models.titanium_titanium_health_info import TitaniumTitaniumHealthInfo
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
    api_instance = titanium_airflow_client.MonitoringApi(api_client)

    try:
        # Get instance status
        api_response = await api_instance.get_health()
        print("The response of MonitoringApi->get_health:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MonitoringApi->get_health: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**TitaniumTitaniumHealthInfo**](TitaniumHealthInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_version**
> TitaniumTitaniumVersionInfo get_version()

Get version information

### Example


```python
import titanium_airflow_client
from titanium_airflow_client.models.titanium_titanium_version_info import TitaniumTitaniumVersionInfo
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
    api_instance = titanium_airflow_client.MonitoringApi(api_client)

    try:
        # Get version information
        api_response = await api_instance.get_version()
        print("The response of MonitoringApi->get_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MonitoringApi->get_version: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**TitaniumTitaniumVersionInfo**](TitaniumVersionInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

