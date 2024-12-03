# TestRunFillByConfigurationsPostModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test_point_selectors** | [**List[TestPointSelector]**](TestPointSelector.md) | Specifies an array of work items and configuration to create a test run for. | 
**project_id** | **str** | Specifies the GUID of the project, in which a test run will be created. | 
**test_plan_id** | **str** | Specifies the GUID of the test plan, within which the test run will be created. | 
**name** | **str** | Specifies the name of the test run. | [optional] 
**description** | **str** | Specifies the test run description. | [optional] 
**launch_source** | **str** | Specifies the test run launch source. | [optional] 
**attachments** | [**List[AttachmentPutModel]**](AttachmentPutModel.md) | Collection of attachment ids to relate to the test run | [optional] 
**links** | [**List[LinkPostModel]**](LinkPostModel.md) | Collection of links to relate to the test run | [optional] 

## Example

```python
from testit_api_client.models.test_run_fill_by_configurations_post_model import TestRunFillByConfigurationsPostModel

# TODO update the JSON string below
json = "{}"
# create an instance of TestRunFillByConfigurationsPostModel from a JSON string
test_run_fill_by_configurations_post_model_instance = TestRunFillByConfigurationsPostModel.from_json(json)
# print the JSON string representation of the object
print(TestRunFillByConfigurationsPostModel.to_json())

# convert the object into a dict
test_run_fill_by_configurations_post_model_dict = test_run_fill_by_configurations_post_model_instance.to_dict()
# create an instance of TestRunFillByConfigurationsPostModel from a dict
test_run_fill_by_configurations_post_model_from_dict = TestRunFillByConfigurationsPostModel.from_dict(test_run_fill_by_configurations_post_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


