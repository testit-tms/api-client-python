# StepPostModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | [optional] 
**expected** | **str** |  | [optional] 
**test_data** | **str** |  | [optional] 
**comments** | **str** |  | [optional] 
**work_item_id** | **str** |  | [optional] 

## Example

```python
from testit_api_client.models.step_post_model import StepPostModel

# TODO update the JSON string below
json = "{}"
# create an instance of StepPostModel from a JSON string
step_post_model_instance = StepPostModel.from_json(json)
# print the JSON string representation of the object
print StepPostModel.to_json()

# convert the object into a dict
step_post_model_dict = step_post_model_instance.to_dict()
# create an instance of StepPostModel from a dict
step_post_model_from_dict = StepPostModel.from_dict(step_post_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


