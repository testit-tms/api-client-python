# TestSuiteWithChildrenModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**children** | [**List[TestSuiteWithChildrenModel]**](TestSuiteWithChildrenModel.md) |  | [optional] 
**tester_id** | **str** |  | [optional] 
**parent_id** | **str** |  | [optional] 
**test_plan_id** | **str** |  | 
**name** | **str** |  | 
**id** | **str** | Unique ID of the entity | 
**is_deleted** | **bool** | Indicates if the entity is deleted | 

## Example

```python
from testit_api_client.models.test_suite_with_children_model import TestSuiteWithChildrenModel

# TODO update the JSON string below
json = "{}"
# create an instance of TestSuiteWithChildrenModel from a JSON string
test_suite_with_children_model_instance = TestSuiteWithChildrenModel.from_json(json)
# print the JSON string representation of the object
print(TestSuiteWithChildrenModel.to_json())

# convert the object into a dict
test_suite_with_children_model_dict = test_suite_with_children_model_instance.to_dict()
# create an instance of TestSuiteWithChildrenModel from a dict
test_suite_with_children_model_from_dict = TestSuiteWithChildrenModel.from_dict(test_suite_with_children_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


