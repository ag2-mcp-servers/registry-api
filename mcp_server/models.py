# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-28T14:48:48+00:00

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field


class Api(BaseModel):
    annotations: Optional[Dict[str, str]] = Field(
        None,
        description='Annotations attach non-identifying metadata to resources. Annotation keys and values are less restricted than those of labels, but should be generally used for small values of broad interest. Larger, topic- specific metadata should be stored in Artifacts.',
    )
    availability: Optional[str] = Field(
        None,
        description='A user-definable description of the availability of this service. Format: free-form, but we expect single words that describe availability, e.g. "NONE", "TESTING", "PREVIEW", "GENERAL", "DEPRECATED", "SHUTDOWN".',
    )
    createTime: Optional[datetime] = Field(
        None, description='Output only. Creation timestamp.'
    )
    description: Optional[str] = Field(None, description='A detailed description.')
    displayName: Optional[str] = Field(None, description='Human-meaningful name.')
    labels: Optional[Dict[str, str]] = Field(
        None,
        description='Labels attach identifying metadata to resources. Identifying metadata can be used to filter list operations. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. No more than 64 user labels can be associated with one resource (System labels are excluded). See https://goo.gl/xmQnxf for more information and examples of labels. System reserved label keys are prefixed with "apigeeregistry.googleapis.com/" and cannot be changed.',
    )
    name: Optional[str] = Field(None, description='Resource name.')
    recommendedDeployment: Optional[str] = Field(
        None,
        description='The recommended deployment of the API. Format: apis/{api}/deployments/{deployment}',
    )
    recommendedVersion: Optional[str] = Field(
        None,
        description='The recommended version of the API. Format: apis/{api}/versions/{version}',
    )
    updateTime: Optional[datetime] = Field(
        None, description='Output only. Last update timestamp.'
    )


class ApiDeployment(BaseModel):
    accessGuidance: Optional[str] = Field(
        None,
        description='Text briefly describing how to access the endpoint. Changes to this value will not affect the revision.',
    )
    annotations: Optional[Dict[str, str]] = Field(
        None,
        description='Annotations attach non-identifying metadata to resources. Annotation keys and values are less restricted than those of labels, but should be generally used for small values of broad interest. Larger, topic- specific metadata should be stored in Artifacts.',
    )
    apiSpecRevision: Optional[str] = Field(
        None,
        description='The full resource name (including revision id) of the spec of the API being served by the deployment. Changes to this value will update the revision. Format: apis/{api}/deployments/{deployment}',
    )
    createTime: Optional[datetime] = Field(
        None,
        description='Output only. Creation timestamp; when the deployment resource was created.',
    )
    description: Optional[str] = Field(None, description='A detailed description.')
    displayName: Optional[str] = Field(None, description='Human-meaningful name.')
    endpointUri: Optional[str] = Field(
        None,
        description='The address where the deployment is serving. Changes to this value will update the revision.',
    )
    externalChannelUri: Optional[str] = Field(
        None,
        description='The address of the external channel of the API (e.g. the Developer Portal). Changes to this value will not affect the revision.',
    )
    intendedAudience: Optional[str] = Field(
        None,
        description='Text briefly identifying the intended audience of the API. Changes to this value will not affect the revision.',
    )
    labels: Optional[Dict[str, str]] = Field(
        None,
        description='Labels attach identifying metadata to resources. Identifying metadata can be used to filter list operations. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. No more than 64 user labels can be associated with one resource (System labels are excluded). See https://goo.gl/xmQnxf for more information and examples of labels. System reserved label keys are prefixed with "registry.googleapis.com/" and cannot be changed.',
    )
    name: Optional[str] = Field(None, description='Resource name.')
    revisionCreateTime: Optional[datetime] = Field(
        None,
        description='Output only. Revision creation timestamp; when the represented revision was created.',
    )
    revisionId: Optional[str] = Field(
        None,
        description='Output only. Immutable. The revision ID of the deployment. A new revision is committed whenever the deployment contents are changed. The format is an 8-character hexadecimal string.',
    )
    revisionUpdateTime: Optional[datetime] = Field(
        None,
        description='Output only. Last update timestamp: when the represented revision was last modified.',
    )


