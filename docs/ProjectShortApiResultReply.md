# ProjectShortApiResultReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ProjectShortApiResult]**](ProjectShortApiResult.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from testit_api_client.models.project_short_api_result_reply import ProjectShortApiResultReply

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectShortApiResultReply from a JSON string
project_short_api_result_reply_instance = ProjectShortApiResultReply.from_json(json)
# print the JSON string representation of the object
print(ProjectShortApiResultReply.to_json())

# convert the object into a dict
project_short_api_result_reply_dict = project_short_api_result_reply_instance.to_dict()
# create an instance of ProjectShortApiResultReply from a dict
project_short_api_result_reply_from_dict = ProjectShortApiResultReply.from_dict(project_short_api_result_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


