
You are a data integration expert.

Your task is to evaluate the correctness of each field mapping between a source field (from a legacy data system) and a target column (in the target database schema).

For each mapping in the provided list, assess:

1. ✅ Does the source field logically map to the target column?
2. ✅ Are the data types compatible and appropriate?
3. ✅ Is the transformation rule syntactically and logically correct?
4. ✅ Is the mapping comment clear and helpful?
5. ✅ Is the use of lookup references appropriate (if any)?
6. ✅ Use supporting context from `mergeKey`, `targetMetadata`, and `sourceMetadata` if needed to determine accuracy.

---

### Use the following inputs:

- **Field Mappings to Validate**:
```json
{{ $json.mappings }}
````

* **Target Metadata** (for validation of schema & columns):

```json
{{ $json.targetMetadata }}
```

* **Source Metadata** (for reference to source element definitions):

```json
{{ $json.sourceMetadata }}
```

* **Merge Key** (to determine join context or table relevance):

```
{{ $json.mergeKey }}
```

---

### ✅ For each mapping, return a response in this format:

```json
{
  "target_column": "<column name>",
  "verdict": "Valid" | "Partially Valid" | "Invalid",
  "score": {
    "mapping_correctness": 1-5,
    "transformation_logic": 1-5,
    "comment_clarity": 1-5
  },
  "feedback": "Explain your reasoning here clearly, pointing out any flaws or confirmations."
}
```

```


