# CreateTestRunAndFillByConfigurationsApiModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | Specifies the GUID of the project, in which a test run will be created. | 
**test_plan_id** | **str** | Specifies the GUID of the test plan, within which the test run will be created. | 
**name** | **str** | Specifies the name of the test run. | [optional] 
**description** | **str** | Specifies the test run description. | [optional] 
**launch_source** | **str** | Specifies the test run launch source. | [optional] 
**attachments** | [**List[AssignAttachmentApiModel]**](AssignAttachmentApiModel.md) | Collection of attachment ids to relate to the test run | [optional] 
**links** | [**List[CreateLinkApiModel]**](CreateLinkApiModel.md) | Collection of links to relate to the test run | [optional] 
**test_point_selectors** | [**List[TestPointSelector]**](TestPointSelector.md) | Specifies an array of work items and configuration to create a test run for. | 

## Example

```python
from testit_api_client.models.create_test_run_and_fill_by_configurations_api_model import CreateTestRunAndFillByConfigurationsApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTestRunAndFillByConfigurationsApiModel from a JSON string
create_test_run_and_fill_by_configurations_api_model_instance = CreateTestRunAndFillByConfigurationsApiModel.from_json(json)
# print the JSON string representation of the object
print CreateTestRunAndFillByConfigurationsApiModel.to_json()

# convert the object into a dict
create_test_run_and_fill_by_configurations_api_model_dict = create_test_run_and_fill_by_configurations_api_model_instance.to_dict()
# create an instance of CreateTestRunAndFillByConfigurationsApiModel from a dict
create_test_run_and_fill_by_configurations_api_model_from_dict = CreateTestRunAndFillByConfigurationsApiModel.from_dict(create_test_run_and_fill_by_configurations_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


