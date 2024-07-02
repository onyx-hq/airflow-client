# coding: utf-8

# flake8: noqa

"""
    Airflow API (Stable)

    # Overview  To facilitate management, Apache Airflow supports a range of REST API endpoints across its objects. This section provides an overview of the API design, methods, and supported use cases.  Most of the endpoints accept `JSON` as input and return `JSON` responses. This means that you must usually add the following headers to your request: ``` Content-type: application/json Accept: application/json ```  ## Resources  The term `resource` refers to a single type of object in the Airflow metadata. An API is broken up by its endpoint's corresponding resource. The name of a resource is typically plural and expressed in camelCase. Example: `dagRuns`.  Resource names are used as part of endpoint URLs, as well as in API parameters and responses.  ## CRUD Operations  The platform supports **C**reate, **R**ead, **U**pdate, and **D**elete operations on most resources. You can review the standards for these operations and their standard parameters below.  Some endpoints have special behavior as exceptions.  ### Create  To create a resource, you typically submit an HTTP `POST` request with the resource's required metadata in the request body. The response returns a `201 Created` response code upon success with the resource's metadata, including its internal `id`, in the response body.  ### Read  The HTTP `GET` request can be used to read a resource or to list a number of resources.  A resource's `id` can be submitted in the request parameters to read a specific resource. The response usually returns a `200 OK` response code upon success, with the resource's metadata in the response body.  If a `GET` request does not include a specific resource `id`, it is treated as a list request. The response usually returns a `200 OK` response code upon success, with an object containing a list of resources' metadata in the response body.  When reading resources, some common query parameters are usually available. e.g.: ``` v1/connections?limit=25&offset=25 ```  |Query Parameter|Type|Description| |---------------|----|-----------| |limit|integer|Maximum number of objects to fetch. Usually 25 by default| |offset|integer|Offset after which to start returning objects. For use with limit query parameter.|  ### Update  Updating a resource requires the resource `id`, and is typically done using an HTTP `PATCH` request, with the fields to modify in the request body. The response usually returns a `200 OK` response code upon success, with information about the modified resource in the response body.  ### Delete  Deleting a resource requires the resource `id` and is typically executed via an HTTP `DELETE` request. The response usually returns a `204 No Content` response code upon success.  ## Conventions  - Resource names are plural and expressed in camelCase. - Names are consistent between URL parameter name and field name.  - Field names are in snake_case. ```json {     \"description\": \"string\",     \"name\": \"string\",     \"occupied_slots\": 0,     \"open_slots\": 0     \"queued_slots\": 0,     \"running_slots\": 0,     \"scheduled_slots\": 0,     \"slots\": 0, } ```  ### Update Mask  Update mask is available as a query parameter in patch endpoints. It is used to notify the API which fields you want to update. Using `update_mask` makes it easier to update objects by helping the server know which fields to update in an object instead of updating all fields. The update request ignores any fields that aren't specified in the field mask, leaving them with their current values.  Example: ```   resource = request.get('/resource/my-id').json()   resource['my_field'] = 'new-value'   request.patch('/resource/my-id?update_mask=my_field', data=json.dumps(resource)) ```  ## Versioning and Endpoint Lifecycle  - API versioning is not synchronized to specific releases of the Apache Airflow. - APIs are designed to be backward compatible. - Any changes to the API will first go through a deprecation phase.  # Trying the API  You can use a third party client, such as [curl](https://curl.haxx.se/), [HTTPie](https://httpie.org/), [Postman](https://www.postman.com/) or [the Insomnia rest client](https://insomnia.rest/) to test the Apache Airflow API.  Note that you will need to pass credentials data.  For e.g., here is how to pause a DAG with [curl](https://curl.haxx.se/), when basic authorization is used: ```bash curl -X PATCH 'https://example.com/api/v1/dags/{dag_id}?update_mask=is_paused' \\ -H 'Content-Type: application/json' \\ --user \"username:password\" \\ -d '{     \"is_paused\": true }' ```  Using a graphical tool such as [Postman](https://www.postman.com/) or [Insomnia](https://insomnia.rest/), it is possible to import the API specifications directly:  1. Download the API specification by clicking the **Download** button at the top of this document 2. Import the JSON specification in the graphical tool of your choice.   - In *Postman*, you can click the **import** button at the top   - With *Insomnia*, you can just drag-and-drop the file on the UI  Note that with *Postman*, you can also generate code snippets by selecting a request and clicking on the **Code** button.  ## Enabling CORS  [Cross-origin resource sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) is a browser security feature that restricts HTTP requests that are initiated from scripts running in the browser.  For details on enabling/configuring CORS, see [Enabling CORS](https://airflow.apache.org/docs/apache-airflow/stable/security/api.html).  # Authentication  To be able to meet the requirements of many organizations, Airflow supports many authentication methods, and it is even possible to add your own method.  If you want to check which auth backend is currently set, you can use `airflow config get-value api auth_backends` command as in the example below. ```bash $ airflow config get-value api auth_backends airflow.api.auth.backend.basic_auth ``` The default is to deny all requests.  For details on configuring the authentication, see [API Authorization](https://airflow.apache.org/docs/apache-airflow/stable/security/api.html).  # Errors  We follow the error response format proposed in [RFC 7807](https://tools.ietf.org/html/rfc7807) also known as Problem Details for HTTP APIs. As with our normal API responses, your client must be prepared to gracefully handle additional members of the response.  ## Unauthenticated  This indicates that the request has not been applied because it lacks valid authentication credentials for the target resource. Please check that you have valid credentials.  ## PermissionDenied  This response means that the server understood the request but refuses to authorize it because it lacks sufficient rights to the resource. It happens when you do not have the necessary permission to execute the action you performed. You need to get the appropriate permissions in other to resolve this error.  ## BadRequest  This response means that the server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). To resolve this, please ensure that your syntax is correct.  ## NotFound  This client error response indicates that the server cannot find the requested resource.  ## MethodNotAllowed  Indicates that the request method is known by the server but is not supported by the target resource.  ## NotAcceptable  The target resource does not have a current representation that would be acceptable to the user agent, according to the proactive negotiation header fields received in the request, and the server is unwilling to supply a default representation.  ## AlreadyExists  The request could not be completed due to a conflict with the current state of the target resource, e.g. the resource it tries to create already exists.  ## Unknown  This means that the server encountered an unexpected condition that prevented it from fulfilling the request. 

    The version of the OpenAPI document: 2.9.2
    Contact: dev@airflow.apache.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.0"

# import apis into sdk package
from titanium_airflow_client.api.config_api import ConfigApi
from titanium_airflow_client.api.connection_api import ConnectionApi
from titanium_airflow_client.api.dag_api import DAGApi
from titanium_airflow_client.api.dag_run_api import DAGRunApi
from titanium_airflow_client.api.dag_warning_api import DagWarningApi
from titanium_airflow_client.api.dataset_api import DatasetApi
from titanium_airflow_client.api.event_log_api import EventLogApi
from titanium_airflow_client.api.import_error_api import ImportErrorApi
from titanium_airflow_client.api.monitoring_api import MonitoringApi
from titanium_airflow_client.api.permission_api import PermissionApi
from titanium_airflow_client.api.plugin_api import PluginApi
from titanium_airflow_client.api.pool_api import PoolApi
from titanium_airflow_client.api.provider_api import ProviderApi
from titanium_airflow_client.api.role_api import RoleApi
from titanium_airflow_client.api.task_instance_api import TaskInstanceApi
from titanium_airflow_client.api.user_api import UserApi
from titanium_airflow_client.api.variable_api import VariableApi
from titanium_airflow_client.api.x_com_api import XComApi

# import ApiClient
from titanium_airflow_client.api_response import ApiResponse
from titanium_airflow_client.api_client import ApiClient
from titanium_airflow_client.configuration import Configuration
from titanium_airflow_client.exceptions import OpenApiException
from titanium_airflow_client.exceptions import ApiTypeError
from titanium_airflow_client.exceptions import ApiValueError
from titanium_airflow_client.exceptions import ApiKeyError
from titanium_airflow_client.exceptions import ApiAttributeError
from titanium_airflow_client.exceptions import ApiException

# import models into sdk package
from titanium_airflow_client.models.titanium_action import TitaniumAction
from titanium_airflow_client.models.titanium_action_collection import TitaniumActionCollection
from titanium_airflow_client.models.titanium_action_resource import TitaniumActionResource
from titanium_airflow_client.models.titanium_basic_dag_run import TitaniumBasicDAGRun
from titanium_airflow_client.models.titanium_class_reference import TitaniumClassReference
from titanium_airflow_client.models.titanium_clear_dag_run import TitaniumClearDagRun
from titanium_airflow_client.models.titanium_clear_dag_run200_response import TitaniumClearDagRun200Response
from titanium_airflow_client.models.titanium_clear_task_instances import TitaniumClearTaskInstances
from titanium_airflow_client.models.titanium_collection_info import TitaniumCollectionInfo
from titanium_airflow_client.models.titanium_config import TitaniumConfig
from titanium_airflow_client.models.titanium_config_option import TitaniumConfigOption
from titanium_airflow_client.models.titanium_config_section import TitaniumConfigSection
from titanium_airflow_client.models.titanium_connection import TitaniumConnection
from titanium_airflow_client.models.titanium_connection_collection import TitaniumConnectionCollection
from titanium_airflow_client.models.titanium_connection_collection_item import TitaniumConnectionCollectionItem
from titanium_airflow_client.models.titanium_connection_test import TitaniumConnectionTest
from titanium_airflow_client.models.titanium_create_dataset_event import TitaniumCreateDatasetEvent
from titanium_airflow_client.models.titanium_cron_expression import TitaniumCronExpression
from titanium_airflow_client.models.titanium_dag import TitaniumDAG
from titanium_airflow_client.models.titanium_dag_collection import TitaniumDAGCollection
from titanium_airflow_client.models.titanium_dag_detail import TitaniumDAGDetail
from titanium_airflow_client.models.titanium_dag_run import TitaniumDAGRun
from titanium_airflow_client.models.titanium_dag_run_collection import TitaniumDAGRunCollection
from titanium_airflow_client.models.titanium_dag_processor_status import TitaniumDagProcessorStatus
from titanium_airflow_client.models.titanium_dag_schedule_dataset_reference import TitaniumDagScheduleDatasetReference
from titanium_airflow_client.models.titanium_dag_state import TitaniumDagState
from titanium_airflow_client.models.titanium_dag_warning import TitaniumDagWarning
from titanium_airflow_client.models.titanium_dag_warning_collection import TitaniumDagWarningCollection
from titanium_airflow_client.models.titanium_dataset import TitaniumDataset
from titanium_airflow_client.models.titanium_dataset_collection import TitaniumDatasetCollection
from titanium_airflow_client.models.titanium_dataset_event import TitaniumDatasetEvent
from titanium_airflow_client.models.titanium_dataset_event_collection import TitaniumDatasetEventCollection
from titanium_airflow_client.models.titanium_error import TitaniumError
from titanium_airflow_client.models.titanium_event_log import TitaniumEventLog
from titanium_airflow_client.models.titanium_event_log_collection import TitaniumEventLogCollection
from titanium_airflow_client.models.titanium_extra_link import TitaniumExtraLink
from titanium_airflow_client.models.titanium_extra_link_collection import TitaniumExtraLinkCollection
from titanium_airflow_client.models.titanium_get_dag_source200_response import TitaniumGetDagSource200Response
from titanium_airflow_client.models.titanium_get_log200_response import TitaniumGetLog200Response
from titanium_airflow_client.models.titanium_get_providers200_response import TitaniumGetProviders200Response
from titanium_airflow_client.models.titanium_health_info import TitaniumHealthInfo
from titanium_airflow_client.models.titanium_health_status import TitaniumHealthStatus
from titanium_airflow_client.models.titanium_import_error import TitaniumImportError
from titanium_airflow_client.models.titanium_import_error_collection import TitaniumImportErrorCollection
from titanium_airflow_client.models.titanium_job import TitaniumJob
from titanium_airflow_client.models.titanium_list_dag_runs_form import TitaniumListDagRunsForm
from titanium_airflow_client.models.titanium_list_task_instance_form import TitaniumListTaskInstanceForm
from titanium_airflow_client.models.titanium_metadatabase_status import TitaniumMetadatabaseStatus
from titanium_airflow_client.models.titanium_plugin_collection import TitaniumPluginCollection
from titanium_airflow_client.models.titanium_plugin_collection_item import TitaniumPluginCollectionItem
from titanium_airflow_client.models.titanium_pool import TitaniumPool
from titanium_airflow_client.models.titanium_pool_collection import TitaniumPoolCollection
from titanium_airflow_client.models.titanium_provider import TitaniumProvider
from titanium_airflow_client.models.titanium_provider_collection import TitaniumProviderCollection
from titanium_airflow_client.models.titanium_queued_event import TitaniumQueuedEvent
from titanium_airflow_client.models.titanium_queued_event_collection import TitaniumQueuedEventCollection
from titanium_airflow_client.models.titanium_relative_delta import TitaniumRelativeDelta
from titanium_airflow_client.models.titanium_resource import TitaniumResource
from titanium_airflow_client.models.titanium_role import TitaniumRole
from titanium_airflow_client.models.titanium_role_collection import TitaniumRoleCollection
from titanium_airflow_client.models.titanium_sla_miss import TitaniumSLAMiss
from titanium_airflow_client.models.titanium_schedule_interval import TitaniumScheduleInterval
from titanium_airflow_client.models.titanium_scheduler_status import TitaniumSchedulerStatus
from titanium_airflow_client.models.titanium_set_dag_run_note import TitaniumSetDagRunNote
from titanium_airflow_client.models.titanium_set_task_instance_note import TitaniumSetTaskInstanceNote
from titanium_airflow_client.models.titanium_tag import TitaniumTag
from titanium_airflow_client.models.titanium_task import TitaniumTask
from titanium_airflow_client.models.titanium_task_collection import TitaniumTaskCollection
from titanium_airflow_client.models.titanium_task_extra_links_inner import TitaniumTaskExtraLinksInner
from titanium_airflow_client.models.titanium_task_instance import TitaniumTaskInstance
from titanium_airflow_client.models.titanium_task_instance_collection import TitaniumTaskInstanceCollection
from titanium_airflow_client.models.titanium_task_instance_reference import TitaniumTaskInstanceReference
from titanium_airflow_client.models.titanium_task_instance_reference_collection import TitaniumTaskInstanceReferenceCollection
from titanium_airflow_client.models.titanium_task_outlet_dataset_reference import TitaniumTaskOutletDatasetReference
from titanium_airflow_client.models.titanium_task_state import TitaniumTaskState
from titanium_airflow_client.models.titanium_time_delta import TitaniumTimeDelta
from titanium_airflow_client.models.titanium_trigger import TitaniumTrigger
from titanium_airflow_client.models.titanium_trigger_rule import TitaniumTriggerRule
from titanium_airflow_client.models.titanium_triggerer_status import TitaniumTriggererStatus
from titanium_airflow_client.models.titanium_update_dag_run_state import TitaniumUpdateDagRunState
from titanium_airflow_client.models.titanium_update_task_instance import TitaniumUpdateTaskInstance
from titanium_airflow_client.models.titanium_update_task_instances_state import TitaniumUpdateTaskInstancesState
from titanium_airflow_client.models.titanium_update_task_state import TitaniumUpdateTaskState
from titanium_airflow_client.models.titanium_user import TitaniumUser
from titanium_airflow_client.models.titanium_user_collection import TitaniumUserCollection
from titanium_airflow_client.models.titanium_user_collection_item import TitaniumUserCollectionItem
from titanium_airflow_client.models.titanium_user_collection_item_roles_inner import TitaniumUserCollectionItemRolesInner
from titanium_airflow_client.models.titanium_variable import TitaniumVariable
from titanium_airflow_client.models.titanium_variable_collection import TitaniumVariableCollection
from titanium_airflow_client.models.titanium_variable_collection_item import TitaniumVariableCollectionItem
from titanium_airflow_client.models.titanium_version_info import TitaniumVersionInfo
from titanium_airflow_client.models.titanium_weight_rule import TitaniumWeightRule
from titanium_airflow_client.models.titanium_x_com import TitaniumXCom
from titanium_airflow_client.models.titanium_x_com_collection import TitaniumXComCollection
from titanium_airflow_client.models.titanium_x_com_collection_item import TitaniumXComCollectionItem
