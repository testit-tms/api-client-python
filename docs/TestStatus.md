# TestStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**type** | [**TestStatusType**](TestStatusType.md) |  | 
**is_based** | **bool** |  | 
**is_default** | **bool** |  | 
**code** | **str** |  | 
**description** | **str** |  | [optional] 

## Example

```python
from testit_api_client.models.test_status import TestStatus

# TODO update the JSON string below
json = "{}"
# create an instance of TestStatus from a JSON string
test_status_instance = TestStatus.from_json(json)
# print the JSON string representation of the object
print(TestStatus.to_json())

# convert the object into a dict
test_status_dict = test_status_instance.to_dict()
# create an instance of TestStatus from a dict
test_status_from_dict = TestStatus.from_dict(test_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


