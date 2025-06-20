# TestSuiteV2PutModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**parent_id** | **str** |  | [optional] 
**name** | **str** |  | 
**is_deleted** | **bool** |  | 
**auto_refresh** | **bool** |  | [optional] 

## Example

```python
from testit_api_client.models.test_suite_v2_put_model import TestSuiteV2PutModel

# TODO update the JSON string below
json = "{}"
# create an instance of TestSuiteV2PutModel from a JSON string
test_suite_v2_put_model_instance = TestSuiteV2PutModel.from_json(json)
# print the JSON string representation of the object
print(TestSuiteV2PutModel.to_json())

# convert the object into a dict
test_suite_v2_put_model_dict = test_suite_v2_put_model_instance.to_dict()
# create an instance of TestSuiteV2PutModel from a dict
test_suite_v2_put_model_from_dict = TestSuiteV2PutModel.from_dict(test_suite_v2_put_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


