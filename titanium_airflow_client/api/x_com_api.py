# coding: utf-8

"""
    Airflow API (Stable)

    # Overview  To facilitate management, Apache Airflow supports a range of REST API endpoints across its objects. This section provides an overview of the API design, methods, and supported use cases.  Most of the endpoints accept `JSON` as input and return `JSON` responses. This means that you must usually add the following headers to your request: ``` Content-type: application/json Accept: application/json ```  ## Resources  The term `resource` refers to a single type of object in the Airflow metadata. An API is broken up by its endpoint's corresponding resource. The name of a resource is typically plural and expressed in camelCase. Example: `dagRuns`.  Resource names are used as part of endpoint URLs, as well as in API parameters and responses.  ## CRUD Operations  The platform supports **C**reate, **R**ead, **U**pdate, and **D**elete operations on most resources. You can review the standards for these operations and their standard parameters below.  Some endpoints have special behavior as exceptions.  ### Create  To create a resource, you typically submit an HTTP `POST` request with the resource's required metadata in the request body. The response returns a `201 Created` response code upon success with the resource's metadata, including its internal `id`, in the response body.  ### Read  The HTTP `GET` request can be used to read a resource or to list a number of resources.  A resource's `id` can be submitted in the request parameters to read a specific resource. The response usually returns a `200 OK` response code upon success, with the resource's metadata in the response body.  If a `GET` request does not include a specific resource `id`, it is treated as a list request. The response usually returns a `200 OK` response code upon success, with an object containing a list of resources' metadata in the response body.  When reading resources, some common query parameters are usually available. e.g.: ``` v1/connections?limit=25&offset=25 ```  |Query Parameter|Type|Description| |---------------|----|-----------| |limit|integer|Maximum number of objects to fetch. Usually 25 by default| |offset|integer|Offset after which to start returning objects. For use with limit query parameter.|  ### Update  Updating a resource requires the resource `id`, and is typically done using an HTTP `PATCH` request, with the fields to modify in the request body. The response usually returns a `200 OK` response code upon success, with information about the modified resource in the response body.  ### Delete  Deleting a resource requires the resource `id` and is typically executed via an HTTP `DELETE` request. The response usually returns a `204 No Content` response code upon success.  ## Conventions  - Resource names are plural and expressed in camelCase. - Names are consistent between URL parameter name and field name.  - Field names are in snake_case. ```json {     \"description\": \"string\",     \"name\": \"string\",     \"occupied_slots\": 0,     \"open_slots\": 0     \"queued_slots\": 0,     \"running_slots\": 0,     \"scheduled_slots\": 0,     \"slots\": 0, } ```  ### Update Mask  Update mask is available as a query parameter in patch endpoints. It is used to notify the API which fields you want to update. Using `update_mask` makes it easier to update objects by helping the server know which fields to update in an object instead of updating all fields. The update request ignores any fields that aren't specified in the field mask, leaving them with their current values.  Example: ```   resource = request.get('/resource/my-id').json()   resource['my_field'] = 'new-value'   request.patch('/resource/my-id?update_mask=my_field', data=json.dumps(resource)) ```  ## Versioning and Endpoint Lifecycle  - API versioning is not synchronized to specific releases of the Apache Airflow. - APIs are designed to be backward compatible. - Any changes to the API will first go through a deprecation phase.  # Trying the API  You can use a third party client, such as [curl](https://curl.haxx.se/), [HTTPie](https://httpie.org/), [Postman](https://www.postman.com/) or [the Insomnia rest client](https://insomnia.rest/) to test the Apache Airflow API.  Note that you will need to pass credentials data.  For e.g., here is how to pause a DAG with [curl](https://curl.haxx.se/), when basic authorization is used: ```bash curl -X PATCH 'https://example.com/api/v1/dags/{dag_id}?update_mask=is_paused' \\ -H 'Content-Type: application/json' \\ --user \"username:password\" \\ -d '{     \"is_paused\": true }' ```  Using a graphical tool such as [Postman](https://www.postman.com/) or [Insomnia](https://insomnia.rest/), it is possible to import the API specifications directly:  1. Download the API specification by clicking the **Download** button at the top of this document 2. Import the JSON specification in the graphical tool of your choice.   - In *Postman*, you can click the **import** button at the top   - With *Insomnia*, you can just drag-and-drop the file on the UI  Note that with *Postman*, you can also generate code snippets by selecting a request and clicking on the **Code** button.  ## Enabling CORS  [Cross-origin resource sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) is a browser security feature that restricts HTTP requests that are initiated from scripts running in the browser.  For details on enabling/configuring CORS, see [Enabling CORS](https://airflow.apache.org/docs/apache-airflow/stable/security/api.html).  # Authentication  To be able to meet the requirements of many organizations, Airflow supports many authentication methods, and it is even possible to add your own method.  If you want to check which auth backend is currently set, you can use `airflow config get-value api auth_backends` command as in the example below. ```bash $ airflow config get-value api auth_backends airflow.api.auth.backend.basic_auth ``` The default is to deny all requests.  For details on configuring the authentication, see [API Authorization](https://airflow.apache.org/docs/apache-airflow/stable/security/api.html).  # Errors  We follow the error response format proposed in [RFC 7807](https://tools.ietf.org/html/rfc7807) also known as Problem Details for HTTP APIs. As with our normal API responses, your client must be prepared to gracefully handle additional members of the response.  ## Unauthenticated  This indicates that the request has not been applied because it lacks valid authentication credentials for the target resource. Please check that you have valid credentials.  ## PermissionDenied  This response means that the server understood the request but refuses to authorize it because it lacks sufficient rights to the resource. It happens when you do not have the necessary permission to execute the action you performed. You need to get the appropriate permissions in other to resolve this error.  ## BadRequest  This response means that the server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). To resolve this, please ensure that your syntax is correct.  ## NotFound  This client error response indicates that the server cannot find the requested resource.  ## MethodNotAllowed  Indicates that the request method is known by the server but is not supported by the target resource.  ## NotAcceptable  The target resource does not have a current representation that would be acceptable to the user agent, according to the proactive negotiation header fields received in the request, and the server is unwilling to supply a default representation.  ## AlreadyExists  The request could not be completed due to a conflict with the current state of the target resource, e.g. the resource it tries to create already exists.  ## Unknown  This means that the server encountered an unexpected condition that prevented it from fulfilling the request. 

    The version of the OpenAPI document: 2.9.2
    Contact: dev@airflow.apache.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import Field, StrictBool, StrictInt, StrictStr
from typing import Optional
from typing_extensions import Annotated
from titanium_airflow_client.models.x_com import XCom
from titanium_airflow_client.models.x_com_collection import XComCollection

from titanium_airflow_client.api_client import ApiClient, RequestSerialized
from titanium_airflow_client.api_response import ApiResponse
from titanium_airflow_client.rest import RESTResponseType


class XComApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def get_xcom_entries(
        self,
        dag_id: Annotated[StrictStr, Field(description="The DAG ID.")],
        dag_run_id: Annotated[StrictStr, Field(description="The DAG run ID.")],
        task_id: Annotated[StrictStr, Field(description="The task ID.")],
        map_index: Annotated[Optional[StrictInt], Field(description="Filter on map index for mapped task.")] = None,
        xcom_key: Annotated[Optional[StrictStr], Field(description="Only filter the XCom records which have the provided key.")] = None,
        limit: Annotated[Optional[StrictInt], Field(description="The numbers of items to return.")] = None,
        offset: Annotated[Optional[Annotated[int, Field(strict=True, ge=0)]], Field(description="The number of items to skip before starting to collect the result set.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> XComCollection:
        """List XCom entries

        This endpoint allows specifying `~` as the dag_id, dag_run_id, task_id to retrieve XCOM entries for for all DAGs, DAG runs and task instances. XCom values won't be returned as they can be large. Use this endpoint to get a list of XCom entries and then fetch individual entry to get value.

        :param dag_id: The DAG ID. (required)
        :type dag_id: str
        :param dag_run_id: The DAG run ID. (required)
        :type dag_run_id: str
        :param task_id: The task ID. (required)
        :type task_id: str
        :param map_index: Filter on map index for mapped task.
        :type map_index: int
        :param xcom_key: Only filter the XCom records which have the provided key.
        :type xcom_key: str
        :param limit: The numbers of items to return.
        :type limit: int
        :param offset: The number of items to skip before starting to collect the result set.
        :type offset: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_xcom_entries_serialize(
            dag_id=dag_id,
            dag_run_id=dag_run_id,
            task_id=task_id,
            map_index=map_index,
            xcom_key=xcom_key,
            limit=limit,
            offset=offset,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "XComCollection",
            '401': "Error",
            '403': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def get_xcom_entries_with_http_info(
        self,
        dag_id: Annotated[StrictStr, Field(description="The DAG ID.")],
        dag_run_id: Annotated[StrictStr, Field(description="The DAG run ID.")],
        task_id: Annotated[StrictStr, Field(description="The task ID.")],
        map_index: Annotated[Optional[StrictInt], Field(description="Filter on map index for mapped task.")] = None,
        xcom_key: Annotated[Optional[StrictStr], Field(description="Only filter the XCom records which have the provided key.")] = None,
        limit: Annotated[Optional[StrictInt], Field(description="The numbers of items to return.")] = None,
        offset: Annotated[Optional[Annotated[int, Field(strict=True, ge=0)]], Field(description="The number of items to skip before starting to collect the result set.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[XComCollection]:
        """List XCom entries

        This endpoint allows specifying `~` as the dag_id, dag_run_id, task_id to retrieve XCOM entries for for all DAGs, DAG runs and task instances. XCom values won't be returned as they can be large. Use this endpoint to get a list of XCom entries and then fetch individual entry to get value.

        :param dag_id: The DAG ID. (required)
        :type dag_id: str
        :param dag_run_id: The DAG run ID. (required)
        :type dag_run_id: str
        :param task_id: The task ID. (required)
        :type task_id: str
        :param map_index: Filter on map index for mapped task.
        :type map_index: int
        :param xcom_key: Only filter the XCom records which have the provided key.
        :type xcom_key: str
        :param limit: The numbers of items to return.
        :type limit: int
        :param offset: The number of items to skip before starting to collect the result set.
        :type offset: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_xcom_entries_serialize(
            dag_id=dag_id,
            dag_run_id=dag_run_id,
            task_id=task_id,
            map_index=map_index,
            xcom_key=xcom_key,
            limit=limit,
            offset=offset,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "XComCollection",
            '401': "Error",
            '403': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def get_xcom_entries_without_preload_content(
        self,
        dag_id: Annotated[StrictStr, Field(description="The DAG ID.")],
        dag_run_id: Annotated[StrictStr, Field(description="The DAG run ID.")],
        task_id: Annotated[StrictStr, Field(description="The task ID.")],
        map_index: Annotated[Optional[StrictInt], Field(description="Filter on map index for mapped task.")] = None,
        xcom_key: Annotated[Optional[StrictStr], Field(description="Only filter the XCom records which have the provided key.")] = None,
        limit: Annotated[Optional[StrictInt], Field(description="The numbers of items to return.")] = None,
        offset: Annotated[Optional[Annotated[int, Field(strict=True, ge=0)]], Field(description="The number of items to skip before starting to collect the result set.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """List XCom entries

        This endpoint allows specifying `~` as the dag_id, dag_run_id, task_id to retrieve XCOM entries for for all DAGs, DAG runs and task instances. XCom values won't be returned as they can be large. Use this endpoint to get a list of XCom entries and then fetch individual entry to get value.

        :param dag_id: The DAG ID. (required)
        :type dag_id: str
        :param dag_run_id: The DAG run ID. (required)
        :type dag_run_id: str
        :param task_id: The task ID. (required)
        :type task_id: str
        :param map_index: Filter on map index for mapped task.
        :type map_index: int
        :param xcom_key: Only filter the XCom records which have the provided key.
        :type xcom_key: str
        :param limit: The numbers of items to return.
        :type limit: int
        :param offset: The number of items to skip before starting to collect the result set.
        :type offset: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_xcom_entries_serialize(
            dag_id=dag_id,
            dag_run_id=dag_run_id,
            task_id=task_id,
            map_index=map_index,
            xcom_key=xcom_key,
            limit=limit,
            offset=offset,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "XComCollection",
            '401': "Error",
            '403': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_xcom_entries_serialize(
        self,
        dag_id,
        dag_run_id,
        task_id,
        map_index,
        xcom_key,
        limit,
        offset,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if dag_id is not None:
            _path_params['dag_id'] = dag_id
        if dag_run_id is not None:
            _path_params['dag_run_id'] = dag_run_id
        if task_id is not None:
            _path_params['task_id'] = task_id
        # process the query parameters
        if map_index is not None:
            
            _query_params.append(('map_index', map_index))
            
        if xcom_key is not None:
            
            _query_params.append(('xcom_key', xcom_key))
            
        if limit is not None:
            
            _query_params.append(('limit', limit))
            
        if offset is not None:
            
            _query_params.append(('offset', offset))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'application/json'
            ]
        )


        # authentication setting
        _auth_settings: List[str] = [
            'Basic', 
            'Kerberos', 
            'GoogleOpenId'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/xcomEntries',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def get_xcom_entry(
        self,
        dag_id: Annotated[StrictStr, Field(description="The DAG ID.")],
        dag_run_id: Annotated[StrictStr, Field(description="The DAG run ID.")],
        task_id: Annotated[StrictStr, Field(description="The task ID.")],
        xcom_key: Annotated[StrictStr, Field(description="The XCom key.")],
        map_index: Annotated[Optional[StrictInt], Field(description="Filter on map index for mapped task.")] = None,
        deserialize: Annotated[Optional[StrictBool], Field(description="Whether to deserialize an XCom value when using a custom XCom backend.  The XCom API endpoint calls `orm_deserialize_value` by default since an XCom may contain value that is potentially expensive to deserialize in the web server. Setting this to true overrides the consideration, and calls `deserialize_value` instead.  This parameter is not meaningful when using the default XCom backend.  *New in version 2.4.0* ")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> XCom:
        """Get an XCom entry


        :param dag_id: The DAG ID. (required)
        :type dag_id: str
        :param dag_run_id: The DAG run ID. (required)
        :type dag_run_id: str
        :param task_id: The task ID. (required)
        :type task_id: str
        :param xcom_key: The XCom key. (required)
        :type xcom_key: str
        :param map_index: Filter on map index for mapped task.
        :type map_index: int
        :param deserialize: Whether to deserialize an XCom value when using a custom XCom backend.  The XCom API endpoint calls `orm_deserialize_value` by default since an XCom may contain value that is potentially expensive to deserialize in the web server. Setting this to true overrides the consideration, and calls `deserialize_value` instead.  This parameter is not meaningful when using the default XCom backend.  *New in version 2.4.0* 
        :type deserialize: bool
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_xcom_entry_serialize(
            dag_id=dag_id,
            dag_run_id=dag_run_id,
            task_id=task_id,
            xcom_key=xcom_key,
            map_index=map_index,
            deserialize=deserialize,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "XCom",
            '401': "Error",
            '403': "Error",
            '404': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def get_xcom_entry_with_http_info(
        self,
        dag_id: Annotated[StrictStr, Field(description="The DAG ID.")],
        dag_run_id: Annotated[StrictStr, Field(description="The DAG run ID.")],
        task_id: Annotated[StrictStr, Field(description="The task ID.")],
        xcom_key: Annotated[StrictStr, Field(description="The XCom key.")],
        map_index: Annotated[Optional[StrictInt], Field(description="Filter on map index for mapped task.")] = None,
        deserialize: Annotated[Optional[StrictBool], Field(description="Whether to deserialize an XCom value when using a custom XCom backend.  The XCom API endpoint calls `orm_deserialize_value` by default since an XCom may contain value that is potentially expensive to deserialize in the web server. Setting this to true overrides the consideration, and calls `deserialize_value` instead.  This parameter is not meaningful when using the default XCom backend.  *New in version 2.4.0* ")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[XCom]:
        """Get an XCom entry


        :param dag_id: The DAG ID. (required)
        :type dag_id: str
        :param dag_run_id: The DAG run ID. (required)
        :type dag_run_id: str
        :param task_id: The task ID. (required)
        :type task_id: str
        :param xcom_key: The XCom key. (required)
        :type xcom_key: str
        :param map_index: Filter on map index for mapped task.
        :type map_index: int
        :param deserialize: Whether to deserialize an XCom value when using a custom XCom backend.  The XCom API endpoint calls `orm_deserialize_value` by default since an XCom may contain value that is potentially expensive to deserialize in the web server. Setting this to true overrides the consideration, and calls `deserialize_value` instead.  This parameter is not meaningful when using the default XCom backend.  *New in version 2.4.0* 
        :type deserialize: bool
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_xcom_entry_serialize(
            dag_id=dag_id,
            dag_run_id=dag_run_id,
            task_id=task_id,
            xcom_key=xcom_key,
            map_index=map_index,
            deserialize=deserialize,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "XCom",
            '401': "Error",
            '403': "Error",
            '404': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def get_xcom_entry_without_preload_content(
        self,
        dag_id: Annotated[StrictStr, Field(description="The DAG ID.")],
        dag_run_id: Annotated[StrictStr, Field(description="The DAG run ID.")],
        task_id: Annotated[StrictStr, Field(description="The task ID.")],
        xcom_key: Annotated[StrictStr, Field(description="The XCom key.")],
        map_index: Annotated[Optional[StrictInt], Field(description="Filter on map index for mapped task.")] = None,
        deserialize: Annotated[Optional[StrictBool], Field(description="Whether to deserialize an XCom value when using a custom XCom backend.  The XCom API endpoint calls `orm_deserialize_value` by default since an XCom may contain value that is potentially expensive to deserialize in the web server. Setting this to true overrides the consideration, and calls `deserialize_value` instead.  This parameter is not meaningful when using the default XCom backend.  *New in version 2.4.0* ")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get an XCom entry


        :param dag_id: The DAG ID. (required)
        :type dag_id: str
        :param dag_run_id: The DAG run ID. (required)
        :type dag_run_id: str
        :param task_id: The task ID. (required)
        :type task_id: str
        :param xcom_key: The XCom key. (required)
        :type xcom_key: str
        :param map_index: Filter on map index for mapped task.
        :type map_index: int
        :param deserialize: Whether to deserialize an XCom value when using a custom XCom backend.  The XCom API endpoint calls `orm_deserialize_value` by default since an XCom may contain value that is potentially expensive to deserialize in the web server. Setting this to true overrides the consideration, and calls `deserialize_value` instead.  This parameter is not meaningful when using the default XCom backend.  *New in version 2.4.0* 
        :type deserialize: bool
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_xcom_entry_serialize(
            dag_id=dag_id,
            dag_run_id=dag_run_id,
            task_id=task_id,
            xcom_key=xcom_key,
            map_index=map_index,
            deserialize=deserialize,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "XCom",
            '401': "Error",
            '403': "Error",
            '404': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_xcom_entry_serialize(
        self,
        dag_id,
        dag_run_id,
        task_id,
        xcom_key,
        map_index,
        deserialize,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if dag_id is not None:
            _path_params['dag_id'] = dag_id
        if dag_run_id is not None:
            _path_params['dag_run_id'] = dag_run_id
        if task_id is not None:
            _path_params['task_id'] = task_id
        if xcom_key is not None:
            _path_params['xcom_key'] = xcom_key
        # process the query parameters
        if map_index is not None:
            
            _query_params.append(('map_index', map_index))
            
        if deserialize is not None:
            
            _query_params.append(('deserialize', deserialize))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'application/json'
            ]
        )


        # authentication setting
        _auth_settings: List[str] = [
            'Basic', 
            'Kerberos', 
            'GoogleOpenId'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/xcomEntries/{xcom_key}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


