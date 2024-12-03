# TestRunV2PutModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**launch_source** | **str** | Once launch source is specified it cannot be updated | [optional] 
**attachments** | [**List[AttachmentPutModel]**](AttachmentPutModel.md) |  | [optional] 
**links** | [**List[LinkPutModel]**](LinkPutModel.md) |  | [optional] 

## Example

```python
from testit_api_client.models.test_run_v2_put_model import TestRunV2PutModel

# TODO update the JSON string below
json = "{}"
# create an instance of TestRunV2PutModel from a JSON string
test_run_v2_put_model_instance = TestRunV2PutModel.from_json(json)
# print the JSON string representation of the object
print(TestRunV2PutModel.to_json())

# convert the object into a dict
test_run_v2_put_model_dict = test_run_v2_put_model_instance.to_dict()
# create an instance of TestRunV2PutModel from a dict
test_run_v2_put_model_from_dict = TestRunV2PutModel.from_dict(test_run_v2_put_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


