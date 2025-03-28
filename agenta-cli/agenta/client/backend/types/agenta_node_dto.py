# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .lifecycle_dto import LifecycleDto
from .root_dto import RootDto
from .tree_dto import TreeDto
from .node_dto import NodeDto
from .parent_dto import ParentDto
from .time_dto import TimeDto
from .status_dto import StatusDto
from .exception_dto import ExceptionDto
from .link_dto import LinkDto
from .o_tel_extra_dto import OTelExtraDto
from .agenta_node_dto_nodes_value import AgentaNodeDtoNodesValue
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class AgentaNodeDto(UniversalBaseModel):
    lifecycle: typing.Optional[LifecycleDto] = None
    root: RootDto
    tree: TreeDto
    node: NodeDto
    parent: typing.Optional[ParentDto] = None
    time: TimeDto
    status: StatusDto
    exception: typing.Optional[ExceptionDto] = None
    data: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None
    metrics: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None
    meta: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None
    refs: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None
    links: typing.Optional[typing.List[LinkDto]] = None
    otel: typing.Optional[OTelExtraDto] = None
    nodes: typing.Optional[
        typing.Dict[str, typing.Optional[AgentaNodeDtoNodesValue]]
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(
            extra="allow", frozen=True
        )  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
