# AuditApiResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**user_name** | **str** |  | [optional] 
**date_time** | **datetime** |  | 

## Example

```python
from testit_api_client.models.audit_api_result import AuditApiResult

# TODO update the JSON string below
json = "{}"
# create an instance of AuditApiResult from a JSON string
audit_api_result_instance = AuditApiResult.from_json(json)
# print the JSON string representation of the object
print AuditApiResult.to_json()

# convert the object into a dict
audit_api_result_dict = audit_api_result_instance.to_dict()
# create an instance of AuditApiResult from a dict
audit_api_result_from_dict = AuditApiResult.from_dict(audit_api_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


