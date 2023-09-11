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
    from testit_api_client.model.test_point_filter_model_work_item_created_date import TestPointFilterModelWorkItemCreatedDate
    from testit_api_client.model.test_point_filter_model_work_item_modified_date import TestPointFilterModelWorkItemModifiedDate
    from testit_api_client.model.test_suite_work_items_search_model_duration import TestSuiteWorkItemsSearchModelDuration
    from testit_api_client.model.test_suite_work_items_search_model_median_duration import TestSuiteWorkItemsSearchModelMedianDuration
    from testit_api_client.model.work_item_entity_types import WorkItemEntityTypes
    from testit_api_client.model.work_item_priority_model import WorkItemPriorityModel
    from testit_api_client.model.work_item_states import WorkItemStates
    globals()['TestPointFilterModelWorkItemCreatedDate'] = TestPointFilterModelWorkItemCreatedDate
    globals()['TestPointFilterModelWorkItemModifiedDate'] = TestPointFilterModelWorkItemModifiedDate
    globals()['TestSuiteWorkItemsSearchModelDuration'] = TestSuiteWorkItemsSearchModelDuration
    globals()['TestSuiteWorkItemsSearchModelMedianDuration'] = TestSuiteWorkItemsSearchModelMedianDuration
    globals()['WorkItemEntityTypes'] = WorkItemEntityTypes
    globals()['WorkItemPriorityModel'] = WorkItemPriorityModel
    globals()['WorkItemStates'] = WorkItemStates


