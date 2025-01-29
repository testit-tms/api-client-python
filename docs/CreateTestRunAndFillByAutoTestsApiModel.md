# CreateTestRunAndFillByAutoTestsApiModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | Specifies the GUID of the project, in which a test run will be created. | 
**name** | **str** | Specifies the name of the test run. | [optional] 
**configuration_ids** | **List[str]** | Specifies the configuration GUIDs, from which test points are created. You can specify several GUIDs. | 
**auto_test_external_ids** | **List[str]** | Specifies the external ID of the autotest. You can specify several IDs. | 
**description** | **str** | Specifies the test run description. | [optional] 
**launch_source** | **str** | Specifies the test run launch source. | [optional] 
**attachments** | [**List[AssignAttachmentApiModel]**](AssignAttachmentApiModel.md) | Collection of attachment ids to relate to the test run | [optional] 
**links** | [**List[CreateLinkApiModel]**](CreateLinkApiModel.md) | Collection of links to relate to the test run | [optional] 

## Example

```python
from testit_api_client.models.create_test_run_and_fill_by_auto_tests_api_model import CreateTestRunAndFillByAutoTestsApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTestRunAndFillByAutoTestsApiModel from a JSON string
create_test_run_and_fill_by_auto_tests_api_model_instance = CreateTestRunAndFillByAutoTestsApiModel.from_json(json)
# print the JSON string representation of the object
print(CreateTestRunAndFillByAutoTestsApiModel.to_json())

# convert the object into a dict
create_test_run_and_fill_by_auto_tests_api_model_dict = create_test_run_and_fill_by_auto_tests_api_model_instance.to_dict()
# create an instance of CreateTestRunAndFillByAutoTestsApiModel from a dict
create_test_run_and_fill_by_auto_tests_api_model_from_dict = CreateTestRunAndFillByAutoTestsApiModel.from_dict(create_test_run_and_fill_by_auto_tests_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


