# coding: utf-8

"""
    API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Dict, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, constr
from testit_api_client.models.request_type_model import RequestTypeModel
from testit_api_client.models.web_hook_event_type_model import WebHookEventTypeModel

class WebHookPostModel(BaseModel):
    """
    WebHookPostModel
    """
    project_id: StrictStr = Field(default=..., alias="projectId", description="Unique ID of the webhook project")
    event_type: WebHookEventTypeModel = Field(default=..., alias="eventType", description="Type of event which triggers the webhook")
    description: Optional[StrictStr] = Field(default=None, description="Description of the webhook")
    url: constr(strict=True, min_length=1) = Field(default=..., description="Request URL of the webhook")
    request_type: RequestTypeModel = Field(default=..., alias="requestType", description="Request method of the webhook")
    should_send_body: StrictBool = Field(default=..., alias="shouldSendBody", description="Indicates if the webhook sends body")
    headers: Dict[str, StrictStr] = Field(default=..., description="Collection of the webhook headers")
    query_parameters: Dict[str, StrictStr] = Field(default=..., alias="queryParameters", description="Collection of the webhook query parameters")
    is_enabled: StrictBool = Field(default=..., alias="isEnabled", description="Indicates if the webhook is active")
    should_send_custom_body: StrictBool = Field(default=..., alias="shouldSendCustomBody", description="Indicates if the webhook sends custom body")
    custom_body: Optional[StrictStr] = Field(default=None, alias="customBody", description="Custom body of the webhook")
    should_replace_parameters: StrictBool = Field(default=..., alias="shouldReplaceParameters", description="Indicates if the webhook injects parameters")
    should_escape_parameters: StrictBool = Field(default=..., alias="shouldEscapeParameters", description="Indicates if the webhook escapes invalid characters in parameters")
    name: constr(strict=True, max_length=255, min_length=0) = Field(default=..., description="Name of the webhook")
    __properties = ["projectId", "eventType", "description", "url", "requestType", "shouldSendBody", "headers", "queryParameters", "isEnabled", "shouldSendCustomBody", "customBody", "shouldReplaceParameters", "shouldEscapeParameters", "name"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> WebHookPostModel:
        """Create an instance of WebHookPostModel from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if custom_body (nullable) is None
        # and __fields_set__ contains the field
        if self.custom_body is None and "custom_body" in self.__fields_set__:
            _dict['customBody'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> WebHookPostModel:
        """Create an instance of WebHookPostModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return WebHookPostModel.parse_obj(obj)

        _obj = WebHookPostModel.parse_obj({
            "project_id": obj.get("projectId"),
            "event_type": obj.get("eventType"),
            "description": obj.get("description"),
            "url": obj.get("url"),
            "request_type": obj.get("requestType"),
            "should_send_body": obj.get("shouldSendBody"),
            "headers": obj.get("headers"),
            "query_parameters": obj.get("queryParameters"),
            "is_enabled": obj.get("isEnabled"),
            "should_send_custom_body": obj.get("shouldSendCustomBody"),
            "custom_body": obj.get("customBody"),
            "should_replace_parameters": obj.get("shouldReplaceParameters"),
            "should_escape_parameters": obj.get("shouldEscapeParameters"),
            "name": obj.get("name")
        })
        return _obj