class TestSuiteWorkItemsSearchModel(ModelNormal):
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
        ('tag_names',): {
        },
        ('entity_types',): {
        },
        ('include_ids',): {
        },
        ('exclude_ids',): {
        },
        ('name',): {
            'max_length': 255,
            'min_length': 0,
        },
        ('ids',): {
        },
        ('global_ids',): {
        },
        ('project_ids',): {
        },
        ('section_ids',): {
        },
        ('created_by_ids',): {
        },
        ('modified_by_ids',): {
        },
        ('states',): {
        },
        ('priorities',): {
        },
        ('types',): {
        },
        ('tags',): {
        },
        ('auto_test_ids',): {
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
            'tag_names': ([str], none_type,),  # noqa: E501
            'entity_types': ([WorkItemEntityTypes], none_type,),  # noqa: E501
            'name_or_id': (str, none_type,),  # noqa: E501
            'include_ids': ([str], none_type,),  # noqa: E501
            'exclude_ids': ([str], none_type,),  # noqa: E501
            'name': (str, none_type,),  # noqa: E501
            'ids': ([str], none_type,),  # noqa: E501
            'global_ids': ([int], none_type,),  # noqa: E501
            'attributes': ({str: ([str], none_type)}, none_type,),  # noqa: E501
            'is_deleted': (bool, none_type,),  # noqa: E501
            'project_ids': ([str], none_type,),  # noqa: E501
            'section_ids': ([str], none_type,),  # noqa: E501
            'created_by_ids': ([str], none_type,),  # noqa: E501
            'modified_by_ids': ([str], none_type,),  # noqa: E501
            'states': ([WorkItemStates], none_type,),  # noqa: E501
            'priorities': ([WorkItemPriorityModel], none_type,),  # noqa: E501
            'types': ([WorkItemEntityTypes], none_type,),  # noqa: E501
            'created_date': (TestPointFilterModelWorkItemCreatedDate,),  # noqa: E501
            'modified_date': (TestPointFilterModelWorkItemModifiedDate,),  # noqa: E501
            'duration': (TestSuiteWorkItemsSearchModelDuration,),  # noqa: E501
            'median_duration': (TestSuiteWorkItemsSearchModelMedianDuration,),  # noqa: E501
            'is_automated': (bool, none_type,),  # noqa: E501
            'tags': ([str], none_type,),  # noqa: E501
            'auto_test_ids': ([str], none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'tag_names': 'tagNames',  # noqa: E501
        'entity_types': 'entityTypes',  # noqa: E501
        'name_or_id': 'nameOrId',  # noqa: E501
        'include_ids': 'includeIds',  # noqa: E501
        'exclude_ids': 'excludeIds',  # noqa: E501
        'name': 'name',  # noqa: E501
        'ids': 'ids',  # noqa: E501
        'global_ids': 'globalIds',  # noqa: E501
        'attributes': 'attributes',  # noqa: E501
        'is_deleted': 'isDeleted',  # noqa: E501
        'project_ids': 'projectIds',  # noqa: E501
        'section_ids': 'sectionIds',  # noqa: E501
        'created_by_ids': 'createdByIds',  # noqa: E501
        'modified_by_ids': 'modifiedByIds',  # noqa: E501
        'states': 'states',  # noqa: E501
        'priorities': 'priorities',  # noqa: E501
        'types': 'types',  # noqa: E501
        'created_date': 'createdDate',  # noqa: E501
        'modified_date': 'modifiedDate',  # noqa: E501
        'duration': 'duration',  # noqa: E501
        'median_duration': 'medianDuration',  # noqa: E501
        'is_automated': 'isAutomated',  # noqa: E501
        'tags': 'tags',  # noqa: E501
        'auto_test_ids': 'autoTestIds',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """TestSuiteWorkItemsSearchModel - a model defined in OpenAPI

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
            tag_names ([str], none_type): Collection of tags. [optional]  # noqa: E501
            entity_types ([WorkItemEntityTypes], none_type): Collection of types of work item  <br>Allowed values: `TestCases`, `CheckLists`, `SharedSteps`. [optional]  # noqa: E501
            name_or_id (str, none_type): Name or identifier (UUID) of work item. [optional]  # noqa: E501
            include_ids ([str], none_type): Collection of identifiers of work items which need to be included in result regardless of filtering. [optional]  # noqa: E501
            exclude_ids ([str], none_type): Collection of identifiers of work items which need to be excluded from result regardless of filtering. [optional]  # noqa: E501
            name (str, none_type): Name of work item. [optional]  # noqa: E501
            ids ([str], none_type): Specifies a work item unique IDs to search for. [optional]  # noqa: E501
            global_ids ([int], none_type): Collection of global (integer) identifiers. [optional]  # noqa: E501
            attributes ({str: ([str], none_type)}, none_type): Custom attributes of work item. [optional]  # noqa: E501
            is_deleted (bool, none_type): Is result must consist of only actual/deleted work items. [optional]  # noqa: E501
            project_ids ([str], none_type): Collection of project identifiers. [optional]  # noqa: E501
            section_ids ([str], none_type): Collection of section identifiers. [optional]  # noqa: E501
            created_by_ids ([str], none_type): Collection of identifiers of users who created work item. [optional]  # noqa: E501
            modified_by_ids ([str], none_type): Collection of identifiers of users who applied last modification to work item. [optional]  # noqa: E501
            states ([WorkItemStates], none_type): Collection of states of work item. [optional]  # noqa: E501
            priorities ([WorkItemPriorityModel], none_type): Collection of priorities of work item. [optional]  # noqa: E501
            types ([WorkItemEntityTypes], none_type): Collection of types of work item. [optional]  # noqa: E501
            created_date (TestPointFilterModelWorkItemCreatedDate): [optional]  # noqa: E501
            modified_date (TestPointFilterModelWorkItemModifiedDate): [optional]  # noqa: E501
            duration (TestSuiteWorkItemsSearchModelDuration): [optional]  # noqa: E501
            median_duration (TestSuiteWorkItemsSearchModelMedianDuration): [optional]  # noqa: E501
            is_automated (bool, none_type): Is result must consist of only manual/automated work items. [optional]  # noqa: E501
            tags ([str], none_type): Collection of tags. [optional]  # noqa: E501
            auto_test_ids ([str], none_type): Collection of identifiers of linked autotests. [optional]  # noqa: E501
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
    def __init__(self, *args, **kwargs):  # noqa: E501
        """TestSuiteWorkItemsSearchModel - a model defined in OpenAPI

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
            tag_names ([str], none_type): Collection of tags. [optional]  # noqa: E501
            entity_types ([WorkItemEntityTypes], none_type): Collection of types of work item  <br>Allowed values: `TestCases`, `CheckLists`, `SharedSteps`. [optional]  # noqa: E501
            name_or_id (str, none_type): Name or identifier (UUID) of work item. [optional]  # noqa: E501
            include_ids ([str], none_type): Collection of identifiers of work items which need to be included in result regardless of filtering. [optional]  # noqa: E501
            exclude_ids ([str], none_type): Collection of identifiers of work items which need to be excluded from result regardless of filtering. [optional]  # noqa: E501
            name (str, none_type): Name of work item. [optional]  # noqa: E501
            ids ([str], none_type): Specifies a work item unique IDs to search for. [optional]  # noqa: E501
            global_ids ([int], none_type): Collection of global (integer) identifiers. [optional]  # noqa: E501
            attributes ({str: ([str], none_type)}, none_type): Custom attributes of work item. [optional]  # noqa: E501
            is_deleted (bool, none_type): Is result must consist of only actual/deleted work items. [optional]  # noqa: E501
            project_ids ([str], none_type): Collection of project identifiers. [optional]  # noqa: E501
            section_ids ([str], none_type): Collection of section identifiers. [optional]  # noqa: E501
            created_by_ids ([str], none_type): Collection of identifiers of users who created work item. [optional]  # noqa: E501
            modified_by_ids ([str], none_type): Collection of identifiers of users who applied last modification to work item. [optional]  # noqa: E501
            states ([WorkItemStates], none_type): Collection of states of work item. [optional]  # noqa: E501
            priorities ([WorkItemPriorityModel], none_type): Collection of priorities of work item. [optional]  # noqa: E501
            types ([WorkItemEntityTypes], none_type): Collection of types of work item. [optional]  # noqa: E501
            created_date (TestPointFilterModelWorkItemCreatedDate): [optional]  # noqa: E501
            modified_date (TestPointFilterModelWorkItemModifiedDate): [optional]  # noqa: E501
            duration (TestSuiteWorkItemsSearchModelDuration): [optional]  # noqa: E501
            median_duration (TestSuiteWorkItemsSearchModelMedianDuration): [optional]  # noqa: E501
            is_automated (bool, none_type): Is result must consist of only manual/automated work items. [optional]  # noqa: E501
            tags ([str], none_type): Collection of tags. [optional]  # noqa: E501
            auto_test_ids ([str], none_type): Collection of identifiers of linked autotests. [optional]  # noqa: E501
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
