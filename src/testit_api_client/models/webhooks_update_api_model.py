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



from pydantic import BaseModel, Field
from testit_api_client.models.webhook_bulk_update_api_model import WebhookBulkUpdateApiModel
from testit_api_client.models.webhooks_extraction_api_model import WebhooksExtractionApiModel
from testit_api_client.models.webhooks_filter_api_model import WebhooksFilterApiModel

class WebhooksUpdateApiModel(BaseModel):
    """
    WebhooksUpdateApiModel
    """
    filter: WebhooksFilterApiModel = Field(...)
    model: WebhookBulkUpdateApiModel = Field(...)
    extractor: WebhooksExtractionApiModel = Field(...)
    __properties = ["filter", "model", "extractor"]

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
    def from_json(cls, json_str: str) -> WebhooksUpdateApiModel:
        """Create an instance of WebhooksUpdateApiModel from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of filter
        if self.filter:
            _dict['filter'] = self.filter.to_dict()
        # override the default output from pydantic by calling `to_dict()` of model
        if self.model:
            _dict['model'] = self.model.to_dict()
        # override the default output from pydantic by calling `to_dict()` of extractor
        if self.extractor:
            _dict['extractor'] = self.extractor.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> WebhooksUpdateApiModel:
        """Create an instance of WebhooksUpdateApiModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return WebhooksUpdateApiModel.parse_obj(obj)

        _obj = WebhooksUpdateApiModel.parse_obj({
            "filter": WebhooksFilterApiModel.from_dict(obj.get("filter")) if obj.get("filter") is not None else None,
            "model": WebhookBulkUpdateApiModel.from_dict(obj.get("model")) if obj.get("model") is not None else None,
            "extractor": WebhooksExtractionApiModel.from_dict(obj.get("extractor")) if obj.get("extractor") is not None else None
        })
        return _obj


