# titanium_airflow_client.XComApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_xcom_entries**](XComApi.md#get_xcom_entries) | **GET** /dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/xcomEntries | List XCom entries
[**get_xcom_entry**](XComApi.md#get_xcom_entry) | **GET** /dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/xcomEntries/{xcom_key} | Get an XCom entry


# **get_xcom_entries**
> XComCollection get_xcom_entries(dag_id, dag_run_id, task_id, map_index=map_index, xcom_key=xcom_key, limit=limit, offset=offset)

List XCom entries

This endpoint allows specifying `~` as the dag_id, dag_run_id, task_id to retrieve XCOM entries for for all DAGs, DAG runs and task instances. XCom values won't be returned as they can be large. Use this endpoint to get a list of XCom entries and then fetch individual entry to get value.

### Example

* Basic Authentication (Basic):

```python
import titanium_airflow_client
from titanium_airflow_client.models.x_com_collection import XComCollection
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
    api_instance = titanium_airflow_client.XComApi(api_client)
    dag_id = 'dag_id_example' # str | The DAG ID.
    dag_run_id = 'dag_run_id_example' # str | The DAG run ID.
    task_id = 'task_id_example' # str | The task ID.
    map_index = 56 # int | Filter on map index for mapped task. (optional)
    xcom_key = 'xcom_key_example' # str | Only filter the XCom records which have the provided key. (optional)
    limit = 100 # int | The numbers of items to return. (optional) (default to 100)
    offset = 56 # int | The number of items to skip before starting to collect the result set. (optional)

    try:
        # List XCom entries
        api_response = api_instance.get_xcom_entries(dag_id, dag_run_id, task_id, map_index=map_index, xcom_key=xcom_key, limit=limit, offset=offset)
        print("The response of XComApi->get_xcom_entries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling XComApi->get_xcom_entries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**| The DAG ID. | 
 **dag_run_id** | **str**| The DAG run ID. | 
 **task_id** | **str**| The task ID. | 
 **map_index** | **int**| Filter on map index for mapped task. | [optional] 
 **xcom_key** | **str**| Only filter the XCom records which have the provided key. | [optional] 
 **limit** | **int**| The numbers of items to return. | [optional] [default to 100]
 **offset** | **int**| The number of items to skip before starting to collect the result set. | [optional] 

### Return type

[**XComCollection**](XComCollection.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_xcom_entry**
> XCom get_xcom_entry(dag_id, dag_run_id, task_id, xcom_key, map_index=map_index, deserialize=deserialize)

Get an XCom entry

### Example

* Basic Authentication (Basic):

```python
import titanium_airflow_client
from titanium_airflow_client.models.x_com import XCom
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
    api_instance = titanium_airflow_client.XComApi(api_client)
    dag_id = 'dag_id_example' # str | The DAG ID.
    dag_run_id = 'dag_run_id_example' # str | The DAG run ID.
    task_id = 'task_id_example' # str | The task ID.
    xcom_key = 'xcom_key_example' # str | The XCom key.
    map_index = 56 # int | Filter on map index for mapped task. (optional)
    deserialize = False # bool | Whether to deserialize an XCom value when using a custom XCom backend.  The XCom API endpoint calls `orm_deserialize_value` by default since an XCom may contain value that is potentially expensive to deserialize in the web server. Setting this to true overrides the consideration, and calls `deserialize_value` instead.  This parameter is not meaningful when using the default XCom backend.  *New in version 2.4.0*  (optional) (default to False)

    try:
        # Get an XCom entry
        api_response = api_instance.get_xcom_entry(dag_id, dag_run_id, task_id, xcom_key, map_index=map_index, deserialize=deserialize)
        print("The response of XComApi->get_xcom_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling XComApi->get_xcom_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**| The DAG ID. | 
 **dag_run_id** | **str**| The DAG run ID. | 
 **task_id** | **str**| The task ID. | 
 **xcom_key** | **str**| The XCom key. | 
 **map_index** | **int**| Filter on map index for mapped task. | [optional] 
 **deserialize** | **bool**| Whether to deserialize an XCom value when using a custom XCom backend.  The XCom API endpoint calls &#x60;orm_deserialize_value&#x60; by default since an XCom may contain value that is potentially expensive to deserialize in the web server. Setting this to true overrides the consideration, and calls &#x60;deserialize_value&#x60; instead.  This parameter is not meaningful when using the default XCom backend.  *New in version 2.4.0*  | [optional] [default to False]

### Return type

[**XCom**](XCom.md)

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