class ApiSpec(BaseModel):
    annotations: Optional[Dict[str, str]] = Field(
        None,
        description='Annotations attach non-identifying metadata to resources. Annotation keys and values are less restricted than those of labels, but should be generally used for small values of broad interest. Larger, topic- specific metadata should be stored in Artifacts.',
    )
    contents: Optional[str] = Field(
        None,
        description='Input only. The contents of the spec. Provided by API callers when specs are created or updated. To access the contents of a spec, use GetApiSpecContents.',
    )
    createTime: Optional[datetime] = Field(
        None,
        description='Output only. Creation timestamp; when the spec resource was created.',
    )
    description: Optional[str] = Field(None, description='A detailed description.')
    filename: Optional[str] = Field(
        None,
        description='A possibly-hierarchical name used to refer to the spec from other specs.',
    )
    hash: Optional[str] = Field(
        None,
        description="Output only. A SHA-256 hash of the spec's contents. If the spec is gzipped, this is the hash of the uncompressed spec.",
    )
    labels: Optional[Dict[str, str]] = Field(
        None,
        description='Labels attach identifying metadata to resources. Identifying metadata can be used to filter list operations. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. No more than 64 user labels can be associated with one resource (System labels are excluded). See https://goo.gl/xmQnxf for more information and examples of labels. System reserved label keys are prefixed with "apigeeregistry.googleapis.com/" and cannot be changed.',
    )
    mimeType: Optional[str] = Field(
        None,
        description='A style (format) descriptor for this spec that is specified as a Media Type (https://en.wikipedia.org/wiki/Media_type). Possible values include "application/vnd.apigee.proto", "application/vnd.apigee.openapi", and "application/vnd.apigee.graphql", with possible suffixes representing compression types. These hypothetical names are defined in the vendor tree defined in RFC6838 (https://tools.ietf.org/html/rfc6838) and are not final. Content types can specify compression. Currently only GZip compression is supported (indicated with "+gzip").',
    )
    name: Optional[str] = Field(None, description='Resource name.')
    revisionCreateTime: Optional[datetime] = Field(
        None,
        description='Output only. Revision creation timestamp; when the represented revision was created.',
    )
    revisionId: Optional[str] = Field(
        None,
        description='Output only. Immutable. The revision ID of the spec. A new revision is committed whenever the spec contents are changed. The format is an 8-character hexadecimal string.',
    )
    revisionUpdateTime: Optional[datetime] = Field(
        None,
        description='Output only. Last update timestamp: when the represented revision was last modified.',
    )
    sizeBytes: Optional[int] = Field(
        None,
        description='Output only. The size of the spec file in bytes. If the spec is gzipped, this is the size of the uncompressed spec.',
    )
    sourceUri: Optional[str] = Field(
        None,
        description='The original source URI of the spec (if one exists). This is an external location that can be used for reference purposes but which may not be authoritative since this external resource may change after the spec is retrieved.',
    )


class ApiVersion(BaseModel):
    annotations: Optional[Dict[str, str]] = Field(
        None,
        description='Annotations attach non-identifying metadata to resources. Annotation keys and values are less restricted than those of labels, but should be generally used for small values of broad interest. Larger, topic- specific metadata should be stored in Artifacts.',
    )
    createTime: Optional[datetime] = Field(
        None, description='Output only. Creation timestamp.'
    )
    description: Optional[str] = Field(None, description='A detailed description.')
    displayName: Optional[str] = Field(None, description='Human-meaningful name.')
    labels: Optional[Dict[str, str]] = Field(
        None,
        description='Labels attach identifying metadata to resources. Identifying metadata can be used to filter list operations. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. No more than 64 user labels can be associated with one resource (System labels are excluded). See https://goo.gl/xmQnxf for more information and examples of labels. System reserved label keys are prefixed with "apigeeregistry.googleapis.com/" and cannot be changed.',
    )
    name: Optional[str] = Field(None, description='Resource name.')
    state: Optional[str] = Field(
        None,
        description='A user-definable description of the lifecycle phase of this API version. Format: free-form, but we expect single words that describe API maturity, e.g. "CONCEPT", "DESIGN", "DEVELOPMENT", "STAGING", "PRODUCTION", "DEPRECATED", "RETIRED".',
    )
    updateTime: Optional[datetime] = Field(
        None, description='Output only. Last update timestamp.'
    )


