"""
Import JSON data to Neo4j database.

Supports multiple JSON formats:
- Node/Relationship format ({"nodes": [...], "relationships": [...]})
- Enrichment format ({"enrichments": [...]})

Usage:
    python scripts/import_to_neo4j.py <json_file>
"""

import os
import sys
import json
from pathlib import Path
from dotenv import load_dotenv
from neo4j import GraphDatabase
from scripts.utils import setup_logger

# Load environment
load_dotenv()

# Configure logging
logger = setup_logger("import", log_file="output/logs/import_to_neo4j.log")

# Neo4j connection
NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USER = os.getenv("NEO4J_USER")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")


class Neo4jImporter:
    """Import data to Neo4j database."""

    def __init__(self):
        self.driver = GraphDatabase.driver(
            NEO4J_URI,
            auth=(NEO4J_USER, NEO4J_PASSWORD)
        )

    def close(self):
        """Close database connection."""
        self.driver.close()

    def import_nodes(self, nodes):
        """Import nodes to Neo4j."""
        logger.info("Importing %d nodes...", len(nodes))

        count = 0
        with self.driver.session() as session:
            for node in nodes:
                labels = ":".join(node.get("labels", ["Node"]))
                node_id = node["properties"]["id"]
                properties = node["properties"]

                query = f"""
                MERGE (n:{labels} {{id: $id}})
                SET n += $props
                RETURN count(n) as created
                """

                result = session.run(query, id=node_id, props=properties)
                count += result.single()["created"]

        logger.info("Imported %d nodes", count)
        return count

    def import_relationships(self, relationships):
        """Import relationships to Neo4j."""
        logger.info("Importing %d relationships...", len(relationships))

        count = 0
        with self.driver.session() as session:
            for rel in relationships:
                source_id = rel["source_id"]
                target_id = rel["target_id"]
                rel_type = rel["type"]
                properties = rel.get("properties", {})

                query = f"""
                MATCH (source {{id: $source_id}})
                MATCH (target {{id: $target_id}})
                MERGE (source)-[r:{rel_type}]->(target)
                SET r += $props
                RETURN count(r) as created
                """

                result = session.run(
                    query,
                    source_id=source_id,
                    target_id=target_id,
                    props=properties
                )
                count += result.single()["created"]

        logger.info("Imported %d relationships", count)
        return count

    def import_file(self, json_file):
        """Import data from JSON file."""
        logger.info("Loading data from %s", json_file)

        data = json.loads(Path(json_file).read_text())

        # Import nodes
        if "nodes" in data:
            self.import_nodes(data["nodes"])

        # Import relationships
        if "relationships" in data:
            self.import_relationships(data["relationships"])

        logger.info("Import complete!")


def main():
    """Main execution."""
    if len(sys.argv) < 2:
        print("Usage: python scripts/import_to_neo4j.py <json_file>")
        sys.exit(1)

    json_file = sys.argv[1]

    if not Path(json_file).exists():
        logger.error("File not found: %s", json_file)
        sys.exit(1)

    importer = Neo4jImporter()

    try:
        importer.import_file(json_file)
    finally:
        importer.close()


if __name__ == "__main__":
    main()
