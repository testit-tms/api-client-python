# TestSuiteV2TreeModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**children** | [**List[TestSuiteV2TreeModel]**](TestSuiteV2TreeModel.md) | nested enumeration of children is allowed | [optional] 
**id** | **str** | Unique ID of the test suite | 
**refresh_date** | **datetime** | Date of the last refresh of the test suite | [optional] 
**parent_id** | **str** | Unique ID of the parent test suite in hierarchy | [optional] 
**test_plan_id** | **str** | Unique ID of test plan to which the test suite belongs | 
**name** | **str** | Name of the test suite | 
**type** | [**TestSuiteType**](TestSuiteType.md) | Type of the test suite | [optional] 
**save_structure** | **bool** | Indicates if the test suite retains section tree structure | [optional] 
**auto_refresh** | **bool** | Indicates if scheduled auto refresh is enabled for the test suite | [optional] 

## Example

```python
from testit_api_client.models.test_suite_v2_tree_model import TestSuiteV2TreeModel

# TODO update the JSON string below
json = "{}"
# create an instance of TestSuiteV2TreeModel from a JSON string
test_suite_v2_tree_model_instance = TestSuiteV2TreeModel.from_json(json)
# print the JSON string representation of the object
print TestSuiteV2TreeModel.to_json()

# convert the object into a dict
test_suite_v2_tree_model_dict = test_suite_v2_tree_model_instance.to_dict()
# create an instance of TestSuiteV2TreeModel from a dict
test_suite_v2_tree_model_from_dict = TestSuiteV2TreeModel.from_dict(test_suite_v2_tree_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


