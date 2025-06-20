# TestPlanLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bug_link** | [**LinkModel**](LinkModel.md) |  | [optional] 
**work_item_global_id** | **int** |  | [optional] 
**work_item_name** | **str** |  | [optional] 
**configuration_name** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**comment** | **str** |  | [optional] 
**info** | [**ExternalLinkModel**](ExternalLinkModel.md) |  | [optional] 

## Example

```python
from testit_api_client.models.test_plan_link import TestPlanLink

# TODO update the JSON string below
json = "{}"
# create an instance of TestPlanLink from a JSON string
test_plan_link_instance = TestPlanLink.from_json(json)
# print the JSON string representation of the object
print(TestPlanLink.to_json())

# convert the object into a dict
test_plan_link_dict = test_plan_link_instance.to_dict()
# create an instance of TestPlanLink from a dict
test_plan_link_from_dict = TestPlanLink.from_dict(test_plan_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


