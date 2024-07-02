# titanium_airflow_client.DAGApi

All URIs are relative to *https://airflow.apache.org/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_dag**](DAGApi.md#delete_dag) | **DELETE** /dags/{dag_id} | Delete a DAG
[**get_dag**](DAGApi.md#get_dag) | **GET** /dags/{dag_id} | Get basic information about a DAG
[**get_dag_details**](DAGApi.md#get_dag_details) | **GET** /dags/{dag_id}/details | Get a simplified representation of DAG
[**get_dag_source**](DAGApi.md#get_dag_source) | **GET** /dagSources/{file_token} | Get a source code
[**get_dags**](DAGApi.md#get_dags) | **GET** /dags | List DAGs
[**get_task**](DAGApi.md#get_task) | **GET** /dags/{dag_id}/tasks/{task_id} | Get simplified representation of a task
[**get_tasks**](DAGApi.md#get_tasks) | **GET** /dags/{dag_id}/tasks | Get tasks for DAG
[**patch_dag**](DAGApi.md#patch_dag) | **PATCH** /dags/{dag_id} | Update a DAG
[**patch_dags**](DAGApi.md#patch_dags) | **PATCH** /dags | Update DAGs
[**post_clear_task_instances**](DAGApi.md#post_clear_task_instances) | **POST** /dags/{dag_id}/clearTaskInstances | Clear a set of task instances
[**post_set_task_instances_state**](DAGApi.md#post_set_task_instances_state) | **POST** /dags/{dag_id}/updateTaskInstancesState | Set a state of task instances


# **delete_dag**
> delete_dag(dag_id)

Delete a DAG

Deletes all metadata related to the DAG, including finished DAG Runs and Tasks. Logs are not deleted. This action cannot be undone.  *New in version 2.2.0* 

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
with titanium_airflow_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = titanium_airflow_client.DAGApi(api_client)
    dag_id = 'dag_id_example' # str | The DAG ID.

    try:
        # Delete a DAG
        api_instance.delete_dag(dag_id)
    except Exception as e:
        print("Exception when calling DAGApi->delete_dag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**| The DAG ID. | 

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
**409** | An existing resource conflicts with the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dag**
> DAG get_dag(dag_id, fields=fields)

Get basic information about a DAG

Presents only information available in database (DAGModel). If you need detailed information, consider using GET /dags/{dag_id}/details. 

### Example


```python
import titanium_airflow_client
from titanium_airflow_client.models.dag import DAG
from titanium_airflow_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://airflow.apache.org/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = titanium_airflow_client.Configuration(
    host = "https://airflow.apache.org/api/v1"
)


# Enter a context with an instance of the API client
with titanium_airflow_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = titanium_airflow_client.DAGApi(api_client)
    dag_id = 'dag_id_example' # str | The DAG ID.
    fields = ['fields_example'] # List[str] | List of field for return.  (optional)

    try:
        # Get basic information about a DAG
        api_response = api_instance.get_dag(dag_id, fields=fields)
        print("The response of DAGApi->get_dag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DAGApi->get_dag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**| The DAG ID. | 
 **fields** | [**List[str]**](str.md)| List of field for return.  | [optional] 

### Return type

[**DAG**](DAG.md)

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

# **get_dag_details**
> DAGDetail get_dag_details(dag_id, fields=fields)

Get a simplified representation of DAG

The response contains many DAG attributes, so the response can be large. If possible, consider using GET /dags/{dag_id}. 

### Example


```python
import titanium_airflow_client
from titanium_airflow_client.models.dag_detail import DAGDetail
from titanium_airflow_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://airflow.apache.org/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = titanium_airflow_client.Configuration(
    host = "https://airflow.apache.org/api/v1"
)


# Enter a context with an instance of the API client
with titanium_airflow_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = titanium_airflow_client.DAGApi(api_client)
    dag_id = 'dag_id_example' # str | The DAG ID.
    fields = ['fields_example'] # List[str] | List of field for return.  (optional)

    try:
        # Get a simplified representation of DAG
        api_response = api_instance.get_dag_details(dag_id, fields=fields)
        print("The response of DAGApi->get_dag_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DAGApi->get_dag_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**| The DAG ID. | 
 **fields** | [**List[str]**](str.md)| List of field for return.  | [optional] 

### Return type

[**DAGDetail**](DAGDetail.md)

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

# **get_dag_source**
> GetDagSource200Response get_dag_source(file_token)

Get a source code

Get a source code using file token. 

### Example


```python
import titanium_airflow_client
from titanium_airflow_client.models.get_dag_source200_response import GetDagSource200Response
from titanium_airflow_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://airflow.apache.org/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = titanium_airflow_client.Configuration(
    host = "https://airflow.apache.org/api/v1"
)


# Enter a context with an instance of the API client
with titanium_airflow_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = titanium_airflow_client.DAGApi(api_client)
    file_token = 'file_token_example' # str | The key containing the encrypted path to the file. Encryption and decryption take place only on the server. This prevents the client from reading an non-DAG file. This also ensures API extensibility, because the format of encrypted data may change. 

    try:
        # Get a source code
        api_response = api_instance.get_dag_source(file_token)
        print("The response of DAGApi->get_dag_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DAGApi->get_dag_source: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_token** | **str**| The key containing the encrypted path to the file. Encryption and decryption take place only on the server. This prevents the client from reading an non-DAG file. This also ensures API extensibility, because the format of encrypted data may change.  | 

### Return type

[**GetDagSource200Response**](GetDagSource200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, plain/text

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Request not authenticated due to missing, invalid, authentication info. |  -  |
**403** | Client does not have sufficient permission. |  -  |
**404** | A specified resource is not found. |  -  |
**406** | A specified Accept header is not allowed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dags**
> DAGCollection get_dags(limit=limit, offset=offset, order_by=order_by, tags=tags, only_active=only_active, paused=paused, fields=fields, dag_id_pattern=dag_id_pattern)

List DAGs

List DAGs in the database. `dag_id_pattern` can be set to match dags of a specific pattern 

### Example


```python
import titanium_airflow_client
from titanium_airflow_client.models.dag_collection import DAGCollection
from titanium_airflow_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://airflow.apache.org/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = titanium_airflow_client.Configuration(
    host = "https://airflow.apache.org/api/v1"
)


# Enter a context with an instance of the API client
with titanium_airflow_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = titanium_airflow_client.DAGApi(api_client)
    limit = 100 # int | The numbers of items to return. (optional) (default to 100)
    offset = 56 # int | The number of items to skip before starting to collect the result set. (optional)
    order_by = 'order_by_example' # str | The name of the field to order the results by. Prefix a field name with `-` to reverse the sort order.  *New in version 2.1.0*  (optional)
    tags = ['tags_example'] # List[str] | List of tags to filter results.  *New in version 2.2.0*  (optional)
    only_active = True # bool | Only filter active DAGs.  *New in version 2.1.1*  (optional) (default to True)
    paused = True # bool | Only filter paused/unpaused DAGs. If absent or null, it returns paused and unpaused DAGs.  *New in version 2.6.0*  (optional)
    fields = ['fields_example'] # List[str] | List of field for return.  (optional)
    dag_id_pattern = 'dag_id_pattern_example' # str | If set, only return DAGs with dag_ids matching this pattern.  (optional)

    try:
        # List DAGs
        api_response = api_instance.get_dags(limit=limit, offset=offset, order_by=order_by, tags=tags, only_active=only_active, paused=paused, fields=fields, dag_id_pattern=dag_id_pattern)
        print("The response of DAGApi->get_dags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DAGApi->get_dags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The numbers of items to return. | [optional] [default to 100]
 **offset** | **int**| The number of items to skip before starting to collect the result set. | [optional] 
 **order_by** | **str**| The name of the field to order the results by. Prefix a field name with &#x60;-&#x60; to reverse the sort order.  *New in version 2.1.0*  | [optional] 
 **tags** | [**List[str]**](str.md)| List of tags to filter results.  *New in version 2.2.0*  | [optional] 
 **only_active** | **bool**| Only filter active DAGs.  *New in version 2.1.1*  | [optional] [default to True]
 **paused** | **bool**| Only filter paused/unpaused DAGs. If absent or null, it returns paused and unpaused DAGs.  *New in version 2.6.0*  | [optional] 
 **fields** | [**List[str]**](str.md)| List of field for return.  | [optional] 
 **dag_id_pattern** | **str**| If set, only return DAGs with dag_ids matching this pattern.  | [optional] 

### Return type

[**DAGCollection**](DAGCollection.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task**
> Task get_task(dag_id, task_id)

Get simplified representation of a task

### Example


```python
import titanium_airflow_client
from titanium_airflow_client.models.task import Task
from titanium_airflow_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://airflow.apache.org/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = titanium_airflow_client.Configuration(
    host = "https://airflow.apache.org/api/v1"
)


# Enter a context with an instance of the API client
with titanium_airflow_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = titanium_airflow_client.DAGApi(api_client)
    dag_id = 'dag_id_example' # str | The DAG ID.
    task_id = 'task_id_example' # str | The task ID.

    try:
        # Get simplified representation of a task
        api_response = api_instance.get_task(dag_id, task_id)
        print("The response of DAGApi->get_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DAGApi->get_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**| The DAG ID. | 
 **task_id** | **str**| The task ID. | 

### Return type

[**Task**](Task.md)

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

# **get_tasks**
> TaskCollection get_tasks(dag_id, order_by=order_by)

Get tasks for DAG

### Example


```python
import titanium_airflow_client
from titanium_airflow_client.models.task_collection import TaskCollection
from titanium_airflow_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://airflow.apache.org/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = titanium_airflow_client.Configuration(
    host = "https://airflow.apache.org/api/v1"
)


# Enter a context with an instance of the API client
with titanium_airflow_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = titanium_airflow_client.DAGApi(api_client)
    dag_id = 'dag_id_example' # str | The DAG ID.
    order_by = 'order_by_example' # str | The name of the field to order the results by. Prefix a field name with `-` to reverse the sort order.  *New in version 2.1.0*  (optional)

    try:
        # Get tasks for DAG
        api_response = api_instance.get_tasks(dag_id, order_by=order_by)
        print("The response of DAGApi->get_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DAGApi->get_tasks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**| The DAG ID. | 
 **order_by** | **str**| The name of the field to order the results by. Prefix a field name with &#x60;-&#x60; to reverse the sort order.  *New in version 2.1.0*  | [optional] 

### Return type

[**TaskCollection**](TaskCollection.md)

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

# **patch_dag**
> DAG patch_dag(dag_id, dag, update_mask=update_mask)

Update a DAG

### Example


```python
import titanium_airflow_client
from titanium_airflow_client.models.dag import DAG
from titanium_airflow_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://airflow.apache.org/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = titanium_airflow_client.Configuration(
    host = "https://airflow.apache.org/api/v1"
)


# Enter a context with an instance of the API client
with titanium_airflow_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = titanium_airflow_client.DAGApi(api_client)
    dag_id = 'dag_id_example' # str | The DAG ID.
    dag = {"is_paused":true} # DAG | 
    update_mask = ['update_mask_example'] # List[str] | The fields to update on the resource. If absent or empty, all modifiable fields are updated. A comma-separated list of fully qualified names of fields.  (optional)

    try:
        # Update a DAG
        api_response = api_instance.patch_dag(dag_id, dag, update_mask=update_mask)
        print("The response of DAGApi->patch_dag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DAGApi->patch_dag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**| The DAG ID. | 
 **dag** | [**DAG**](DAG.md)|  | 
 **update_mask** | [**List[str]**](str.md)| The fields to update on the resource. If absent or empty, all modifiable fields are updated. A comma-separated list of fully qualified names of fields.  | [optional] 

### Return type

[**DAG**](DAG.md)

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

# **patch_dags**
> DAGCollection patch_dags(dag_id_pattern, dag, limit=limit, offset=offset, tags=tags, update_mask=update_mask, only_active=only_active)

Update DAGs

Update DAGs of a given dag_id_pattern using UpdateMask. This endpoint allows specifying `~` as the dag_id_pattern to update all DAGs. *New in version 2.3.0* 

### Example


```python
import titanium_airflow_client
from titanium_airflow_client.models.dag import DAG
from titanium_airflow_client.models.dag_collection import DAGCollection
from titanium_airflow_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://airflow.apache.org/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = titanium_airflow_client.Configuration(
    host = "https://airflow.apache.org/api/v1"
)


# Enter a context with an instance of the API client
with titanium_airflow_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = titanium_airflow_client.DAGApi(api_client)
    dag_id_pattern = 'dag_id_pattern_example' # str | If set, only update DAGs with dag_ids matching this pattern. 
    dag = {"is_paused":true} # DAG | 
    limit = 100 # int | The numbers of items to return. (optional) (default to 100)
    offset = 56 # int | The number of items to skip before starting to collect the result set. (optional)
    tags = ['tags_example'] # List[str] | List of tags to filter results.  *New in version 2.2.0*  (optional)
    update_mask = ['update_mask_example'] # List[str] | The fields to update on the resource. If absent or empty, all modifiable fields are updated. A comma-separated list of fully qualified names of fields.  (optional)
    only_active = True # bool | Only filter active DAGs.  *New in version 2.1.1*  (optional) (default to True)

    try:
        # Update DAGs
        api_response = api_instance.patch_dags(dag_id_pattern, dag, limit=limit, offset=offset, tags=tags, update_mask=update_mask, only_active=only_active)
        print("The response of DAGApi->patch_dags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DAGApi->patch_dags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id_pattern** | **str**| If set, only update DAGs with dag_ids matching this pattern.  | 
 **dag** | [**DAG**](DAG.md)|  | 
 **limit** | **int**| The numbers of items to return. | [optional] [default to 100]
 **offset** | **int**| The number of items to skip before starting to collect the result set. | [optional] 
 **tags** | [**List[str]**](str.md)| List of tags to filter results.  *New in version 2.2.0*  | [optional] 
 **update_mask** | [**List[str]**](str.md)| The fields to update on the resource. If absent or empty, all modifiable fields are updated. A comma-separated list of fully qualified names of fields.  | [optional] 
 **only_active** | **bool**| Only filter active DAGs.  *New in version 2.1.1*  | [optional] [default to True]

### Return type

[**DAGCollection**](DAGCollection.md)

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

# **post_clear_task_instances**
> TaskInstanceReferenceCollection post_clear_task_instances(dag_id, clear_task_instances)

Clear a set of task instances

Clears a set of task instances associated with the DAG for a specified date range. 

### Example


```python
import titanium_airflow_client
from titanium_airflow_client.models.clear_task_instances import ClearTaskInstances
from titanium_airflow_client.models.task_instance_reference_collection import TaskInstanceReferenceCollection
from titanium_airflow_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://airflow.apache.org/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = titanium_airflow_client.Configuration(
    host = "https://airflow.apache.org/api/v1"
)


# Enter a context with an instance of the API client
with titanium_airflow_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = titanium_airflow_client.DAGApi(api_client)
    dag_id = 'dag_id_example' # str | The DAG ID.
    clear_task_instances = titanium_airflow_client.ClearTaskInstances() # ClearTaskInstances | Parameters of action

    try:
        # Clear a set of task instances
        api_response = api_instance.post_clear_task_instances(dag_id, clear_task_instances)
        print("The response of DAGApi->post_clear_task_instances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DAGApi->post_clear_task_instances: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**| The DAG ID. | 
 **clear_task_instances** | [**ClearTaskInstances**](ClearTaskInstances.md)| Parameters of action | 

### Return type

[**TaskInstanceReferenceCollection**](TaskInstanceReferenceCollection.md)

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

# **post_set_task_instances_state**
> TaskInstanceReferenceCollection post_set_task_instances_state(dag_id, update_task_instances_state)

Set a state of task instances

Updates the state for multiple task instances simultaneously. 

### Example


```python
import titanium_airflow_client
from titanium_airflow_client.models.task_instance_reference_collection import TaskInstanceReferenceCollection
from titanium_airflow_client.models.update_task_instances_state import UpdateTaskInstancesState
from titanium_airflow_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://airflow.apache.org/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = titanium_airflow_client.Configuration(
    host = "https://airflow.apache.org/api/v1"
)


# Enter a context with an instance of the API client
with titanium_airflow_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = titanium_airflow_client.DAGApi(api_client)
    dag_id = 'dag_id_example' # str | The DAG ID.
    update_task_instances_state = titanium_airflow_client.UpdateTaskInstancesState() # UpdateTaskInstancesState | Parameters of action

    try:
        # Set a state of task instances
        api_response = api_instance.post_set_task_instances_state(dag_id, update_task_instances_state)
        print("The response of DAGApi->post_set_task_instances_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DAGApi->post_set_task_instances_state: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**| The DAG ID. | 
 **update_task_instances_state** | [**UpdateTaskInstancesState**](UpdateTaskInstancesState.md)| Parameters of action | 

### Return type

[**TaskInstanceReferenceCollection**](TaskInstanceReferenceCollection.md)

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

