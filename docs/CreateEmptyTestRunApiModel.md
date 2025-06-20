# CreateEmptyTestRunApiModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | Project unique identifier              This property is to link test run with a project | 
**name** | **str** | Test run name | [optional] 
**description** | **str** | Test run description | [optional] 
**launch_source** | **str** | Test run launch source | [optional] 
**attachments** | [**List[AssignAttachmentApiModel]**](AssignAttachmentApiModel.md) | Collection of attachments to relate to the test run | [optional] 
**links** | [**List[CreateLinkApiModel]**](CreateLinkApiModel.md) | Collection of links to relate to the test run | [optional] 

## Example

```python
from testit_api_client.models.create_empty_test_run_api_model import CreateEmptyTestRunApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEmptyTestRunApiModel from a JSON string
create_empty_test_run_api_model_instance = CreateEmptyTestRunApiModel.from_json(json)
# print the JSON string representation of the object
print CreateEmptyTestRunApiModel.to_json()

# convert the object into a dict
create_empty_test_run_api_model_dict = create_empty_test_run_api_model_instance.to_dict()
# create an instance of CreateEmptyTestRunApiModel from a dict
create_empty_test_run_api_model_from_dict = CreateEmptyTestRunApiModel.from_dict(create_empty_test_run_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


