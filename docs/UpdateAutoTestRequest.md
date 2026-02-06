# UpdateAutoTestRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | Unique ID of the autotest project | 
**external_id** | **str** | External ID of the autotest | 
**name** | **str** | Name of the autotest | 
**id** | **str, none_type** | Autotest unique internal identifier | [optional] 
**external_key** | **str, none_type** | External key of the autotest | [optional] 
**namespace** | **str, none_type** | Name of the autotest namespace | [optional] 
**classname** | **str, none_type** | Name of the autotest class | [optional] 
**title** | **str, none_type** | Name of the autotest in autotest&#39;s card | [optional] 
**description** | **str, none_type** | Description of the autotest in autotest&#39;s card | [optional] 
**is_flaky** | **bool, none_type** | Indicates if the autotest is marked as flaky | [optional] 
**steps** | [**[AutoTestStepApiModel], none_type**](AutoTestStepApiModel.md) | Collection of the autotest steps | [optional] 
**setup** | [**[AutoTestStepApiModel], none_type**](AutoTestStepApiModel.md) | Collection of the autotest setup steps | [optional] 
**teardown** | [**[AutoTestStepApiModel], none_type**](AutoTestStepApiModel.md) | Collection of the autotest teardown steps | [optional] 
**work_item_ids** | **[str], none_type** | Specifies the IDs of work items to link your autotest to. You can specify several IDs. | [optional] 
**work_item_ids_for_link_with_auto_test** | **[str], none_type** | Specifies the IDs of work items to link your autotest to. You can specify several IDs. | [optional] 
**labels** | [**[LabelApiModel], none_type**](LabelApiModel.md) | Collection of the autotest labels | [optional] 
**links** | [**[LinkUpdateApiModel], none_type**](LinkUpdateApiModel.md) | Collection of the autotest links | [optional] 
**tags** | **[str], none_type** | Collection of the autotest tags | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


