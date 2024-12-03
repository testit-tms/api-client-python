# TestStatusUpdateModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | [optional] 

## Example

```python
from testit_api_client.models.test_status_update_model import TestStatusUpdateModel

# TODO update the JSON string below
json = "{}"
# create an instance of TestStatusUpdateModel from a JSON string
test_status_update_model_instance = TestStatusUpdateModel.from_json(json)
# print the JSON string representation of the object
print(TestStatusUpdateModel.to_json())

# convert the object into a dict
test_status_update_model_dict = test_status_update_model_instance.to_dict()
# create an instance of TestStatusUpdateModel from a dict
test_status_update_model_from_dict = TestStatusUpdateModel.from_dict(test_status_update_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


