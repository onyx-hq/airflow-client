# titanium_airflow_client.TaskInstanceApi

All URIs are relative to *https://airflow.apache.org/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_extra_links**](TaskInstanceApi.md#get_extra_links) | **GET** /dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/links | List extra links
[**get_log**](TaskInstanceApi.md#get_log) | **GET** /dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/logs/{task_try_number} | Get logs
[**get_mapped_task_instance**](TaskInstanceApi.md#get_mapped_task_instance) | **GET** /dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/{map_index} | Get a mapped task instance
[**get_mapped_task_instances**](TaskInstanceApi.md#get_mapped_task_instances) | **GET** /dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/listMapped | List mapped task instances
[**get_task_instance**](TaskInstanceApi.md#get_task_instance) | **GET** /dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id} | Get a task instance
[**get_task_instances**](TaskInstanceApi.md#get_task_instances) | **GET** /dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances | List task instances
[**get_task_instances_batch**](TaskInstanceApi.md#get_task_instances_batch) | **POST** /dags/~/dagRuns/~/taskInstances/list | List task instances (batch)
[**patch_mapped_task_instance**](TaskInstanceApi.md#patch_mapped_task_instance) | **PATCH** /dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/{map_index} | Updates the state of a mapped task instance
[**patch_task_instance**](TaskInstanceApi.md#patch_task_instance) | **PATCH** /dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id} | Updates the state of a task instance
[**set_mapped_task_instance_note**](TaskInstanceApi.md#set_mapped_task_instance_note) | **PATCH** /dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/{map_index}/setNote | Update the TaskInstance note.
[**set_task_instance_note**](TaskInstanceApi.md#set_task_instance_note) | **PATCH** /dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/setNote | Update the TaskInstance note.


# **get_extra_links**
> TitaniumTitaniumExtraLinkCollection get_extra_links(dag_id, dag_run_id, task_id)

List extra links

List extra links for task instance. 

### Example


```python
import titanium_airflow_client
from titanium_airflow_client.models.titanium_titanium_extra_link_collection import TitaniumTitaniumExtraLinkCollection
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
    api_instance = titanium_airflow_client.TaskInstanceApi(api_client)
    dag_id = 'dag_id_example' # str | The DAG ID.
    dag_run_id = 'dag_run_id_example' # str | The DAG run ID.
    task_id = 'task_id_example' # str | The task ID.

    try:
        # List extra links
        api_response = await api_instance.get_extra_links(dag_id, dag_run_id, task_id)
        print("The response of TaskInstanceApi->get_extra_links:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskInstanceApi->get_extra_links: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**| The DAG ID. | 
 **dag_run_id** | **str**| The DAG run ID. | 
 **task_id** | **str**| The task ID. | 

### Return type

[**TitaniumTitaniumExtraLinkCollection**](TitaniumExtraLinkCollection.md)

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

# **get_log**
> TitaniumTitaniumGetLog200Response get_log(dag_id, dag_run_id, task_id, task_try_number, full_content=full_content, map_index=map_index, token=token)

Get logs

Get logs for a specific task instance and its try number. To get log from specific character position, following way of using URLSafeSerializer can be used.  Example: ``` from itsdangerous.url_safe import URLSafeSerializer  request_url = f\"api/v1/dags/{DAG_ID}/dagRuns/{RUN_ID}/taskInstances/{TASK_ID}/logs/1\" key = app.config[\"SECRET_KEY\"] serializer = URLSafeSerializer(key) token = serializer.dumps({\"log_pos\": 10000})  response = self.client.get(     request_url,     query_string={\"token\": token},     headers={\"Accept\": \"text/plain\"},     environ_overrides={\"REMOTE_USER\": \"test\"}, ) continuation_token = response.json[\"continuation_token\"]     metadata = URLSafeSerializer(key).loads(continuation_token)     log_pos = metadata[\"log_pos\"]     end_of_log = metadata[\"end_of_log\"] ``` If log_pos is passed as 10000 like the above example, it renders the logs starting from char position 10000 to last (not the end as the logs may be tailing behind in running state). This way pagination can be done with metadata as part of the token. 

### Example


```python
import titanium_airflow_client
from titanium_airflow_client.models.titanium_titanium_get_log200_response import TitaniumTitaniumGetLog200Response
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
    api_instance = titanium_airflow_client.TaskInstanceApi(api_client)
    dag_id = 'dag_id_example' # str | The DAG ID.
    dag_run_id = 'dag_run_id_example' # str | The DAG run ID.
    task_id = 'task_id_example' # str | The task ID.
    task_try_number = 56 # int | The task try number.
    full_content = True # bool | A full content will be returned. By default, only the first fragment will be returned.  (optional)
    map_index = 56 # int | Filter on map index for mapped task. (optional)
    token = 'token_example' # str | A token that allows you to continue fetching logs. If passed, it will specify the location from which the download should be continued.  (optional)

    try:
        # Get logs
        api_response = await api_instance.get_log(dag_id, dag_run_id, task_id, task_try_number, full_content=full_content, map_index=map_index, token=token)
        print("The response of TaskInstanceApi->get_log:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskInstanceApi->get_log: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**| The DAG ID. | 
 **dag_run_id** | **str**| The DAG run ID. | 
 **task_id** | **str**| The task ID. | 
 **task_try_number** | **int**| The task try number. | 
 **full_content** | **bool**| A full content will be returned. By default, only the first fragment will be returned.  | [optional] 
 **map_index** | **int**| Filter on map index for mapped task. | [optional] 
 **token** | **str**| A token that allows you to continue fetching logs. If passed, it will specify the location from which the download should be continued.  | [optional] 

### Return type

[**TitaniumTitaniumGetLog200Response**](TitaniumGetLog200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**400** | Client specified an invalid argument. |  -  |
**401** | Request not authenticated due to missing, invalid, authentication info. |  -  |
**403** | Client does not have sufficient permission. |  -  |
**404** | A specified resource is not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mapped_task_instance**
> TitaniumTitaniumTaskInstance get_mapped_task_instance(dag_id, dag_run_id, task_id, map_index)

Get a mapped task instance

Get details of a mapped task instance.  *New in version 2.3.0* 

### Example


```python
import titanium_airflow_client
from titanium_airflow_client.models.titanium_titanium_task_instance import TitaniumTitaniumTaskInstance
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
    api_instance = titanium_airflow_client.TaskInstanceApi(api_client)
    dag_id = 'dag_id_example' # str | The DAG ID.
    dag_run_id = 'dag_run_id_example' # str | The DAG run ID.
    task_id = 'task_id_example' # str | The task ID.
    map_index = 56 # int | The map index.

    try:
        # Get a mapped task instance
        api_response = await api_instance.get_mapped_task_instance(dag_id, dag_run_id, task_id, map_index)
        print("The response of TaskInstanceApi->get_mapped_task_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskInstanceApi->get_mapped_task_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**| The DAG ID. | 
 **dag_run_id** | **str**| The DAG run ID. | 
 **task_id** | **str**| The task ID. | 
 **map_index** | **int**| The map index. | 

### Return type

[**TitaniumTitaniumTaskInstance**](TitaniumTaskInstance.md)

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

# **get_mapped_task_instances**
> TitaniumTitaniumTaskInstanceCollection get_mapped_task_instances(dag_id, dag_run_id, task_id, limit=limit, offset=offset, execution_date_gte=execution_date_gte, execution_date_lte=execution_date_lte, start_date_gte=start_date_gte, start_date_lte=start_date_lte, end_date_gte=end_date_gte, end_date_lte=end_date_lte, updated_at_gte=updated_at_gte, updated_at_lte=updated_at_lte, duration_gte=duration_gte, duration_lte=duration_lte, state=state, pool=pool, queue=queue, order_by=order_by)

List mapped task instances

Get details of all mapped task instances.  *New in version 2.3.0* 

### Example


```python
import titanium_airflow_client
from titanium_airflow_client.models.titanium_titanium_task_instance_collection import TitaniumTitaniumTaskInstanceCollection
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
    api_instance = titanium_airflow_client.TaskInstanceApi(api_client)
    dag_id = 'dag_id_example' # str | The DAG ID.
    dag_run_id = 'dag_run_id_example' # str | The DAG run ID.
    task_id = 'task_id_example' # str | The task ID.
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
    duration_gte = 3.4 # float | Returns objects greater than or equal to the specified values.  This can be combined with duration_lte parameter to receive only the selected period.  (optional)
    duration_lte = 3.4 # float | Returns objects less than or equal to the specified values.  This can be combined with duration_gte parameter to receive only the selected range.  (optional)
    state = ['state_example'] # List[str] | The value can be repeated to retrieve multiple matching values (OR condition). (optional)
    pool = ['pool_example'] # List[str] | The value can be repeated to retrieve multiple matching values (OR condition). (optional)
    queue = ['queue_example'] # List[str] | The value can be repeated to retrieve multiple matching values (OR condition). (optional)
    order_by = 'order_by_example' # str | The name of the field to order the results by. Prefix a field name with `-` to reverse the sort order.  *New in version 2.1.0*  (optional)

    try:
        # List mapped task instances
        api_response = await api_instance.get_mapped_task_instances(dag_id, dag_run_id, task_id, limit=limit, offset=offset, execution_date_gte=execution_date_gte, execution_date_lte=execution_date_lte, start_date_gte=start_date_gte, start_date_lte=start_date_lte, end_date_gte=end_date_gte, end_date_lte=end_date_lte, updated_at_gte=updated_at_gte, updated_at_lte=updated_at_lte, duration_gte=duration_gte, duration_lte=duration_lte, state=state, pool=pool, queue=queue, order_by=order_by)
        print("The response of TaskInstanceApi->get_mapped_task_instances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskInstanceApi->get_mapped_task_instances: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**| The DAG ID. | 
 **dag_run_id** | **str**| The DAG run ID. | 
 **task_id** | **str**| The task ID. | 
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
 **duration_gte** | **float**| Returns objects greater than or equal to the specified values.  This can be combined with duration_lte parameter to receive only the selected period.  | [optional] 
 **duration_lte** | **float**| Returns objects less than or equal to the specified values.  This can be combined with duration_gte parameter to receive only the selected range.  | [optional] 
 **state** | [**List[str]**](str.md)| The value can be repeated to retrieve multiple matching values (OR condition). | [optional] 
 **pool** | [**List[str]**](str.md)| The value can be repeated to retrieve multiple matching values (OR condition). | [optional] 
 **queue** | [**List[str]**](str.md)| The value can be repeated to retrieve multiple matching values (OR condition). | [optional] 
 **order_by** | **str**| The name of the field to order the results by. Prefix a field name with &#x60;-&#x60; to reverse the sort order.  *New in version 2.1.0*  | [optional] 

### Return type

[**TitaniumTitaniumTaskInstanceCollection**](TitaniumTaskInstanceCollection.md)

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

# **get_task_instance**
> TitaniumTitaniumTaskInstance get_task_instance(dag_id, dag_run_id, task_id)

Get a task instance

### Example


```python
import titanium_airflow_client
from titanium_airflow_client.models.titanium_titanium_task_instance import TitaniumTitaniumTaskInstance
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
    api_instance = titanium_airflow_client.TaskInstanceApi(api_client)
    dag_id = 'dag_id_example' # str | The DAG ID.
    dag_run_id = 'dag_run_id_example' # str | The DAG run ID.
    task_id = 'task_id_example' # str | The task ID.

    try:
        # Get a task instance
        api_response = await api_instance.get_task_instance(dag_id, dag_run_id, task_id)
        print("The response of TaskInstanceApi->get_task_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskInstanceApi->get_task_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**| The DAG ID. | 
 **dag_run_id** | **str**| The DAG run ID. | 
 **task_id** | **str**| The task ID. | 

### Return type

[**TitaniumTitaniumTaskInstance**](TitaniumTaskInstance.md)

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

# **get_task_instances**
> TitaniumTitaniumTaskInstanceCollection get_task_instances(dag_id, dag_run_id, execution_date_gte=execution_date_gte, execution_date_lte=execution_date_lte, start_date_gte=start_date_gte, start_date_lte=start_date_lte, end_date_gte=end_date_gte, end_date_lte=end_date_lte, updated_at_gte=updated_at_gte, updated_at_lte=updated_at_lte, duration_gte=duration_gte, duration_lte=duration_lte, state=state, pool=pool, queue=queue, limit=limit, offset=offset)

List task instances

This endpoint allows specifying `~` as the dag_id, dag_run_id to retrieve DAG runs for all DAGs and DAG runs. 

### Example


```python
import titanium_airflow_client
from titanium_airflow_client.models.titanium_titanium_task_instance_collection import TitaniumTitaniumTaskInstanceCollection
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
    api_instance = titanium_airflow_client.TaskInstanceApi(api_client)
    dag_id = 'dag_id_example' # str | The DAG ID.
    dag_run_id = 'dag_run_id_example' # str | The DAG run ID.
    execution_date_gte = '2013-10-20T19:20:30+01:00' # datetime | Returns objects greater or equal to the specified date.  This can be combined with execution_date_lte parameter to receive only the selected period.  (optional)
    execution_date_lte = '2013-10-20T19:20:30+01:00' # datetime | Returns objects less than or equal to the specified date.  This can be combined with execution_date_gte parameter to receive only the selected period.  (optional)
    start_date_gte = '2013-10-20T19:20:30+01:00' # datetime | Returns objects greater or equal the specified date.  This can be combined with start_date_lte parameter to receive only the selected period.  (optional)
    start_date_lte = '2013-10-20T19:20:30+01:00' # datetime | Returns objects less or equal the specified date.  This can be combined with start_date_gte parameter to receive only the selected period.  (optional)
    end_date_gte = '2013-10-20T19:20:30+01:00' # datetime | Returns objects greater or equal the specified date.  This can be combined with start_date_lte parameter to receive only the selected period.  (optional)
    end_date_lte = '2013-10-20T19:20:30+01:00' # datetime | Returns objects less than or equal to the specified date.  This can be combined with start_date_gte parameter to receive only the selected period.  (optional)
    updated_at_gte = '2013-10-20T19:20:30+01:00' # datetime | Returns objects greater or equal the specified date.  This can be combined with updated_at_lte parameter to receive only the selected period.  *New in version 2.6.0*  (optional)
    updated_at_lte = '2013-10-20T19:20:30+01:00' # datetime | Returns objects less or equal the specified date.  This can be combined with updated_at_gte parameter to receive only the selected period.  *New in version 2.6.0*  (optional)
    duration_gte = 3.4 # float | Returns objects greater than or equal to the specified values.  This can be combined with duration_lte parameter to receive only the selected period.  (optional)
    duration_lte = 3.4 # float | Returns objects less than or equal to the specified values.  This can be combined with duration_gte parameter to receive only the selected range.  (optional)
    state = ['state_example'] # List[str] | The value can be repeated to retrieve multiple matching values (OR condition). (optional)
    pool = ['pool_example'] # List[str] | The value can be repeated to retrieve multiple matching values (OR condition). (optional)
    queue = ['queue_example'] # List[str] | The value can be repeated to retrieve multiple matching values (OR condition). (optional)
    limit = 100 # int | The numbers of items to return. (optional) (default to 100)
    offset = 56 # int | The number of items to skip before starting to collect the result set. (optional)

    try:
        # List task instances
        api_response = await api_instance.get_task_instances(dag_id, dag_run_id, execution_date_gte=execution_date_gte, execution_date_lte=execution_date_lte, start_date_gte=start_date_gte, start_date_lte=start_date_lte, end_date_gte=end_date_gte, end_date_lte=end_date_lte, updated_at_gte=updated_at_gte, updated_at_lte=updated_at_lte, duration_gte=duration_gte, duration_lte=duration_lte, state=state, pool=pool, queue=queue, limit=limit, offset=offset)
        print("The response of TaskInstanceApi->get_task_instances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskInstanceApi->get_task_instances: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**| The DAG ID. | 
 **dag_run_id** | **str**| The DAG run ID. | 
 **execution_date_gte** | **datetime**| Returns objects greater or equal to the specified date.  This can be combined with execution_date_lte parameter to receive only the selected period.  | [optional] 
 **execution_date_lte** | **datetime**| Returns objects less than or equal to the specified date.  This can be combined with execution_date_gte parameter to receive only the selected period.  | [optional] 
 **start_date_gte** | **datetime**| Returns objects greater or equal the specified date.  This can be combined with start_date_lte parameter to receive only the selected period.  | [optional] 
 **start_date_lte** | **datetime**| Returns objects less or equal the specified date.  This can be combined with start_date_gte parameter to receive only the selected period.  | [optional] 
 **end_date_gte** | **datetime**| Returns objects greater or equal the specified date.  This can be combined with start_date_lte parameter to receive only the selected period.  | [optional] 
 **end_date_lte** | **datetime**| Returns objects less than or equal to the specified date.  This can be combined with start_date_gte parameter to receive only the selected period.  | [optional] 
 **updated_at_gte** | **datetime**| Returns objects greater or equal the specified date.  This can be combined with updated_at_lte parameter to receive only the selected period.  *New in version 2.6.0*  | [optional] 
 **updated_at_lte** | **datetime**| Returns objects less or equal the specified date.  This can be combined with updated_at_gte parameter to receive only the selected period.  *New in version 2.6.0*  | [optional] 
 **duration_gte** | **float**| Returns objects greater than or equal to the specified values.  This can be combined with duration_lte parameter to receive only the selected period.  | [optional] 
 **duration_lte** | **float**| Returns objects less than or equal to the specified values.  This can be combined with duration_gte parameter to receive only the selected range.  | [optional] 
 **state** | [**List[str]**](str.md)| The value can be repeated to retrieve multiple matching values (OR condition). | [optional] 
 **pool** | [**List[str]**](str.md)| The value can be repeated to retrieve multiple matching values (OR condition). | [optional] 
 **queue** | [**List[str]**](str.md)| The value can be repeated to retrieve multiple matching values (OR condition). | [optional] 
 **limit** | **int**| The numbers of items to return. | [optional] [default to 100]
 **offset** | **int**| The number of items to skip before starting to collect the result set. | [optional] 

### Return type

[**TitaniumTitaniumTaskInstanceCollection**](TitaniumTaskInstanceCollection.md)

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

# **get_task_instances_batch**
> TitaniumTitaniumTaskInstanceCollection get_task_instances_batch(titanium_list_task_instance_form)

List task instances (batch)

List task instances from all DAGs and DAG runs. This endpoint is a POST to allow filtering across a large number of DAG IDs, where as a GET it would run in to maximum HTTP request URL length limits. 

### Example


```python
import titanium_airflow_client
from titanium_airflow_client.models.titanium_list_task_instance_form import TitaniumListTaskInstanceForm
from titanium_airflow_client.models.titanium_titanium_task_instance_collection import TitaniumTitaniumTaskInstanceCollection
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
    api_instance = titanium_airflow_client.TaskInstanceApi(api_client)
    titanium_list_task_instance_form = titanium_airflow_client.TitaniumListTaskInstanceForm() # TitaniumListTaskInstanceForm | 

    try:
        # List task instances (batch)
        api_response = await api_instance.get_task_instances_batch(titanium_list_task_instance_form)
        print("The response of TaskInstanceApi->get_task_instances_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskInstanceApi->get_task_instances_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **titanium_list_task_instance_form** | [**TitaniumListTaskInstanceForm**](TitaniumListTaskInstanceForm.md)|  | 

### Return type

[**TitaniumTitaniumTaskInstanceCollection**](TitaniumTaskInstanceCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Request not authenticated due to missing, invalid, authentication info. |  -  |
**403** | Client does not have sufficient permission. |  -  |
**404** | A specified resource is not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_mapped_task_instance**
> TitaniumTitaniumTaskInstanceReference patch_mapped_task_instance(dag_id, dag_run_id, task_id, map_index, titanium_update_task_instance=titanium_update_task_instance)

Updates the state of a mapped task instance

Updates the state for single mapped task instance. *New in version 2.5.0* 

### Example


```python
import titanium_airflow_client
from titanium_airflow_client.models.titanium_titanium_task_instance_reference import TitaniumTitaniumTaskInstanceReference
from titanium_airflow_client.models.titanium_update_task_instance import TitaniumUpdateTaskInstance
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
    api_instance = titanium_airflow_client.TaskInstanceApi(api_client)
    dag_id = 'dag_id_example' # str | The DAG ID.
    dag_run_id = 'dag_run_id_example' # str | The DAG run ID.
    task_id = 'task_id_example' # str | The task ID.
    map_index = 56 # int | The map index.
    titanium_update_task_instance = titanium_airflow_client.TitaniumUpdateTaskInstance() # TitaniumUpdateTaskInstance | Parameters of action (optional)

    try:
        # Updates the state of a mapped task instance
        api_response = await api_instance.patch_mapped_task_instance(dag_id, dag_run_id, task_id, map_index, titanium_update_task_instance=titanium_update_task_instance)
        print("The response of TaskInstanceApi->patch_mapped_task_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskInstanceApi->patch_mapped_task_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**| The DAG ID. | 
 **dag_run_id** | **str**| The DAG run ID. | 
 **task_id** | **str**| The task ID. | 
 **map_index** | **int**| The map index. | 
 **titanium_update_task_instance** | [**TitaniumUpdateTaskInstance**](TitaniumUpdateTaskInstance.md)| Parameters of action | [optional] 

### Return type

[**TitaniumTitaniumTaskInstanceReference**](TitaniumTaskInstanceReference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Request not authenticated due to missing, invalid, authentication info. |  -  |
**403** | Client does not have sufficient permission. |  -  |
**404** | A specified resource is not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_task_instance**
> TitaniumTitaniumTaskInstanceReference patch_task_instance(dag_id, dag_run_id, task_id, titanium_update_task_instance)

Updates the state of a task instance

Updates the state for single task instance. *New in version 2.5.0* 

### Example


```python
import titanium_airflow_client
from titanium_airflow_client.models.titanium_titanium_task_instance_reference import TitaniumTitaniumTaskInstanceReference
from titanium_airflow_client.models.titanium_update_task_instance import TitaniumUpdateTaskInstance
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
    api_instance = titanium_airflow_client.TaskInstanceApi(api_client)
    dag_id = 'dag_id_example' # str | The DAG ID.
    dag_run_id = 'dag_run_id_example' # str | The DAG run ID.
    task_id = 'task_id_example' # str | The task ID.
    titanium_update_task_instance = titanium_airflow_client.TitaniumUpdateTaskInstance() # TitaniumUpdateTaskInstance | Parameters of action

    try:
        # Updates the state of a task instance
        api_response = await api_instance.patch_task_instance(dag_id, dag_run_id, task_id, titanium_update_task_instance)
        print("The response of TaskInstanceApi->patch_task_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskInstanceApi->patch_task_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**| The DAG ID. | 
 **dag_run_id** | **str**| The DAG run ID. | 
 **task_id** | **str**| The task ID. | 
 **titanium_update_task_instance** | [**TitaniumUpdateTaskInstance**](TitaniumUpdateTaskInstance.md)| Parameters of action | 

### Return type

[**TitaniumTitaniumTaskInstanceReference**](TitaniumTaskInstanceReference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Request not authenticated due to missing, invalid, authentication info. |  -  |
**403** | Client does not have sufficient permission. |  -  |
**404** | A specified resource is not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_mapped_task_instance_note**
> TitaniumTitaniumTaskInstance set_mapped_task_instance_note(dag_id, dag_run_id, task_id, map_index, titanium_set_task_instance_note)

Update the TaskInstance note.

Update the manual user note of a mapped Task Instance.  *New in version 2.5.0* 

### Example


```python
import titanium_airflow_client
from titanium_airflow_client.models.titanium_set_task_instance_note import TitaniumSetTaskInstanceNote
from titanium_airflow_client.models.titanium_titanium_task_instance import TitaniumTitaniumTaskInstance
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
    api_instance = titanium_airflow_client.TaskInstanceApi(api_client)
    dag_id = 'dag_id_example' # str | The DAG ID.
    dag_run_id = 'dag_run_id_example' # str | The DAG run ID.
    task_id = 'task_id_example' # str | The task ID.
    map_index = 56 # int | The map index.
    titanium_set_task_instance_note = titanium_airflow_client.TitaniumSetTaskInstanceNote() # TitaniumSetTaskInstanceNote | Parameters of set Task Instance note.

    try:
        # Update the TaskInstance note.
        api_response = await api_instance.set_mapped_task_instance_note(dag_id, dag_run_id, task_id, map_index, titanium_set_task_instance_note)
        print("The response of TaskInstanceApi->set_mapped_task_instance_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskInstanceApi->set_mapped_task_instance_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**| The DAG ID. | 
 **dag_run_id** | **str**| The DAG run ID. | 
 **task_id** | **str**| The task ID. | 
 **map_index** | **int**| The map index. | 
 **titanium_set_task_instance_note** | [**TitaniumSetTaskInstanceNote**](TitaniumSetTaskInstanceNote.md)| Parameters of set Task Instance note. | 

### Return type

[**TitaniumTitaniumTaskInstance**](TitaniumTaskInstance.md)

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

# **set_task_instance_note**
> TitaniumTitaniumTaskInstance set_task_instance_note(dag_id, dag_run_id, task_id, titanium_set_task_instance_note)

Update the TaskInstance note.

Update the manual user note of a non-mapped Task Instance.  *New in version 2.5.0* 

### Example


```python
import titanium_airflow_client
from titanium_airflow_client.models.titanium_set_task_instance_note import TitaniumSetTaskInstanceNote
from titanium_airflow_client.models.titanium_titanium_task_instance import TitaniumTitaniumTaskInstance
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
    api_instance = titanium_airflow_client.TaskInstanceApi(api_client)
    dag_id = 'dag_id_example' # str | The DAG ID.
    dag_run_id = 'dag_run_id_example' # str | The DAG run ID.
    task_id = 'task_id_example' # str | The task ID.
    titanium_set_task_instance_note = titanium_airflow_client.TitaniumSetTaskInstanceNote() # TitaniumSetTaskInstanceNote | Parameters of set Task Instance note.

    try:
        # Update the TaskInstance note.
        api_response = await api_instance.set_task_instance_note(dag_id, dag_run_id, task_id, titanium_set_task_instance_note)
        print("The response of TaskInstanceApi->set_task_instance_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskInstanceApi->set_task_instance_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**| The DAG ID. | 
 **dag_run_id** | **str**| The DAG run ID. | 
 **task_id** | **str**| The task ID. | 
 **titanium_set_task_instance_note** | [**TitaniumSetTaskInstanceNote**](TitaniumSetTaskInstanceNote.md)| Parameters of set Task Instance note. | 

### Return type

[**TitaniumTitaniumTaskInstance**](TitaniumTaskInstance.md)

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
