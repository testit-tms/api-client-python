# CreateTestStatusApiModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the status, must be unique | 
**type** | [**TestStatusApiType**](TestStatusApiType.md) | Type of the status | 
**code** | **str** | Code of the status, must be unique | 
**description** | **str** | Optional description of the status | [optional] 

## Example

```python
from testit_api_client.models.create_test_status_api_model import CreateTestStatusApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTestStatusApiModel from a JSON string
create_test_status_api_model_instance = CreateTestStatusApiModel.from_json(json)
# print the JSON string representation of the object
print(CreateTestStatusApiModel.to_json())

# convert the object into a dict
create_test_status_api_model_dict = create_test_status_api_model_instance.to_dict()
# create an instance of CreateTestStatusApiModel from a dict
create_test_status_api_model_from_dict = CreateTestStatusApiModel.from_dict(create_test_status_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


