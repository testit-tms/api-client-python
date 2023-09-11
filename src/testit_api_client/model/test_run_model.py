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
    from testit_api_client.model.auto_test_model import AutoTestModel
    from testit_api_client.model.test_plan_model import TestPlanModel
    from testit_api_client.model.test_result_model import TestResultModel
    from testit_api_client.model.test_run_analytic_result_model import TestRunAnalyticResultModel
    from testit_api_client.model.test_run_state import TestRunState
    globals()['AutoTestModel'] = AutoTestModel
    globals()['TestPlanModel'] = TestPlanModel
    globals()['TestResultModel'] = TestResultModel
    globals()['TestRunAnalyticResultModel'] = TestRunAnalyticResultModel
    globals()['TestRunState'] = TestRunState


class TestRunModel(ModelNormal):
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
        ('build',): {
            'max_length': 450,
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
            'auto_tests_count': (int,),  # noqa: E501
            'is_automated': (bool,),  # noqa: E501
            'created_date': (datetime,),  # noqa: E501
            'created_by_id': (str,),  # noqa: E501
            'state_name': (TestRunState,),  # noqa: E501
            'project_id': (str,),  # noqa: E501
            'id': (str,),  # noqa: E501
            'is_deleted': (bool,),  # noqa: E501
            'auto_tests': ([AutoTestModel], none_type,),  # noqa: E501
            'test_suite_ids': ([str], none_type,),  # noqa: E501
            'analytic': (TestRunAnalyticResultModel,),  # noqa: E501
            'test_results': ([TestResultModel], none_type,),  # noqa: E501
            'test_plan': (TestPlanModel,),  # noqa: E501
            'modified_date': (datetime, none_type,),  # noqa: E501
            'modified_by_id': (str, none_type,),  # noqa: E501
            'created_by_user_name': (str, none_type,),  # noqa: E501
            'started_date': (datetime, none_type,),  # noqa: E501
            'completed_date': (datetime, none_type,),  # noqa: E501
            'build': (str, none_type,),  # noqa: E501
            'description': (str, none_type,),  # noqa: E501
            'test_plan_id': (str, none_type,),  # noqa: E501
            'run_by_user_id': (str, none_type,),  # noqa: E501
            'stopped_by_user_id': (str, none_type,),  # noqa: E501
            'name': (str, none_type,),  # noqa: E501
            'launch_source': (str, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'auto_tests_count': 'autoTestsCount',  # noqa: E501
        'is_automated': 'isAutomated',  # noqa: E501
        'created_date': 'createdDate',  # noqa: E501
        'created_by_id': 'createdById',  # noqa: E501
        'state_name': 'stateName',  # noqa: E501
        'project_id': 'projectId',  # noqa: E501
        'id': 'id',  # noqa: E501
        'is_deleted': 'isDeleted',  # noqa: E501
        'auto_tests': 'autoTests',  # noqa: E501
        'test_suite_ids': 'testSuiteIds',  # noqa: E501
        'analytic': 'analytic',  # noqa: E501
        'test_results': 'testResults',  # noqa: E501
        'test_plan': 'testPlan',  # noqa: E501
        'modified_date': 'modifiedDate',  # noqa: E501
        'modified_by_id': 'modifiedById',  # noqa: E501
        'created_by_user_name': 'createdByUserName',  # noqa: E501
        'started_date': 'startedDate',  # noqa: E501
        'completed_date': 'completedDate',  # noqa: E501
        'build': 'build',  # noqa: E501
        'description': 'description',  # noqa: E501
        'test_plan_id': 'testPlanId',  # noqa: E501
        'run_by_user_id': 'runByUserId',  # noqa: E501
        'stopped_by_user_id': 'stoppedByUserId',  # noqa: E501
        'name': 'name',  # noqa: E501
        'launch_source': 'launchSource',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, auto_tests_count, is_automated, created_date, created_by_id, state_name, project_id, id, is_deleted, *args, **kwargs):  # noqa: E501
        """TestRunModel - a model defined in OpenAPI

        Args:
            auto_tests_count (int):
            is_automated (bool):
            created_date (datetime):
            created_by_id (str):
            state_name (TestRunState):
            project_id (str):
            id (str): Unique ID of the entity
            is_deleted (bool): Indicates if the entity is deleted

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
            auto_tests ([AutoTestModel], none_type): [optional]  # noqa: E501
            test_suite_ids ([str], none_type): [optional]  # noqa: E501
            analytic (TestRunAnalyticResultModel): [optional]  # noqa: E501
            test_results ([TestResultModel], none_type): [optional]  # noqa: E501
            test_plan (TestPlanModel): [optional]  # noqa: E501
            modified_date (datetime, none_type): [optional]  # noqa: E501
            modified_by_id (str, none_type): [optional]  # noqa: E501
            created_by_user_name (str, none_type): [optional]  # noqa: E501
            started_date (datetime, none_type): [optional]  # noqa: E501
            completed_date (datetime, none_type): [optional]  # noqa: E501
            build (str, none_type): [optional]  # noqa: E501
            description (str, none_type): [optional]  # noqa: E501
            test_plan_id (str, none_type): [optional]  # noqa: E501
            run_by_user_id (str, none_type): [optional]  # noqa: E501
            stopped_by_user_id (str, none_type): [optional]  # noqa: E501
            name (str, none_type): [optional]  # noqa: E501
            launch_source (str, none_type): [optional]  # noqa: E501
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

        self.auto_tests_count = auto_tests_count
        self.is_automated = is_automated
        self.created_date = created_date
        self.created_by_id = created_by_id
        self.state_name = state_name
        self.project_id = project_id
        self.id = id
        self.is_deleted = is_deleted
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
    def __init__(self, auto_tests_count, is_automated, created_date, created_by_id, state_name, project_id, id, is_deleted, *args, **kwargs):  # noqa: E501
        """TestRunModel - a model defined in OpenAPI

        Args:
            auto_tests_count (int):
            is_automated (bool):
            created_date (datetime):
            created_by_id (str):
            state_name (TestRunState):
            project_id (str):
            id (str): Unique ID of the entity
            is_deleted (bool): Indicates if the entity is deleted

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
            auto_tests ([AutoTestModel], none_type): [optional]  # noqa: E501
            test_suite_ids ([str], none_type): [optional]  # noqa: E501
            analytic (TestRunAnalyticResultModel): [optional]  # noqa: E501
            test_results ([TestResultModel], none_type): [optional]  # noqa: E501
            test_plan (TestPlanModel): [optional]  # noqa: E501
            modified_date (datetime, none_type): [optional]  # noqa: E501
            modified_by_id (str, none_type): [optional]  # noqa: E501
            created_by_user_name (str, none_type): [optional]  # noqa: E501
            started_date (datetime, none_type): [optional]  # noqa: E501
            completed_date (datetime, none_type): [optional]  # noqa: E501
            build (str, none_type): [optional]  # noqa: E501
            description (str, none_type): [optional]  # noqa: E501
            test_plan_id (str, none_type): [optional]  # noqa: E501
            run_by_user_id (str, none_type): [optional]  # noqa: E501
            stopped_by_user_id (str, none_type): [optional]  # noqa: E501
            name (str, none_type): [optional]  # noqa: E501
            launch_source (str, none_type): [optional]  # noqa: E501
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

        self.auto_tests_count = auto_tests_count
        self.is_automated = is_automated
        self.created_date = created_date
        self.created_by_id = created_by_id
        self.state_name = state_name
        self.project_id = project_id
        self.id = id
        self.is_deleted = is_deleted
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
