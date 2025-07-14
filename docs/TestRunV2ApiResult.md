# TestRunV2ApiResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Test run unique identifier | 
**name** | **str** | Test run name | 
**description** | **str** | Test run description | [optional] 
**launch_source** | **str** | Test run launch source                Once launch source is specified it cannot be updated. | [optional] 
**started_on** | **datetime** | Date and time of test run start | [optional] 
**completed_on** | **datetime** | Date and time of test run end | [optional] 
**state_name** | [**TestRunState**](TestRunState.md) | Test run state | 
**status** | [**TestStatusApiResult**](TestStatusApiResult.md) | Test run status | 
**project_id** | **str** | Project unique identifier                This property is used to link test run with project. | 
**test_plan_id** | **str** | Test plan unique identifier                This property is used to link test run with test plan. | [optional] 
**test_results** | [**List[TestResultV2GetModel]**](TestResultV2GetModel.md) | Enumeration of test results related to test run | [optional] 
**created_date** | **datetime** | Date and time of test run creation | 
**modified_date** | **datetime** | Date and time of last test run  modification | [optional] 
**created_by_id** | **str** | Unique identifier of user who created test run | 
**modified_by_id** | **str** | Unique identifier of user who applied last test run  modification | [optional] 
**created_by_user_name** | **str** | Username of user who created test run | [optional] 
**attachments** | [**List[AttachmentApiResult]**](AttachmentApiResult.md) | Collection of attachments related to the test run | 
**links** | [**List[LinkApiResult]**](LinkApiResult.md) | Collection of links related to the test run | 
**custom_parameters** | **Dict[str, str]** | Customers test run parameters | [optional] 
**webhooks** | [**List[NamedEntityApiModel]**](NamedEntityApiModel.md) | Enabled webhooks | 
**run_count** | **int** | Run count | 

## Example

```python
from testit_api_client.models.test_run_v2_api_result import TestRunV2ApiResult

# TODO update the JSON string below
json = "{}"
# create an instance of TestRunV2ApiResult from a JSON string
test_run_v2_api_result_instance = TestRunV2ApiResult.from_json(json)
# print the JSON string representation of the object
print TestRunV2ApiResult.to_json()

# convert the object into a dict
test_run_v2_api_result_dict = test_run_v2_api_result_instance.to_dict()
# create an instance of TestRunV2ApiResult from a dict
test_run_v2_api_result_from_dict = TestRunV2ApiResult.from_dict(test_run_v2_api_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


