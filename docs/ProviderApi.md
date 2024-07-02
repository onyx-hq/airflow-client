# titanium_airflow_client.ProviderApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_providers**](ProviderApi.md#get_providers) | **GET** /providers | List providers


# **get_providers**
> GetProviders200Response get_providers()

List providers

Get a list of providers.  *New in version 2.1.0* 

### Example

* Basic Authentication (Basic):

```python
import titanium_airflow_client
from titanium_airflow_client.models.get_providers200_response import GetProviders200Response
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
    api_instance = titanium_airflow_client.ProviderApi(api_client)

    try:
        # List providers
        api_response = api_instance.get_providers()
        print("The response of ProviderApi->get_providers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProviderApi->get_providers: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetProviders200Response**](GetProviders200Response.md)

### Authorization

[Basic](../README.md#Basic), [Kerberos](../README.md#Kerberos), [GoogleOpenId](../README.md#GoogleOpenId)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of providers. |  -  |
**401** | Request not authenticated due to missing, invalid, authentication info. |  -  |
**403** | Client does not have sufficient permission. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

