# WorkflowShortApiResultReply


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[WorkflowShortApiResult]**](WorkflowShortApiResult.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from testit_api_client.models.workflow_short_api_result_reply import WorkflowShortApiResultReply

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowShortApiResultReply from a JSON string
workflow_short_api_result_reply_instance = WorkflowShortApiResultReply.from_json(json)
# print the JSON string representation of the object
print WorkflowShortApiResultReply.to_json()

# convert the object into a dict
workflow_short_api_result_reply_dict = workflow_short_api_result_reply_instance.to_dict()
# create an instance of WorkflowShortApiResultReply from a dict
workflow_short_api_result_reply_from_dict = WorkflowShortApiResultReply.from_dict(workflow_short_api_result_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


