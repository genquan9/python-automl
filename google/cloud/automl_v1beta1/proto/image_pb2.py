# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/automl_v1beta1/proto/image.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.cloud.automl_v1beta1.proto import (
    classification_pb2 as google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_classification__pb2,
)
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/automl_v1beta1/proto/image.proto",
    package="google.cloud.automl.v1beta1",
    syntax="proto3",
    serialized_pb=_b(
        '\n-google/cloud/automl_v1beta1/proto/image.proto\x12\x1bgoogle.cloud.automl.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x36google/cloud/automl_v1beta1/proto/classification.proto\x1a\x1fgoogle/protobuf/timestamp.proto"r\n"ImageClassificationDatasetMetadata\x12L\n\x13\x63lassification_type\x18\x01 \x01(\x0e\x32/.google.cloud.automl.v1beta1.ClassificationType"x\n ImageClassificationModelMetadata\x12\x15\n\rbase_model_id\x18\x01 \x01(\t\x12\x14\n\x0ctrain_budget\x18\x02 \x01(\x03\x12\x12\n\ntrain_cost\x18\x03 \x01(\x03\x12\x13\n\x0bstop_reason\x18\x05 \x01(\tBr\n\x1f\x63om.google.cloud.automl.v1beta1B\nImageProtoP\x01ZAgoogle.golang.org/genproto/googleapis/cloud/automl/v1beta1;automlb\x06proto3'
    ),
    dependencies=[
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
        google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_classification__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,
    ],
)


_IMAGECLASSIFICATIONDATASETMETADATA = _descriptor.Descriptor(
    name="ImageClassificationDatasetMetadata",
    full_name="google.cloud.automl.v1beta1.ImageClassificationDatasetMetadata",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="classification_type",
            full_name="google.cloud.automl.v1beta1.ImageClassificationDatasetMetadata.classification_type",
            index=0,
            number=1,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=197,
    serialized_end=311,
)


_IMAGECLASSIFICATIONMODELMETADATA = _descriptor.Descriptor(
    name="ImageClassificationModelMetadata",
    full_name="google.cloud.automl.v1beta1.ImageClassificationModelMetadata",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="base_model_id",
            full_name="google.cloud.automl.v1beta1.ImageClassificationModelMetadata.base_model_id",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="train_budget",
            full_name="google.cloud.automl.v1beta1.ImageClassificationModelMetadata.train_budget",
            index=1,
            number=2,
            type=3,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="train_cost",
            full_name="google.cloud.automl.v1beta1.ImageClassificationModelMetadata.train_cost",
            index=2,
            number=3,
            type=3,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="stop_reason",
            full_name="google.cloud.automl.v1beta1.ImageClassificationModelMetadata.stop_reason",
            index=3,
            number=5,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=313,
    serialized_end=433,
)

_IMAGECLASSIFICATIONDATASETMETADATA.fields_by_name[
    "classification_type"
].enum_type = (
    google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_classification__pb2._CLASSIFICATIONTYPE
)
DESCRIPTOR.message_types_by_name[
    "ImageClassificationDatasetMetadata"
] = _IMAGECLASSIFICATIONDATASETMETADATA
DESCRIPTOR.message_types_by_name[
    "ImageClassificationModelMetadata"
] = _IMAGECLASSIFICATIONMODELMETADATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ImageClassificationDatasetMetadata = _reflection.GeneratedProtocolMessageType(
    "ImageClassificationDatasetMetadata",
    (_message.Message,),
    dict(
        DESCRIPTOR=_IMAGECLASSIFICATIONDATASETMETADATA,
        __module__="google.cloud.automl_v1beta1.proto.image_pb2",
        __doc__="""Dataset metadata that is specific to image classification.
  
  
  Attributes:
      classification_type:
          Required. Type of the classification problem.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.ImageClassificationDatasetMetadata)
    ),
)
_sym_db.RegisterMessage(ImageClassificationDatasetMetadata)

ImageClassificationModelMetadata = _reflection.GeneratedProtocolMessageType(
    "ImageClassificationModelMetadata",
    (_message.Message,),
    dict(
        DESCRIPTOR=_IMAGECLASSIFICATIONMODELMETADATA,
        __module__="google.cloud.automl_v1beta1.proto.image_pb2",
        __doc__="""Model metadata for image classification.
  
  
  Attributes:
      base_model_id:
          Optional. The ID of the ``base`` model. If it is specified,
          the new model will be created based on the ``base`` model.
          Otherwise, the new model will be created from scratch. The
          ``base`` model is expected to be in the same ``project`` and
          ``location`` as the new model to create.
      train_budget:
          Required. The train budget of creating this model. The actual
          ``train_cost`` will be equal or less than this value.
      train_cost:
          Output only. The actual train cost of creating this model. If
          this model is created from a ``base`` model, the train cost
          used to create the ``base`` model are not included.
      stop_reason:
          Output only. The reason that this create model operation
          stopped, e.g. BUDGET\_REACHED, CONVERGED.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.ImageClassificationModelMetadata)
    ),
)
_sym_db.RegisterMessage(ImageClassificationModelMetadata)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(
    descriptor_pb2.FileOptions(),
    _b(
        "\n\037com.google.cloud.automl.v1beta1B\nImageProtoP\001ZAgoogle.golang.org/genproto/googleapis/cloud/automl/v1beta1;automl"
    ),
)
# @@protoc_insertion_point(module_scope)