class Artifact(BaseModel):
    contents: Optional[str] = Field(
        None,
        description='Input only. The contents of the artifact. Provided by API callers when artifacts are created or replaced. To access the contents of an artifact, use GetArtifactContents.',
    )
    createTime: Optional[datetime] = Field(
        None, description='Output only. Creation timestamp.'
    )
    hash: Optional[str] = Field(
        None,
        description="Output only. A SHA-256 hash of the artifact's contents. If the artifact is gzipped, this is the hash of the uncompressed artifact.",
    )
    mimeType: Optional[str] = Field(
        None,
        description='A content type specifier for the artifact. Content type specifiers are Media Types (https://en.wikipedia.org/wiki/Media_type) with a possible "schema" parameter that specifies a schema for the stored information. Content types can specify compression. Currently only GZip compression is supported (indicated with "+gzip").',
    )
    name: Optional[str] = Field(None, description='Resource name.')
    sizeBytes: Optional[int] = Field(
        None,
        description='Output only. The size of the artifact in bytes. If the artifact is gzipped, this is the size of the uncompressed artifact.',
    )
    updateTime: Optional[datetime] = Field(
        None, description='Output only. Last update timestamp.'
    )


class GoogleProtobufAny(BaseModel):
    model_config = ConfigDict(
        extra='allow',
    )
    field_type: Optional[str] = Field(
        None, alias='@type', description='The type of the serialized message.'
    )


class ListApiDeploymentRevisionsResponse(BaseModel):
    apiDeployments: Optional[List[ApiDeployment]] = Field(
        None, description='The revisions of the deployment.'
    )
    nextPageToken: Optional[str] = Field(
        None,
        description='A token that can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.',
    )


class ListApiDeploymentsResponse(BaseModel):
    apiDeployments: Optional[List[ApiDeployment]] = Field(
        None, description='The deployments from the specified publisher.'
    )
    nextPageToken: Optional[str] = Field(
        None,
        description='A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.',
    )


class ListApiSpecRevisionsResponse(BaseModel):
    apiSpecs: Optional[List[ApiSpec]] = Field(
        None, description='The revisions of the spec.'
    )
    nextPageToken: Optional[str] = Field(
        None,
        description='A token that can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.',
    )


class ListApiSpecsResponse(BaseModel):
    apiSpecs: Optional[List[ApiSpec]] = Field(
        None, description='The specs from the specified publisher.'
    )
    nextPageToken: Optional[str] = Field(
        None,
        description='A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.',
    )


class ListApiVersionsResponse(BaseModel):
    apiVersions: Optional[List[ApiVersion]] = Field(
        None, description='The versions from the specified publisher.'
    )
    nextPageToken: Optional[str] = Field(
        None,
        description='A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.',
    )


class ListApisResponse(BaseModel):
    apis: Optional[List[Api]] = Field(
        None, description='The APIs from the specified publisher.'
    )
    nextPageToken: Optional[str] = Field(
        None,
        description='A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.',
    )


class ListArtifactsResponse(BaseModel):
    artifacts: Optional[List[Artifact]] = Field(
        None, description='The artifacts from the specified publisher.'
    )
    nextPageToken: Optional[str] = Field(
        None,
        description='A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.',
    )


class RollbackApiDeploymentRequest(BaseModel):
    name: str = Field(..., description='Required. The deployment being rolled back.')
    revisionId: str = Field(
        ...,
        description='Required. The revision ID to roll back to. It must be a revision of the same deployment.   Example: c7cfa2a8',
    )


class RollbackApiSpecRequest(BaseModel):
    name: str = Field(..., description='Required. The spec being rolled back.')
    revisionId: str = Field(
        ...,
        description='Required. The revision ID to roll back to. It must be a revision of the same spec.   Example: c7cfa2a8',
    )


class Status(BaseModel):
    code: Optional[int] = Field(
        None,
        description='The status code, which should be an enum value of [google.rpc.Code][google.rpc.Code].',
    )
    details: Optional[List[GoogleProtobufAny]] = Field(
        None,
        description='A list of messages that carry the error details.  There is a common set of message types for APIs to use.',
    )
    message: Optional[str] = Field(
        None,
        description='A developer-facing error message, which should be in English. Any user-facing error message should be localized and sent in the [google.rpc.Status.details][google.rpc.Status.details] field, or localized by the client.',
    )


class TagApiDeploymentRevisionRequest(BaseModel):
    name: str = Field(
        ...,
        description='Required. The name of the deployment to be tagged, including the revision ID.',
    )
    tag: str = Field(
        ...,
        description='Required. The tag to apply. The tag should be at most 40 characters, and match `[a-z][a-z0-9-]{3,39}`.',
    )


class TagApiSpecRevisionRequest(BaseModel):
    name: str = Field(
        ...,
        description='Required. The name of the spec to be tagged, including the revision ID.',
    )
    tag: str = Field(
        ...,
        description='Required. The tag to apply. The tag should be at most 40 characters, and match `[a-z][a-z0-9-]{3,39}`.',
    )
