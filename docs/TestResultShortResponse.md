# TestResultShortResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ID of the test result | 
**name** | **str** | Name of autotest represented by the test result | 
**autotest_global_id** | **int** | Global ID of autotest represented by the test result | 
**test_run_id** | **str** | Unique ID of test run where the test result is located | 
**configuration_id** | **str** | Unique ID of configuration which the test result uses | 
**configuration_name** | **str** | Name of configuration which the test result uses | 
**outcome** | **str** | Outcome of the test result | [optional] 
**status** | [**TestStatus**](TestStatus.md) |  | [optional] 
**result_reasons** | [**List[AutoTestResultReasonShort]**](AutoTestResultReasonShort.md) | Collection of result reasons which the test result have | 
**comment** | **str** | Comment to the test result | [optional] 
**var_date** | **datetime** | Date when the test result was completed or started or created | 
**created_date** | **datetime** | Date when the test result has been created | 
**modified_date** | **datetime** | Date when the test result has been modified | [optional] 
**started_on** | **datetime** | Date when the test result has been started | [optional] 
**completed_on** | **datetime** | Date when the test result has been completed | [optional] 
**duration** | **int** | Time which it took to run the test | [optional] 
**links** | [**List[LinkShort]**](LinkShort.md) | Collection of links attached to the test result | 
**attachments** | [**List[Attachment]**](Attachment.md) | Collection of files attached to the test result | 
**rerun_completed_count** | **int** | Run count | 

## Example

```python
from testit_api_client.models.test_result_short_response import TestResultShortResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TestResultShortResponse from a JSON string
test_result_short_response_instance = TestResultShortResponse.from_json(json)
# print the JSON string representation of the object
print(TestResultShortResponse.to_json())

# convert the object into a dict
test_result_short_response_dict = test_result_short_response_instance.to_dict()
# create an instance of TestResultShortResponse from a dict
test_result_short_response_from_dict = TestResultShortResponse.from_dict(test_result_short_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


