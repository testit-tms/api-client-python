# TestRunV2PostShortModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | This property is to link test run with a project | 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**launch_source** | **str** |  | [optional] 
**attachments** | [**List[AttachmentPutModel]**](AttachmentPutModel.md) |  | [optional] 
**links** | [**List[LinkPostModel]**](LinkPostModel.md) |  | [optional] 

## Example

```python
from testit_api_client.models.test_run_v2_post_short_model import TestRunV2PostShortModel

# TODO update the JSON string below
json = "{}"
# create an instance of TestRunV2PostShortModel from a JSON string
test_run_v2_post_short_model_instance = TestRunV2PostShortModel.from_json(json)
# print the JSON string representation of the object
print(TestRunV2PostShortModel.to_json())

# convert the object into a dict
test_run_v2_post_short_model_dict = test_run_v2_post_short_model_instance.to_dict()
# create an instance of TestRunV2PostShortModel from a dict
test_run_v2_post_short_model_from_dict = TestRunV2PostShortModel.from_dict(test_run_v2_post_short_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


