# TestRunFillByWorkItemsPostModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration_ids** | **List[str]** | Specifies the configuration GUIDs, from which test points are created. You can specify several GUIDs. | 
**work_item_ids** | **List[str]** | Specifies the work item GUIDs, from which test points are created. You can specify several GUIDs. | 
**project_id** | **str** | Specifies the GUID of the project, in which a test run will be created. | 
**test_plan_id** | **str** | Specifies the GUID of the test plan, within which the test run will be created. | 
**name** | **str** | Specifies the name of the test run. | [optional] 
**description** | **str** | Specifies the test run description. | [optional] 
**launch_source** | **str** | Specifies the test run launch source. | [optional] 
**attachments** | [**List[AttachmentPutModel]**](AttachmentPutModel.md) | Collection of attachment ids to relate to the test run | [optional] 
**links** | [**List[LinkPostModel]**](LinkPostModel.md) | Collection of links to relate to the test run | [optional] 

## Example

```python
from testit_api_client.models.test_run_fill_by_work_items_post_model import TestRunFillByWorkItemsPostModel

# TODO update the JSON string below
json = "{}"
# create an instance of TestRunFillByWorkItemsPostModel from a JSON string
test_run_fill_by_work_items_post_model_instance = TestRunFillByWorkItemsPostModel.from_json(json)
# print the JSON string representation of the object
print(TestRunFillByWorkItemsPostModel.to_json())

# convert the object into a dict
test_run_fill_by_work_items_post_model_dict = test_run_fill_by_work_items_post_model_instance.to_dict()
# create an instance of TestRunFillByWorkItemsPostModel from a dict
test_run_fill_by_work_items_post_model_from_dict = TestRunFillByWorkItemsPostModel.from_dict(test_run_fill_by_work_items_post_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


