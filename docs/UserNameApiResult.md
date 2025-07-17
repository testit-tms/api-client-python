# UserNameApiResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | [optional] 

## Example

```python
from testit_api_client.models.user_name_api_result import UserNameApiResult

# TODO update the JSON string below
json = "{}"
# create an instance of UserNameApiResult from a JSON string
user_name_api_result_instance = UserNameApiResult.from_json(json)
# print the JSON string representation of the object
print UserNameApiResult.to_json()

# convert the object into a dict
user_name_api_result_dict = user_name_api_result_instance.to_dict()
# create an instance of UserNameApiResult from a dict
user_name_api_result_from_dict = UserNameApiResult.from_dict(user_name_api_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


