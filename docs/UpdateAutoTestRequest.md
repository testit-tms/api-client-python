# UpdateAutoTestRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_id** | **str** | External ID of the autotest | 
**project_id** | **str** | Unique ID of the autotest project | 
**name** | **str** | Name of the autotest | 
**id** | **str, none_type** | Used for search autotest. If value is null or equals Guid mask filled with zeros, search will be executed using ExternalId | [optional] 
**work_item_ids_for_link_with_auto_test** | **[str], none_type** |  | [optional] 
**work_item_ids** | **[str], none_type** |  | [optional] 
**links** | [**[LinkPutModel], none_type**](LinkPutModel.md) | Collection of the autotest links | [optional] 
**namespace** | **str, none_type** | Name of the autotest namespace | [optional] 
**classname** | **str, none_type** | Name of the autotest class | [optional] 
**steps** | [**[AutoTestStepModel], none_type**](AutoTestStepModel.md) | Collection of the autotest steps | [optional] 
**setup** | [**[AutoTestStepModel], none_type**](AutoTestStepModel.md) | Collection of the autotest setup steps | [optional] 
**teardown** | [**[AutoTestStepModel], none_type**](AutoTestStepModel.md) | Collection of the autotest teardown steps | [optional] 
**title** | **str, none_type** | Name of the autotest in autotest&#39;s card | [optional] 
**description** | **str, none_type** | Description of the autotest in autotest&#39;s card | [optional] 
**labels** | [**[LabelPostModel], none_type**](LabelPostModel.md) | Collection of the autotest labels | [optional] 
**is_flaky** | **bool, none_type** | Indicates if the autotest is marked as flaky | [optional] 
**external_key** | **str, none_type** | External key of the autotest | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


