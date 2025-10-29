from functools import lru_cache
import json
import os
from typing import Any, Dict, List, Mapping, Optional

from neo4j import GraphDatabase
from neo4j.graph import Node, Relationship, Path


@lru_cache(maxsize=1)
def get_driver():
    uri = os.getenv("NEO4J_URI", "bolt://localhost:7687")
    user = os.getenv("NEO4J_USER", "neo4j")
    pwd = os.getenv("NEO4J_PASSWORD", "neo4j")
    return GraphDatabase.driver(uri, auth=(user, pwd))


def run_cypher(query: str, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
    with get_driver().session() as session:
        return [_serialise_record(record) for record in session.run(query, params or {})]


def _serialise_record(record: Mapping[str, Any]) -> Dict[str, Any]:
    return {key: _serialise_value(value) for key, value in dict(record).items()}


def _serialise_value(value: Any) -> Any:
    if isinstance(value, Node):
        data: Dict[str, Any] = {
            "element_id": value.element_id,
            "labels": ":".join(sorted(value.labels)),
        }
        data.update({k: _serialise_value(v) for k, v in dict(value).items()})
        return data
    if isinstance(value, Relationship):
        data = {
            "element_id": value.element_id,
            "type": value.type,
            "start_node": value.start_node.element_id,
            "end_node": value.end_node.element_id,
        }
        data.update({k: _serialise_value(v) for k, v in dict(value).items()})
        return data
    if isinstance(value, Path):
        return {
            "nodes": [_serialise_value(node) for node in value.nodes],
            "relationships": [_serialise_value(rel) for rel in value.relationships],
        }
    if isinstance(value, Mapping):
        return {k: _serialise_value(v) for k, v in value.items()}
    if isinstance(value, (list, tuple, set, frozenset)):
        return [_serialise_value(v) for v in value]
    if isinstance(value, bytes):
        return value.decode("utf-8", errors="replace")
    if isinstance(value, (complex,)):
        return json.dumps(value, ensure_ascii=False)
    return value


def get_labels() -> List[str]:
    recs = run_cypher("CALL db.labels()")
    return sorted(r.get("label") or r.get("labels") or list(r.values())[0] for r in recs)


def get_relationship_types() -> List[str]:
    recs = run_cypher("CALL db.relationshipTypes()")
    return sorted(r.get("relationshipType") or list(r.values())[0] for r in recs)
