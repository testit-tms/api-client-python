# GetExternalFormApiResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test_result_ids** | **List[str]** | Linked test result IDs | 
**form** | [**ExternalFormModel**](ExternalFormModel.md) | External form definition | 

## Example

```python
from testit_api_client.models.get_external_form_api_result import GetExternalFormApiResult

# TODO update the JSON string below
json = "{}"
# create an instance of GetExternalFormApiResult from a JSON string
get_external_form_api_result_instance = GetExternalFormApiResult.from_json(json)
# print the JSON string representation of the object
print(GetExternalFormApiResult.to_json())

# convert the object into a dict
get_external_form_api_result_dict = get_external_form_api_result_instance.to_dict()
# create an instance of GetExternalFormApiResult from a dict
get_external_form_api_result_from_dict = GetExternalFormApiResult.from_dict(get_external_form_api_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


