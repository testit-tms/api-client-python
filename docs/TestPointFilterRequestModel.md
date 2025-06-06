# TestPointFilterRequestModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test_plan_ids** | **List[str]** | Specifies a test point test plan IDS to search for | [optional] 
**test_suite_ids** | **List[str]** | Specifies a test point test suite IDs to search for | [optional] 
**work_item_global_ids** | **List[int]** | Specifies a test point work item global IDs to search for | [optional] 
**work_item_median_duration** | [**Int64RangeSelectorModel**](Int64RangeSelectorModel.md) | Specifies a test point work item median duration range to search for | [optional] 
**work_item_is_deleted** | **bool** | Specifies a test point work item is deleted flag to search for | [optional] 
**statuses** | [**List[TestPointStatus]**](TestPointStatus.md) | Specifies a test point statuses to search for | [optional] 
**status_codes** | **List[str]** | Specifies a test point status codes to search for | [optional] 
**priorities** | [**List[WorkItemPriorityModel]**](WorkItemPriorityModel.md) | Specifies a test point priorities to search for | [optional] 
**source_types** | [**List[WorkItemSourceTypeModel]**](WorkItemSourceTypeModel.md) | Specifies a test point source types to search for | [optional] 
**is_automated** | **bool** | Specifies a test point automation status to search for | [optional] 
**name** | **str** | Specifies a test point name to search for | [optional] 
**configuration_ids** | **List[str]** | Specifies a test point configuration IDs to search for | [optional] 
**tester_ids** | **List[str]** | Specifies a test point assigned user IDs to search for | [optional] 
**duration** | [**Int64RangeSelectorModel**](Int64RangeSelectorModel.md) | Specifies a test point range of duration to search for | [optional] 
**section_ids** | **List[str]** | Specifies a test point work item section IDs to search for | [optional] 
**created_date** | [**DateTimeRangeSelectorModel**](DateTimeRangeSelectorModel.md) | Specifies a test point range of creation date to search for | [optional] 
**created_by_ids** | **List[str]** | Specifies a test point creator IDs to search for | [optional] 
**modified_date** | [**DateTimeRangeSelectorModel**](DateTimeRangeSelectorModel.md) | Specifies a test point range of last modification date to search for | [optional] 
**modified_by_ids** | **List[str]** | Specifies a test point last editor IDs to search for | [optional] 
**tags** | **List[str]** | Specifies a test point tags to search for | [optional] 
**attributes** | **Dict[str, Optional[List[str]]]** | Specifies a test point attributes to search for | [optional] 
**work_item_created_date** | [**DateTimeRangeSelectorModel**](DateTimeRangeSelectorModel.md) | Specifies a work item range of creation date to search for | [optional] 
**work_item_created_by_ids** | **List[str]** | Specifies a work item creator IDs to search for | [optional] 
**work_item_modified_date** | [**DateTimeRangeSelectorModel**](DateTimeRangeSelectorModel.md) | Specifies a work item range of last modification date to search for | [optional] 
**work_item_modified_by_ids** | **List[str]** | Specifies a work item last editor IDs to search for | [optional] 

## Example

```python
from testit_api_client.models.test_point_filter_request_model import TestPointFilterRequestModel

# TODO update the JSON string below
json = "{}"
# create an instance of TestPointFilterRequestModel from a JSON string
test_point_filter_request_model_instance = TestPointFilterRequestModel.from_json(json)
# print the JSON string representation of the object
print(TestPointFilterRequestModel.to_json())

# convert the object into a dict
test_point_filter_request_model_dict = test_point_filter_request_model_instance.to_dict()
# create an instance of TestPointFilterRequestModel from a dict
test_point_filter_request_model_from_dict = TestPointFilterRequestModel.from_dict(test_point_filter_request_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


