import json
from typing import Any, Dict, List, Optional

from .neo4j_connector import run_cypher


def get_nodes_by_label(label: str, limit: int = 100) -> List[Dict[str, Any]]:
    q = f"MATCH (n:`{label}`) RETURN n LIMIT $limit"
    return run_cypher(q, {"limit": limit})


def get_graph_sample(limit: int = 100) -> Dict[str, Any]:
    nodes = run_cypher("MATCH (n) RETURN id(n) AS id, labels(n) AS labels, n AS props LIMIT $limit", {"limit": limit})
    rels = run_cypher("""
        MATCH (a)-[r]->(b)
        RETURN id(a) AS source, type(r) AS type, id(b) AS target
        LIMIT $limit
    """, {"limit": limit})
    return {"nodes": nodes, "relationships": rels}


def search_nodes(
    *,
    label: Optional[str] = None,
    relationship_type: Optional[str] = None,
    term: Optional[str] = None,
    property_key: Optional[str] = None,
    limit: int = 100,
) -> List[Dict[str, Any]]:
    node_pattern = "n"
    if label:
        node_pattern = f"n:`{label}`"

    match_clause = f"MATCH ({node_pattern})"
    if relationship_type:
        match_clause += f"-[:`{relationship_type}`]-()"

    where_clauses = []
    params: Dict[str, Any] = {"limit": limit}

    if term:
        params["term"] = term
        if property_key:
            params["prop_key"] = property_key
            where_clauses.append(
                "n[$prop_key] IS NOT NULL AND toLower(toString(n[$prop_key])) CONTAINS toLower($term)"
            )
        else:
            where_clauses.append(
                "any(k IN keys(n) WHERE toLower(toString(n[k])) CONTAINS toLower($term))"
            )

    query_parts = [match_clause]
    if where_clauses:
        query_parts.append("WHERE " + " AND ".join(where_clauses))
    query_parts.append("RETURN n LIMIT $limit")

    rows = run_cypher("\n".join(query_parts), params)
    return [row.get("n") for row in rows if row.get("n")]


def flatten_node_for_display(node: Dict[str, Any]) -> Dict[str, Any]:
    flat: Dict[str, Any] = {}

    labels = node.get("labels")
    if labels is not None:
        if isinstance(labels, str):
            flat["labels"] = labels
        else:
            flat["labels"] = ", ".join(str(v) for v in _ensure_iterable(labels))

    for key in ("name", "title", "id"):
        if key in node and node[key] is not None:
            flat[key] = node[key]

    if "element_id" in node:
        flat["element_id"] = node["element_id"]

    for key, value in node.items():
        if key in flat:
            continue
        flat[key] = _stringify(value)

    return flat


def _ensure_iterable(value: Any) -> List[Any]:
    if isinstance(value, (list, tuple, set, frozenset)):
        return list(value)
    return [value]


def _stringify(value: Any) -> Any:
    if isinstance(value, dict):
        return json.dumps(value, ensure_ascii=False)
    if isinstance(value, (list, tuple, set, frozenset)):
        return ", ".join(str(v) for v in value)
    return value
