# CustomAttributeSearchResponseModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**work_item_usage** | [**[ProjectShortestModel]**](ProjectShortestModel.md) |  | 
**test_plan_usage** | [**[ProjectShortestModel]**](ProjectShortestModel.md) |  | 
**id** | **str** | Unique ID of the attribute. | 
**type** | [**CustomAttributeTypesEnum**](CustomAttributeTypesEnum.md) |  | 
**options** | [**[CustomAttributeOptionModel]**](CustomAttributeOptionModel.md) | Collection of the attribute options. | 
**targets** | **[str]** | Collection of the attribute targets.   Defines where the attribute can be used (e.g., TestCases, AutoTestCases, TestPlans). | 
**is_read_only** | **bool** | Indicates if the attribute is read-only. | 
**is_deleted** | **bool** | Indicates if the attribute is deleted. | 
**is_system** | **bool** | Indicates if the attribute is system. | 
**name** | **str** | Name of the attribute | 
**is_enabled** | **bool** | Indicates if the attribute is enabled | 
**is_required** | **bool** | Indicates if the attribute value is mandatory to specify | 
**is_global** | **bool** | Indicates if the attribute is available across all projects | 
**code** | **str, none_type** | Optional code identifier for the attribute. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


