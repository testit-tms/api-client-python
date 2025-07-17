# TestStatusShortApiResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**code** | **str** |  | 

## Example

```python
from testit_api_client.models.test_status_short_api_result import TestStatusShortApiResult

# TODO update the JSON string below
json = "{}"
# create an instance of TestStatusShortApiResult from a JSON string
test_status_short_api_result_instance = TestStatusShortApiResult.from_json(json)
# print the JSON string representation of the object
print TestStatusShortApiResult.to_json()

# convert the object into a dict
test_status_short_api_result_dict = test_status_short_api_result_instance.to_dict()
# create an instance of TestStatusShortApiResult from a dict
test_status_short_api_result_from_dict = TestStatusShortApiResult.from_dict(test_status_short_api_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


