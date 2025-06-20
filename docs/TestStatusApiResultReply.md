# TestStatusApiResultReply


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TestStatusApiResult]**](TestStatusApiResult.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from testit_api_client.models.test_status_api_result_reply import TestStatusApiResultReply

# TODO update the JSON string below
json = "{}"
# create an instance of TestStatusApiResultReply from a JSON string
test_status_api_result_reply_instance = TestStatusApiResultReply.from_json(json)
# print the JSON string representation of the object
print TestStatusApiResultReply.to_json()

# convert the object into a dict
test_status_api_result_reply_dict = test_status_api_result_reply_instance.to_dict()
# create an instance of TestStatusApiResultReply from a dict
test_status_api_result_reply_from_dict = TestStatusApiResultReply.from_dict(test_status_api_result_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


