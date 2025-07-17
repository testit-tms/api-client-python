# UpdateTestStatusApiModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the status, must be unique | 
**description** | **str** | Optional description of the status | [optional] 

## Example

```python
from testit_api_client.models.update_test_status_api_model import UpdateTestStatusApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTestStatusApiModel from a JSON string
update_test_status_api_model_instance = UpdateTestStatusApiModel.from_json(json)
# print the JSON string representation of the object
print UpdateTestStatusApiModel.to_json()

# convert the object into a dict
update_test_status_api_model_dict = update_test_status_api_model_instance.to_dict()
# create an instance of UpdateTestStatusApiModel from a dict
update_test_status_api_model_from_dict = UpdateTestStatusApiModel.from_dict(update_test_status_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


