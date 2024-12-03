# TestStatusCreateModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**type** | [**TestStatusType**](TestStatusType.md) |  | 
**code** | **str** |  | 
**description** | **str** |  | [optional] 

## Example

```python
from testit_api_client.models.test_status_create_model import TestStatusCreateModel

# TODO update the JSON string below
json = "{}"
# create an instance of TestStatusCreateModel from a JSON string
test_status_create_model_instance = TestStatusCreateModel.from_json(json)
# print the JSON string representation of the object
print(TestStatusCreateModel.to_json())

# convert the object into a dict
test_status_create_model_dict = test_status_create_model_instance.to_dict()
# create an instance of TestStatusCreateModel from a dict
test_status_create_model_from_dict = TestStatusCreateModel.from_dict(test_status_create_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


