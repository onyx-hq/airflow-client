# titanium_airflow_client.EventLogApi

All URIs are relative to *https://airflow.apache.org/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_event_log**](EventLogApi.md#get_event_log) | **GET** /eventLogs/{event_log_id} | Get a log entry
[**get_event_logs**](EventLogApi.md#get_event_logs) | **GET** /eventLogs | List log entries


# **get_event_log**
> TitaniumTitaniumEventLog get_event_log(event_log_id)

Get a log entry

### Example


```python
import titanium_airflow_client
from titanium_airflow_client.models.titanium_titanium_event_log import TitaniumTitaniumEventLog
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
    api_instance = titanium_airflow_client.EventLogApi(api_client)
    event_log_id = 56 # int | The event log ID.

    try:
        # Get a log entry
        api_response = await api_instance.get_event_log(event_log_id)
        print("The response of EventLogApi->get_event_log:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventLogApi->get_event_log: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_log_id** | **int**| The event log ID. | 

### Return type

[**TitaniumTitaniumEventLog**](TitaniumEventLog.md)

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

# **get_event_logs**
> TitaniumTitaniumEventLogCollection get_event_logs(limit=limit, offset=offset, order_by=order_by, dag_id=dag_id, task_id=task_id, run_id=run_id, event=event, owner=owner, before=before, after=after, included_events=included_events, excluded_events=excluded_events)

List log entries

List log entries from event log.

### Example


```python
import titanium_airflow_client
from titanium_airflow_client.models.titanium_titanium_event_log_collection import TitaniumTitaniumEventLogCollection
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
    api_instance = titanium_airflow_client.EventLogApi(api_client)
    limit = 100 # int | The numbers of items to return. (optional) (default to 100)
    offset = 56 # int | The number of items to skip before starting to collect the result set. (optional)
    order_by = 'order_by_example' # str | The name of the field to order the results by. Prefix a field name with `-` to reverse the sort order.  *New in version 2.1.0*  (optional)
    dag_id = 'dag_id_example' # str | Returns objects matched by the DAG ID. (optional)
    task_id = 'task_id_example' # str | Returns objects matched by the Task ID. (optional)
    run_id = 'run_id_example' # str | Returns objects matched by the Run ID. (optional)
    event = 'event_example' # str | The name of event log. (optional)
    owner = 'owner_example' # str | The owner's name of event log. (optional)
    before = '2013-10-20T19:20:30+01:00' # datetime | Timestamp to select event logs occurring before. (optional)
    after = '2013-10-20T19:20:30+01:00' # datetime | Timestamp to select event logs occurring after. (optional)
    included_events = 'included_events_example' # str | One or more event names separated by commas. If set, only return event logs with events matching this pattern. *New in version 2.9.0*  (optional)
    excluded_events = 'excluded_events_example' # str | One or more event names separated by commas. If set, only return event logs with events that do not match this pattern. *New in version 2.9.0*  (optional)

    try:
        # List log entries
        api_response = await api_instance.get_event_logs(limit=limit, offset=offset, order_by=order_by, dag_id=dag_id, task_id=task_id, run_id=run_id, event=event, owner=owner, before=before, after=after, included_events=included_events, excluded_events=excluded_events)
        print("The response of EventLogApi->get_event_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventLogApi->get_event_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The numbers of items to return. | [optional] [default to 100]
 **offset** | **int**| The number of items to skip before starting to collect the result set. | [optional] 
 **order_by** | **str**| The name of the field to order the results by. Prefix a field name with &#x60;-&#x60; to reverse the sort order.  *New in version 2.1.0*  | [optional] 
 **dag_id** | **str**| Returns objects matched by the DAG ID. | [optional] 
 **task_id** | **str**| Returns objects matched by the Task ID. | [optional] 
 **run_id** | **str**| Returns objects matched by the Run ID. | [optional] 
 **event** | **str**| The name of event log. | [optional] 
 **owner** | **str**| The owner&#39;s name of event log. | [optional] 
 **before** | **datetime**| Timestamp to select event logs occurring before. | [optional] 
 **after** | **datetime**| Timestamp to select event logs occurring after. | [optional] 
 **included_events** | **str**| One or more event names separated by commas. If set, only return event logs with events matching this pattern. *New in version 2.9.0*  | [optional] 
 **excluded_events** | **str**| One or more event names separated by commas. If set, only return event logs with events that do not match this pattern. *New in version 2.9.0*  | [optional] 

### Return type

[**TitaniumTitaniumEventLogCollection**](TitaniumEventLogCollection.md)

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

