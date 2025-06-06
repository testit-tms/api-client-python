# TestStatusModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**type** | [**TestStatusType**](TestStatusType.md) |  | 
**is_system** | **bool** |  | 
**code** | **str** |  | 
**description** | **str** |  | [optional] 

## Example

```python
from testit_api_client.models.test_status_model import TestStatusModel

# TODO update the JSON string below
json = "{}"
# create an instance of TestStatusModel from a JSON string
test_status_model_instance = TestStatusModel.from_json(json)
# print the JSON string representation of the object
print(TestStatusModel.to_json())

# convert the object into a dict
test_status_model_dict = test_status_model_instance.to_dict()
# create an instance of TestStatusModel from a dict
test_status_model_from_dict = TestStatusModel.from_dict(test_status_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


