# TestRunFillByAutoTestsPostModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | Specifies the GUID of the project, in which a test run will be created. | 
**name** | **str** | Specifies the name of the test run. | [optional] 
**configuration_ids** | **List[str]** | Specifies the configuration GUIDs, from which test points are created. You can specify several GUIDs. | 
**auto_test_external_ids** | **List[str]** | Specifies the external ID of the autotest. You can specify several IDs. | 
**description** | **str** | Specifies the test run description. | [optional] 
**launch_source** | **str** | Specifies the test run launch source. | [optional] 
**attachments** | [**List[AttachmentPutModel]**](AttachmentPutModel.md) | Collection of attachment ids to relate to the test run | [optional] 
**links** | [**List[LinkPostModel]**](LinkPostModel.md) | Collection of links to relate to the test run | [optional] 

## Example

```python
from testit_api_client.models.test_run_fill_by_auto_tests_post_model import TestRunFillByAutoTestsPostModel

# TODO update the JSON string below
json = "{}"
# create an instance of TestRunFillByAutoTestsPostModel from a JSON string
test_run_fill_by_auto_tests_post_model_instance = TestRunFillByAutoTestsPostModel.from_json(json)
# print the JSON string representation of the object
print(TestRunFillByAutoTestsPostModel.to_json())

# convert the object into a dict
test_run_fill_by_auto_tests_post_model_dict = test_run_fill_by_auto_tests_post_model_instance.to_dict()
# create an instance of TestRunFillByAutoTestsPostModel from a dict
test_run_fill_by_auto_tests_post_model_from_dict = TestRunFillByAutoTestsPostModel.from_dict(test_run_fill_by_auto_tests_post_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


