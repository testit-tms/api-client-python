# TestResultShortApiResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**outcome** | **str** |  | 
**status** | [**TestStatusApiResult**](TestStatusApiResult.md) |  | 
**traces** | **str** |  | [optional] 
**failure_type** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**test_point** | [**TestPointShortApiResult**](TestPointShortApiResult.md) |  | [optional] 
**created_date** | **datetime** |  | 
**auto_test** | [**AutoTestShortApiResult**](AutoTestShortApiResult.md) |  | [optional] 
**attachments** | [**List[AttachmentApiResult]**](AttachmentApiResult.md) |  | 

## Example

```python
from testit_api_client.models.test_result_short_api_result import TestResultShortApiResult

# TODO update the JSON string below
json = "{}"
# create an instance of TestResultShortApiResult from a JSON string
test_result_short_api_result_instance = TestResultShortApiResult.from_json(json)
# print the JSON string representation of the object
print TestResultShortApiResult.to_json()

# convert the object into a dict
test_result_short_api_result_dict = test_result_short_api_result_instance.to_dict()
# create an instance of TestResultShortApiResult from a dict
test_result_short_api_result_from_dict = TestResultShortApiResult.from_dict(test_result_short_api_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


