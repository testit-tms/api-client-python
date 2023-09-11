"""
    API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v2.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from testit_api_client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from testit_api_client.exceptions import ApiAttributeError


def lazy_import():
    from testit_api_client.model.request_type_model import RequestTypeModel
    from testit_api_client.model.web_hook_event_type_model import WebHookEventTypeModel
    globals()['RequestTypeModel'] = RequestTypeModel
    globals()['WebHookEventTypeModel'] = WebHookEventTypeModel


class WebHookPostModel(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
        ('url',): {
            'min_length': 1,
        },
        ('name',): {
            'max_length': 255,
            'min_length': 0,
        },
    }

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'project_id': (str,),  # noqa: E501
            'event_type': (WebHookEventTypeModel,),  # noqa: E501
            'url': (str,),  # noqa: E501
            'request_type': (RequestTypeModel,),  # noqa: E501
            'should_send_body': (bool,),  # noqa: E501
            'is_enabled': (bool,),  # noqa: E501
            'should_send_custom_body': (bool,),  # noqa: E501
            'should_replace_parameters': (bool,),  # noqa: E501
            'should_escape_parameters': (bool,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'description': (str, none_type,),  # noqa: E501
            'headers': ({str: (str, none_type)}, none_type,),  # noqa: E501
            'query_parameters': ({str: (str, none_type)}, none_type,),  # noqa: E501
            'custom_body': (str, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'project_id': 'projectId',  # noqa: E501
        'event_type': 'eventType',  # noqa: E501
        'url': 'url',  # noqa: E501
        'request_type': 'requestType',  # noqa: E501
        'should_send_body': 'shouldSendBody',  # noqa: E501
        'is_enabled': 'isEnabled',  # noqa: E501
        'should_send_custom_body': 'shouldSendCustomBody',  # noqa: E501
        'should_replace_parameters': 'shouldReplaceParameters',  # noqa: E501
        'should_escape_parameters': 'shouldEscapeParameters',  # noqa: E501
        'name': 'name',  # noqa: E501
        'description': 'description',  # noqa: E501
        'headers': 'headers',  # noqa: E501
        'query_parameters': 'queryParameters',  # noqa: E501
        'custom_body': 'customBody',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, project_id, event_type, url, request_type, should_send_body, is_enabled, should_send_custom_body, should_replace_parameters, should_escape_parameters, name, *args, **kwargs):  # noqa: E501
        """WebHookPostModel - a model defined in OpenAPI

        Args:
            project_id (str): Unique ID of the webhook project
            event_type (WebHookEventTypeModel):
            url (str): Request URL of the webhook
            request_type (RequestTypeModel):
            should_send_body (bool): Indicates if the webhook sends body
            is_enabled (bool): Indicates if the webhook is active
            should_send_custom_body (bool): Indicates if the webhook sends custom body
            should_replace_parameters (bool): Indicates if the webhook injects parameters
            should_escape_parameters (bool): Indicates if the webhook escapes invalid characters in parameters
            name (str): Name of the webhook

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            description (str, none_type): Description of the webhook. [optional]  # noqa: E501
            headers ({str: (str, none_type)}, none_type): Collection of the webhook headers. [optional]  # noqa: E501
            query_parameters ({str: (str, none_type)}, none_type): Collection of the webhook query parameters. [optional]  # noqa: E501
            custom_body (str, none_type): Custom body of the webhook. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', True)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.project_id = project_id
        self.event_type = event_type
        self.url = url
        self.request_type = request_type
        self.should_send_body = should_send_body
        self.is_enabled = is_enabled
        self.should_send_custom_body = should_send_custom_body
        self.should_replace_parameters = should_replace_parameters
        self.should_escape_parameters = should_escape_parameters
        self.name = name
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, project_id, event_type, url, request_type, should_send_body, is_enabled, should_send_custom_body, should_replace_parameters, should_escape_parameters, name, *args, **kwargs):  # noqa: E501
        """WebHookPostModel - a model defined in OpenAPI

        Args:
            project_id (str): Unique ID of the webhook project
            event_type (WebHookEventTypeModel):
            url (str): Request URL of the webhook
            request_type (RequestTypeModel):
            should_send_body (bool): Indicates if the webhook sends body
            is_enabled (bool): Indicates if the webhook is active
            should_send_custom_body (bool): Indicates if the webhook sends custom body
            should_replace_parameters (bool): Indicates if the webhook injects parameters
            should_escape_parameters (bool): Indicates if the webhook escapes invalid characters in parameters
            name (str): Name of the webhook

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            description (str, none_type): Description of the webhook. [optional]  # noqa: E501
            headers ({str: (str, none_type)}, none_type): Collection of the webhook headers. [optional]  # noqa: E501
            query_parameters ({str: (str, none_type)}, none_type): Collection of the webhook query parameters. [optional]  # noqa: E501
            custom_body (str, none_type): Custom body of the webhook. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.project_id = project_id
        self.event_type = event_type
        self.url = url
        self.request_type = request_type
        self.should_send_body = should_send_body
        self.is_enabled = is_enabled
        self.should_send_custom_body = should_send_custom_body
        self.should_replace_parameters = should_replace_parameters
        self.should_escape_parameters = should_escape_parameters
        self.name = name
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
