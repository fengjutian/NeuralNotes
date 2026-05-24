"""Graph schemas for knowledge graph visualization."""

import uuid
from enum import Enum
from typing import Optional, Any

from pydantic import BaseModel, Field


class NodeType(str, Enum):
    """Types of nodes in the knowledge graph."""

    BOOK = "book"
    CONCEPT = "concept"
    AUTHOR = "author"
    HIGHLIGHT = "highlight"
    READER = "reader"


class EdgeType(str, Enum):
    """Types of edges in the knowledge graph."""

    HAS_CONCEPT = "has_concept"
    LIKES = "likes"
    WRITTEN_BY = "written_by"
    RELATED_TO = "related_to"
    FROM_BOOK = "from_book"


class GraphNode(BaseModel):
    """Schema for a node in the knowledge graph.

    Attributes:
        id: Unique identifier.
        type: Node type (book, concept, author, highlight, reader).
        label: Display label for the node.
        properties: Additional node properties.
    """

    id: str = Field(..., description="Unique node identifier")
    type: NodeType = Field(..., description="Node type")
    label: str = Field(..., description="Display label")
    properties: dict[str, Any] = Field(
        default_factory=dict,
        description="Additional node properties",
    )


class GraphEdge(BaseModel):
    """Schema for an edge in the knowledge graph.

    Attributes:
        source: Source node ID.
        target: Target node ID.
        type: Edge type (relationship).
        properties: Additional edge properties.
    """

    source: str = Field(..., description="Source node ID")
    target: str = Field(..., description="Target node ID")
    type: EdgeType = Field(..., description="Edge type")
    properties: dict[str, Any] = Field(
        default_factory=dict,
        description="Additional edge properties",
    )


class GraphResponse(BaseModel):
    """Schema for full graph response.

    Attributes:
        nodes: List of graph nodes.
        edges: List of graph edges.
        total_nodes: Total number of nodes.
        total_edges: Total number of edges.
    """

    nodes: list[GraphNode] = Field(default_factory=list)
    edges: list[GraphEdge] = Field(default_factory=list)
    total_nodes: int = Field(default=0)
    total_edges: int = Field(default=0)


class NodeDetailRequest(BaseModel):
    """Schema for requesting node details."""

    node_id: str = Field(..., description="Node ID to get details for")
    node_type: NodeType = Field(..., description="Node type")


class NodeDetailResponse(BaseModel):
    """Schema for node details response."""

    node: GraphNode
    related_nodes: list[GraphNode] = Field(default_factory=list)
    highlights: list[dict[str, Any]] = Field(default_factory=list)
    books: list[dict[str, Any]] = Field(default_factory=list)
