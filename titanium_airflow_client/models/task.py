# coding: utf-8

"""
    Airflow API (Stable)

    # Overview  To facilitate management, Apache Airflow supports a range of REST API endpoints across its objects. This section provides an overview of the API design, methods, and supported use cases.  Most of the endpoints accept `JSON` as input and return `JSON` responses. This means that you must usually add the following headers to your request: ``` Content-type: application/json Accept: application/json ```  ## Resources  The term `resource` refers to a single type of object in the Airflow metadata. An API is broken up by its endpoint's corresponding resource. The name of a resource is typically plural and expressed in camelCase. Example: `dagRuns`.  Resource names are used as part of endpoint URLs, as well as in API parameters and responses.  ## CRUD Operations  The platform supports **C**reate, **R**ead, **U**pdate, and **D**elete operations on most resources. You can review the standards for these operations and their standard parameters below.  Some endpoints have special behavior as exceptions.  ### Create  To create a resource, you typically submit an HTTP `POST` request with the resource's required metadata in the request body. The response returns a `201 Created` response code upon success with the resource's metadata, including its internal `id`, in the response body.  ### Read  The HTTP `GET` request can be used to read a resource or to list a number of resources.  A resource's `id` can be submitted in the request parameters to read a specific resource. The response usually returns a `200 OK` response code upon success, with the resource's metadata in the response body.  If a `GET` request does not include a specific resource `id`, it is treated as a list request. The response usually returns a `200 OK` response code upon success, with an object containing a list of resources' metadata in the response body.  When reading resources, some common query parameters are usually available. e.g.: ``` v1/connections?limit=25&offset=25 ```  |Query Parameter|Type|Description| |---------------|----|-----------| |limit|integer|Maximum number of objects to fetch. Usually 25 by default| |offset|integer|Offset after which to start returning objects. For use with limit query parameter.|  ### Update  Updating a resource requires the resource `id`, and is typically done using an HTTP `PATCH` request, with the fields to modify in the request body. The response usually returns a `200 OK` response code upon success, with information about the modified resource in the response body.  ### Delete  Deleting a resource requires the resource `id` and is typically executed via an HTTP `DELETE` request. The response usually returns a `204 No Content` response code upon success.  ## Conventions  - Resource names are plural and expressed in camelCase. - Names are consistent between URL parameter name and field name.  - Field names are in snake_case. ```json {     \"description\": \"string\",     \"name\": \"string\",     \"occupied_slots\": 0,     \"open_slots\": 0     \"queued_slots\": 0,     \"running_slots\": 0,     \"scheduled_slots\": 0,     \"slots\": 0, } ```  ### Update Mask  Update mask is available as a query parameter in patch endpoints. It is used to notify the API which fields you want to update. Using `update_mask` makes it easier to update objects by helping the server know which fields to update in an object instead of updating all fields. The update request ignores any fields that aren't specified in the field mask, leaving them with their current values.  Example: ```   resource = request.get('/resource/my-id').json()   resource['my_field'] = 'new-value'   request.patch('/resource/my-id?update_mask=my_field', data=json.dumps(resource)) ```  ## Versioning and Endpoint Lifecycle  - API versioning is not synchronized to specific releases of the Apache Airflow. - APIs are designed to be backward compatible. - Any changes to the API will first go through a deprecation phase.  # Trying the API  You can use a third party client, such as [curl](https://curl.haxx.se/), [HTTPie](https://httpie.org/), [Postman](https://www.postman.com/) or [the Insomnia rest client](https://insomnia.rest/) to test the Apache Airflow API.  Note that you will need to pass credentials data.  For e.g., here is how to pause a DAG with [curl](https://curl.haxx.se/), when basic authorization is used: ```bash curl -X PATCH 'https://example.com/api/v1/dags/{dag_id}?update_mask=is_paused' \\ -H 'Content-Type: application/json' \\ --user \"username:password\" \\ -d '{     \"is_paused\": true }' ```  Using a graphical tool such as [Postman](https://www.postman.com/) or [Insomnia](https://insomnia.rest/), it is possible to import the API specifications directly:  1. Download the API specification by clicking the **Download** button at the top of this document 2. Import the JSON specification in the graphical tool of your choice.   - In *Postman*, you can click the **import** button at the top   - With *Insomnia*, you can just drag-and-drop the file on the UI  Note that with *Postman*, you can also generate code snippets by selecting a request and clicking on the **Code** button.  ## Enabling CORS  [Cross-origin resource sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) is a browser security feature that restricts HTTP requests that are initiated from scripts running in the browser.  For details on enabling/configuring CORS, see [Enabling CORS](https://airflow.apache.org/docs/apache-airflow/stable/security/api.html).  # Authentication  To be able to meet the requirements of many organizations, Airflow supports many authentication methods, and it is even possible to add your own method.  If you want to check which auth backend is currently set, you can use `airflow config get-value api auth_backends` command as in the example below. ```bash $ airflow config get-value api auth_backends airflow.api.auth.backend.basic_auth ``` The default is to deny all requests.  For details on configuring the authentication, see [API Authorization](https://airflow.apache.org/docs/apache-airflow/stable/security/api.html).  # Errors  We follow the error response format proposed in [RFC 7807](https://tools.ietf.org/html/rfc7807) also known as Problem Details for HTTP APIs. As with our normal API responses, your client must be prepared to gracefully handle additional members of the response.  ## Unauthenticated  This indicates that the request has not been applied because it lacks valid authentication credentials for the target resource. Please check that you have valid credentials.  ## PermissionDenied  This response means that the server understood the request but refuses to authorize it because it lacks sufficient rights to the resource. It happens when you do not have the necessary permission to execute the action you performed. You need to get the appropriate permissions in other to resolve this error.  ## BadRequest  This response means that the server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). To resolve this, please ensure that your syntax is correct.  ## NotFound  This client error response indicates that the server cannot find the requested resource.  ## MethodNotAllowed  Indicates that the request method is known by the server but is not supported by the target resource.  ## NotAcceptable  The target resource does not have a current representation that would be acceptable to the user agent, according to the proactive negotiation header fields received in the request, and the server is unwilling to supply a default representation.  ## AlreadyExists  The request could not be completed due to a conflict with the current state of the target resource, e.g. the resource it tries to create already exists.  ## Unknown  This means that the server encountered an unexpected condition that prevented it from fulfilling the request. 

    The version of the OpenAPI document: 2.9.2
    Contact: dev@airflow.apache.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from titanium_airflow_client.models.class_reference import ClassReference
from titanium_airflow_client.models.dag import DAG
from titanium_airflow_client.models.task_extra_links_inner import TaskExtraLinksInner
from titanium_airflow_client.models.time_delta import TimeDelta
from titanium_airflow_client.models.trigger_rule import TriggerRule
from titanium_airflow_client.models.weight_rule import WeightRule
from typing import Optional, Set
from typing_extensions import Self

class Task(BaseModel):
    """
    For details see: [airflow.models.baseoperator.BaseOperator](https://airflow.apache.org/docs/apache-airflow/stable/_api/airflow/models/baseoperator/index.html#airflow.models.baseoperator.BaseOperator) 
    """ # noqa: E501
    class_ref: Optional[ClassReference] = None
    task_id: Optional[StrictStr] = None
    task_display_name: Optional[StrictStr] = None
    owner: Optional[StrictStr] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    trigger_rule: Optional[TriggerRule] = None
    extra_links: Optional[List[TaskExtraLinksInner]] = None
    depends_on_past: Optional[StrictBool] = None
    is_mapped: Optional[StrictBool] = None
    wait_for_downstream: Optional[StrictBool] = None
    retries: Optional[Union[StrictFloat, StrictInt]] = None
    queue: Optional[StrictStr] = None
    pool: Optional[StrictStr] = None
    pool_slots: Optional[Union[StrictFloat, StrictInt]] = None
    execution_timeout: Optional[TimeDelta] = None
    retry_delay: Optional[TimeDelta] = None
    retry_exponential_backoff: Optional[StrictBool] = None
    priority_weight: Optional[Union[StrictFloat, StrictInt]] = None
    weight_rule: Optional[WeightRule] = None
    ui_color: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Color in hexadecimal notation.")
    ui_fgcolor: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Color in hexadecimal notation.")
    template_fields: Optional[List[StrictStr]] = None
    sub_dag: Optional[DAG] = None
    downstream_task_ids: Optional[List[StrictStr]] = None
    __properties: ClassVar[List[str]] = ["class_ref", "task_id", "task_display_name", "owner", "start_date", "end_date", "trigger_rule", "extra_links", "depends_on_past", "is_mapped", "wait_for_downstream", "retries", "queue", "pool", "pool_slots", "execution_timeout", "retry_delay", "retry_exponential_backoff", "priority_weight", "weight_rule", "ui_color", "ui_fgcolor", "template_fields", "sub_dag", "downstream_task_ids"]

    @field_validator('ui_color')
    def ui_color_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^#[a-fA-F0-9]{3,6}$", value):
            raise ValueError(r"must validate the regular expression /^#[a-fA-F0-9]{3,6}$/")
        return value

    @field_validator('ui_fgcolor')
    def ui_fgcolor_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^#[a-fA-F0-9]{3,6}$", value):
            raise ValueError(r"must validate the regular expression /^#[a-fA-F0-9]{3,6}$/")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Task from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "task_id",
            "task_display_name",
            "owner",
            "start_date",
            "end_date",
            "extra_links",
            "depends_on_past",
            "is_mapped",
            "wait_for_downstream",
            "retries",
            "queue",
            "pool",
            "pool_slots",
            "retry_exponential_backoff",
            "priority_weight",
            "template_fields",
            "downstream_task_ids",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of class_ref
        if self.class_ref:
            _dict['class_ref'] = self.class_ref.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in extra_links (list)
        _items = []
        if self.extra_links:
            for _item in self.extra_links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['extra_links'] = _items
        # override the default output from pydantic by calling `to_dict()` of execution_timeout
        if self.execution_timeout:
            _dict['execution_timeout'] = self.execution_timeout.to_dict()
        # override the default output from pydantic by calling `to_dict()` of retry_delay
        if self.retry_delay:
            _dict['retry_delay'] = self.retry_delay.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sub_dag
        if self.sub_dag:
            _dict['sub_dag'] = self.sub_dag.to_dict()
        # set to None if end_date (nullable) is None
        # and model_fields_set contains the field
        if self.end_date is None and "end_date" in self.model_fields_set:
            _dict['end_date'] = None

        # set to None if queue (nullable) is None
        # and model_fields_set contains the field
        if self.queue is None and "queue" in self.model_fields_set:
            _dict['queue'] = None

        # set to None if execution_timeout (nullable) is None
        # and model_fields_set contains the field
        if self.execution_timeout is None and "execution_timeout" in self.model_fields_set:
            _dict['execution_timeout'] = None

        # set to None if retry_delay (nullable) is None
        # and model_fields_set contains the field
        if self.retry_delay is None and "retry_delay" in self.model_fields_set:
            _dict['retry_delay'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Task from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "class_ref": ClassReference.from_dict(obj["class_ref"]) if obj.get("class_ref") is not None else None,
            "task_id": obj.get("task_id"),
            "task_display_name": obj.get("task_display_name"),
            "owner": obj.get("owner"),
            "start_date": obj.get("start_date"),
            "end_date": obj.get("end_date"),
            "trigger_rule": obj.get("trigger_rule"),
            "extra_links": [TaskExtraLinksInner.from_dict(_item) for _item in obj["extra_links"]] if obj.get("extra_links") is not None else None,
            "depends_on_past": obj.get("depends_on_past"),
            "is_mapped": obj.get("is_mapped"),
            "wait_for_downstream": obj.get("wait_for_downstream"),
            "retries": obj.get("retries"),
            "queue": obj.get("queue"),
            "pool": obj.get("pool"),
            "pool_slots": obj.get("pool_slots"),
            "execution_timeout": TimeDelta.from_dict(obj["execution_timeout"]) if obj.get("execution_timeout") is not None else None,
            "retry_delay": TimeDelta.from_dict(obj["retry_delay"]) if obj.get("retry_delay") is not None else None,
            "retry_exponential_backoff": obj.get("retry_exponential_backoff"),
            "priority_weight": obj.get("priority_weight"),
            "weight_rule": obj.get("weight_rule"),
            "ui_color": obj.get("ui_color"),
            "ui_fgcolor": obj.get("ui_fgcolor"),
            "template_fields": obj.get("template_fields"),
            "sub_dag": DAG.from_dict(obj["sub_dag"]) if obj.get("sub_dag") is not None else None,
            "downstream_task_ids": obj.get("downstream_task_ids")
        })
        return _obj


