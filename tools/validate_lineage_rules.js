#!/usr/bin/env node
/* eslint-disable no-console */
const fs = require("fs");
const path = require("path");

function readJson(filePath) {
  return JSON.parse(fs.readFileSync(filePath, "utf8"));
}

function getSourceId(doc, filePath) {
  if (typeof doc.id === "string" && doc.id.length > 0) {
    return doc.id;
  }
  if (doc.meta && typeof doc.meta.id === "string" && doc.meta.id.length > 0) {
    return doc.meta.id;
  }
  if (
    doc.meta &&
    typeof doc.meta.externalId === "string" &&
    doc.meta.externalId.length > 0
  ) {
    return doc.meta.externalId;
  }
  return filePath;
}

function getTargetRef(edge) {
  if (!edge || typeof edge !== "object") {
    return null;
  }
  const refKey = Object.keys(edge).find((k) => k.endsWith("Ref"));
  if (!refKey) {
    return null;
  }
  const value = edge[refKey];
  return typeof value === "string" ? value : null;
}

function validateDoc(filePath) {
  const doc = readJson(filePath);
  if (!Array.isArray(doc.lineage)) {
    return [];
  }

  const source = getSourceId(doc, filePath);
  const byPair = new Map();
  const errors = [];

  for (const [idx, edge] of doc.lineage.entries()) {
    const target = getTargetRef(edge);
    const relation = edge && edge.relationship;
    if (!target || typeof relation !== "string") {
      continue;
    }

    const pairKey = `${source}=>${target}`;
    if (!byPair.has(pairKey)) {
      byPair.set(pairKey, []);
    }
    byPair.get(pairKey).push({ relation, index: idx });
  }

  for (const [pair, entries] of byPair.entries()) {
    if (entries.length > 1) {
      errors.push(
        `${filePath}: lineage has ${entries.length} relations for pair ${pair}; maximum is 1`,
      );
    }
    const hasTranslation = entries.some((e) => e.relation === "translation_of");
    const hasAdaptation = entries.some((e) => e.relation === "adaptation_of");
    if (hasTranslation && hasAdaptation) {
      errors.push(
        `${filePath}: pair ${pair} includes both translation_of and adaptation_of; translation_of must take precedence`,
      );
    }
  }

  return errors;
}

function main() {
  const examplesDir = path.join(process.cwd(), "examples", "story");
  const files = fs
    .readdirSync(examplesDir)
    .filter((f) => f.endsWith(".json"))
    .map((f) => path.join(examplesDir, f));

  const errors = files.flatMap(validateDoc);

  if (errors.length > 0) {
    console.error("Lineage rule violations:");
    for (const err of errors) {
      console.error(`- ${err}`);
    }
    process.exit(1);
  }

  console.log(
    `Lineage policy checks passed for ${files.length} story example files.`,
  );
}

main();
