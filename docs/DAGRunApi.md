# titanium_airflow_client.DAGRunApi

All URIs are relative to *https://airflow.apache.org/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clear_dag_run**](DAGRunApi.md#clear_dag_run) | **POST** /dags/{dag_id}/dagRuns/{dag_run_id}/clear | Clear a DAG run
[**delete_dag_run**](DAGRunApi.md#delete_dag_run) | **DELETE** /dags/{dag_id}/dagRuns/{dag_run_id} | Delete a DAG run
[**get_dag_run**](DAGRunApi.md#get_dag_run) | **GET** /dags/{dag_id}/dagRuns/{dag_run_id} | Get a DAG run
[**get_dag_runs**](DAGRunApi.md#get_dag_runs) | **GET** /dags/{dag_id}/dagRuns | List DAG runs
[**get_dag_runs_batch**](DAGRunApi.md#get_dag_runs_batch) | **POST** /dags/~/dagRuns/list | List DAG runs (batch)
[**get_upstream_dataset_events**](DAGRunApi.md#get_upstream_dataset_events) | **GET** /dags/{dag_id}/dagRuns/{dag_run_id}/upstreamDatasetEvents | Get dataset events for a DAG run
[**post_dag_run**](DAGRunApi.md#post_dag_run) | **POST** /dags/{dag_id}/dagRuns | Trigger a new DAG run.
[**set_dag_run_note**](DAGRunApi.md#set_dag_run_note) | **PATCH** /dags/{dag_id}/dagRuns/{dag_run_id}/setNote | Update the DagRun note.
[**update_dag_run_state**](DAGRunApi.md#update_dag_run_state) | **PATCH** /dags/{dag_id}/dagRuns/{dag_run_id} | Modify a DAG run


# **clear_dag_run**
> TitaniumTitaniumClearDagRun200Response clear_dag_run(dag_id, dag_run_id, titanium_clear_dag_run)

Clear a DAG run

Clear a DAG run.  *New in version 2.4.0* 

### Example


```python
import titanium_airflow_client
from titanium_airflow_client.models.titanium_clear_dag_run import TitaniumClearDagRun
from titanium_airflow_client.models.titanium_titanium_clear_dag_run200_response import TitaniumTitaniumClearDagRun200Response
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
    api_instance = titanium_airflow_client.DAGRunApi(api_client)
    dag_id = 'dag_id_example' # str | The DAG ID.
    dag_run_id = 'dag_run_id_example' # str | The DAG run ID.
    titanium_clear_dag_run = titanium_airflow_client.TitaniumClearDagRun() # TitaniumClearDagRun | 

    try:
        # Clear a DAG run
        api_response = await api_instance.clear_dag_run(dag_id, dag_run_id, titanium_clear_dag_run)
        print("The response of DAGRunApi->clear_dag_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DAGRunApi->clear_dag_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**| The DAG ID. | 
 **dag_run_id** | **str**| The DAG run ID. | 
 **titanium_clear_dag_run** | [**TitaniumClearDagRun**](TitaniumClearDagRun.md)|  | 

### Return type

[**TitaniumTitaniumClearDagRun200Response**](TitaniumClearDagRun200Response.md)

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

# **delete_dag_run**
> delete_dag_run(dag_id, dag_run_id)

Delete a DAG run

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
    api_instance = titanium_airflow_client.DAGRunApi(api_client)
    dag_id = 'dag_id_example' # str | The DAG ID.
    dag_run_id = 'dag_run_id_example' # str | The DAG run ID.

    try:
        # Delete a DAG run
        await api_instance.delete_dag_run(dag_id, dag_run_id)
    except Exception as e:
        print("Exception when calling DAGRunApi->delete_dag_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**| The DAG ID. | 
 **dag_run_id** | **str**| The DAG run ID. | 

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

# **get_dag_run**
> TitaniumTitaniumDAGRun get_dag_run(dag_id, dag_run_id, fields=fields)

Get a DAG run

### Example


```python
import titanium_airflow_client
from titanium_airflow_client.models.titanium_titanium_dag_run import TitaniumTitaniumDAGRun
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
    api_instance = titanium_airflow_client.DAGRunApi(api_client)
    dag_id = 'dag_id_example' # str | The DAG ID.
    dag_run_id = 'dag_run_id_example' # str | The DAG run ID.
    fields = ['fields_example'] # List[str] | List of field for return.  (optional)

    try:
        # Get a DAG run
        api_response = await api_instance.get_dag_run(dag_id, dag_run_id, fields=fields)
        print("The response of DAGRunApi->get_dag_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DAGRunApi->get_dag_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**| The DAG ID. | 
 **dag_run_id** | **str**| The DAG run ID. | 
 **fields** | [**List[str]**](str.md)| List of field for return.  | [optional] 

### Return type

[**TitaniumTitaniumDAGRun**](TitaniumDAGRun.md)

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

# **get_dag_runs**
> TitaniumTitaniumDAGRunCollection get_dag_runs(dag_id, limit=limit, offset=offset, execution_date_gte=execution_date_gte, execution_date_lte=execution_date_lte, start_date_gte=start_date_gte, start_date_lte=start_date_lte, end_date_gte=end_date_gte, end_date_lte=end_date_lte, updated_at_gte=updated_at_gte, updated_at_lte=updated_at_lte, state=state, order_by=order_by, fields=fields)

List DAG runs

This endpoint allows specifying `~` as the dag_id to retrieve DAG runs for all DAGs. 

### Example


```python
import titanium_airflow_client
from titanium_airflow_client.models.titanium_titanium_dag_run_collection import TitaniumTitaniumDAGRunCollection
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
    api_instance = titanium_airflow_client.DAGRunApi(api_client)
    dag_id = 'dag_id_example' # str | The DAG ID.
    limit = 100 # int | The numbers of items to return. (optional) (default to 100)
    offset = 56 # int | The number of items to skip before starting to collect the result set. (optional)
    execution_date_gte = '2013-10-20T19:20:30+01:00' # datetime | Returns objects greater or equal to the specified date.  This can be combined with execution_date_lte parameter to receive only the selected period.  (optional)
    execution_date_lte = '2013-10-20T19:20:30+01:00' # datetime | Returns objects less than or equal to the specified date.  This can be combined with execution_date_gte parameter to receive only the selected period.  (optional)
    start_date_gte = '2013-10-20T19:20:30+01:00' # datetime | Returns objects greater or equal the specified date.  This can be combined with start_date_lte parameter to receive only the selected period.  (optional)
    start_date_lte = '2013-10-20T19:20:30+01:00' # datetime | Returns objects less or equal the specified date.  This can be combined with start_date_gte parameter to receive only the selected period.  (optional)
    end_date_gte = '2013-10-20T19:20:30+01:00' # datetime | Returns objects greater or equal the specified date.  This can be combined with start_date_lte parameter to receive only the selected period.  (optional)
    end_date_lte = '2013-10-20T19:20:30+01:00' # datetime | Returns objects less than or equal to the specified date.  This can be combined with start_date_gte parameter to receive only the selected period.  (optional)
    updated_at_gte = '2013-10-20T19:20:30+01:00' # datetime | Returns objects greater or equal the specified date.  This can be combined with updated_at_lte parameter to receive only the selected period.  *New in version 2.6.0*  (optional)
    updated_at_lte = '2013-10-20T19:20:30+01:00' # datetime | Returns objects less or equal the specified date.  This can be combined with updated_at_gte parameter to receive only the selected period.  *New in version 2.6.0*  (optional)
    state = ['state_example'] # List[str] | The value can be repeated to retrieve multiple matching values (OR condition). (optional)
    order_by = 'order_by_example' # str | The name of the field to order the results by. Prefix a field name with `-` to reverse the sort order.  *New in version 2.1.0*  (optional)
    fields = ['fields_example'] # List[str] | List of field for return.  (optional)

    try:
        # List DAG runs
        api_response = await api_instance.get_dag_runs(dag_id, limit=limit, offset=offset, execution_date_gte=execution_date_gte, execution_date_lte=execution_date_lte, start_date_gte=start_date_gte, start_date_lte=start_date_lte, end_date_gte=end_date_gte, end_date_lte=end_date_lte, updated_at_gte=updated_at_gte, updated_at_lte=updated_at_lte, state=state, order_by=order_by, fields=fields)
        print("The response of DAGRunApi->get_dag_runs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DAGRunApi->get_dag_runs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**| The DAG ID. | 
 **limit** | **int**| The numbers of items to return. | [optional] [default to 100]
 **offset** | **int**| The number of items to skip before starting to collect the result set. | [optional] 
 **execution_date_gte** | **datetime**| Returns objects greater or equal to the specified date.  This can be combined with execution_date_lte parameter to receive only the selected period.  | [optional] 
 **execution_date_lte** | **datetime**| Returns objects less than or equal to the specified date.  This can be combined with execution_date_gte parameter to receive only the selected period.  | [optional] 
 **start_date_gte** | **datetime**| Returns objects greater or equal the specified date.  This can be combined with start_date_lte parameter to receive only the selected period.  | [optional] 
 **start_date_lte** | **datetime**| Returns objects less or equal the specified date.  This can be combined with start_date_gte parameter to receive only the selected period.  | [optional] 
 **end_date_gte** | **datetime**| Returns objects greater or equal the specified date.  This can be combined with start_date_lte parameter to receive only the selected period.  | [optional] 
 **end_date_lte** | **datetime**| Returns objects less than or equal to the specified date.  This can be combined with start_date_gte parameter to receive only the selected period.  | [optional] 
 **updated_at_gte** | **datetime**| Returns objects greater or equal the specified date.  This can be combined with updated_at_lte parameter to receive only the selected period.  *New in version 2.6.0*  | [optional] 
 **updated_at_lte** | **datetime**| Returns objects less or equal the specified date.  This can be combined with updated_at_gte parameter to receive only the selected period.  *New in version 2.6.0*  | [optional] 
 **state** | [**List[str]**](str.md)| The value can be repeated to retrieve multiple matching values (OR condition). | [optional] 
 **order_by** | **str**| The name of the field to order the results by. Prefix a field name with &#x60;-&#x60; to reverse the sort order.  *New in version 2.1.0*  | [optional] 
 **fields** | [**List[str]**](str.md)| List of field for return.  | [optional] 

### Return type

[**TitaniumTitaniumDAGRunCollection**](TitaniumDAGRunCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of DAG runs. |  -  |
**401** | Request not authenticated due to missing, invalid, authentication info. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dag_runs_batch**
> TitaniumTitaniumDAGRunCollection get_dag_runs_batch(titanium_list_dag_runs_form)

List DAG runs (batch)

This endpoint is a POST to allow filtering across a large number of DAG IDs, where as a GET it would run in to maximum HTTP request URL length limit. 

### Example


```python
import titanium_airflow_client
from titanium_airflow_client.models.titanium_list_dag_runs_form import TitaniumListDagRunsForm
from titanium_airflow_client.models.titanium_titanium_dag_run_collection import TitaniumTitaniumDAGRunCollection
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
    api_instance = titanium_airflow_client.DAGRunApi(api_client)
    titanium_list_dag_runs_form = titanium_airflow_client.TitaniumListDagRunsForm() # TitaniumListDagRunsForm | 

    try:
        # List DAG runs (batch)
        api_response = await api_instance.get_dag_runs_batch(titanium_list_dag_runs_form)
        print("The response of DAGRunApi->get_dag_runs_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DAGRunApi->get_dag_runs_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **titanium_list_dag_runs_form** | [**TitaniumListDagRunsForm**](TitaniumListDagRunsForm.md)|  | 

### Return type

[**TitaniumTitaniumDAGRunCollection**](TitaniumDAGRunCollection.md)

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

# **get_upstream_dataset_events**
> TitaniumTitaniumDatasetEventCollection get_upstream_dataset_events(dag_id, dag_run_id)

Get dataset events for a DAG run

Get datasets for a dag run.  *New in version 2.4.0* 

### Example


```python
import titanium_airflow_client
from titanium_airflow_client.models.titanium_titanium_dataset_event_collection import TitaniumTitaniumDatasetEventCollection
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
    api_instance = titanium_airflow_client.DAGRunApi(api_client)
    dag_id = 'dag_id_example' # str | The DAG ID.
    dag_run_id = 'dag_run_id_example' # str | The DAG run ID.

    try:
        # Get dataset events for a DAG run
        api_response = await api_instance.get_upstream_dataset_events(dag_id, dag_run_id)
        print("The response of DAGRunApi->get_upstream_dataset_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DAGRunApi->get_upstream_dataset_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**| The DAG ID. | 
 **dag_run_id** | **str**| The DAG run ID. | 

### Return type

[**TitaniumTitaniumDatasetEventCollection**](TitaniumDatasetEventCollection.md)

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

# **post_dag_run**
> TitaniumTitaniumDAGRun post_dag_run(dag_id, titanium_dag_run)

Trigger a new DAG run.

This will initiate a dagrun. If DAG is paused then dagrun state will remain queued, and the task won't run. 

### Example


```python
import titanium_airflow_client
from titanium_airflow_client.models.titanium_dag_run import TitaniumDAGRun
from titanium_airflow_client.models.titanium_titanium_dag_run import TitaniumTitaniumDAGRun
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
    api_instance = titanium_airflow_client.DAGRunApi(api_client)
    dag_id = 'dag_id_example' # str | The DAG ID.
    titanium_dag_run = titanium_airflow_client.TitaniumDAGRun() # TitaniumDAGRun | 

    try:
        # Trigger a new DAG run.
        api_response = await api_instance.post_dag_run(dag_id, titanium_dag_run)
        print("The response of DAGRunApi->post_dag_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DAGRunApi->post_dag_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**| The DAG ID. | 
 **titanium_dag_run** | [**TitaniumDAGRun**](TitaniumDAGRun.md)|  | 

### Return type

[**TitaniumTitaniumDAGRun**](TitaniumDAGRun.md)

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
**409** | An existing resource conflicts with the request. |  -  |
**403** | Client does not have sufficient permission. |  -  |
**404** | A specified resource is not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_dag_run_note**
> TitaniumTitaniumDAGRun set_dag_run_note(dag_id, dag_run_id, titanium_set_dag_run_note)

Update the DagRun note.

Update the manual user note of a DagRun.  *New in version 2.5.0* 

### Example


```python
import titanium_airflow_client
from titanium_airflow_client.models.titanium_set_dag_run_note import TitaniumSetDagRunNote
from titanium_airflow_client.models.titanium_titanium_dag_run import TitaniumTitaniumDAGRun
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
    api_instance = titanium_airflow_client.DAGRunApi(api_client)
    dag_id = 'dag_id_example' # str | The DAG ID.
    dag_run_id = 'dag_run_id_example' # str | The DAG run ID.
    titanium_set_dag_run_note = titanium_airflow_client.TitaniumSetDagRunNote() # TitaniumSetDagRunNote | Parameters of set DagRun note.

    try:
        # Update the DagRun note.
        api_response = await api_instance.set_dag_run_note(dag_id, dag_run_id, titanium_set_dag_run_note)
        print("The response of DAGRunApi->set_dag_run_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DAGRunApi->set_dag_run_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**| The DAG ID. | 
 **dag_run_id** | **str**| The DAG run ID. | 
 **titanium_set_dag_run_note** | [**TitaniumSetDagRunNote**](TitaniumSetDagRunNote.md)| Parameters of set DagRun note. | 

### Return type

[**TitaniumTitaniumDAGRun**](TitaniumDAGRun.md)

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

# **update_dag_run_state**
> TitaniumTitaniumDAGRun update_dag_run_state(dag_id, dag_run_id, titanium_update_dag_run_state)

Modify a DAG run

Modify a DAG run.  *New in version 2.2.0* 

### Example


```python
import titanium_airflow_client
from titanium_airflow_client.models.titanium_titanium_dag_run import TitaniumTitaniumDAGRun
from titanium_airflow_client.models.titanium_update_dag_run_state import TitaniumUpdateDagRunState
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
    api_instance = titanium_airflow_client.DAGRunApi(api_client)
    dag_id = 'dag_id_example' # str | The DAG ID.
    dag_run_id = 'dag_run_id_example' # str | The DAG run ID.
    titanium_update_dag_run_state = titanium_airflow_client.TitaniumUpdateDagRunState() # TitaniumUpdateDagRunState | 

    try:
        # Modify a DAG run
        api_response = await api_instance.update_dag_run_state(dag_id, dag_run_id, titanium_update_dag_run_state)
        print("The response of DAGRunApi->update_dag_run_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DAGRunApi->update_dag_run_state: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**| The DAG ID. | 
 **dag_run_id** | **str**| The DAG run ID. | 
 **titanium_update_dag_run_state** | [**TitaniumUpdateDagRunState**](TitaniumUpdateDagRunState.md)|  | 

### Return type

[**TitaniumTitaniumDAGRun**](TitaniumDAGRun.md)

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

