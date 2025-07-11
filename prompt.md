
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










output form gpt
[
  {
    "source_element": "Payer type",
    "target_column": "SOURCE",
    "validation_score": 90,
    "comments": "Text to VARCHAR2 type match is good; target length (20) sufficient for source max length (1); lookup used properly."
  },
  {
    "source_element": "Claim ID",
    "target_column": "SN",
    "validation_score": 85,
    "comments": "Source max length (80) exceeds target length (10) but cast to NUMBER; may risk truncation or conversion issues."
  },
  {
    "source_element": "Member ID",
    "target_column": "MEMBER_ID",
    "validation_score": 90,
    "comments": "Target length (20) less than source max length (30), minor length risk; transformation and types compatible."
  },
  {
    "source_element": "Rendering provider ID",
    "target_column": "PROVIDER_ID",
    "validation_score": 90,
    "comments": "Similar to MEMBER_ID, length slightly short; casting and type mapping acceptable."
  },
  {
    "source_element": "Charges",
    "target_column": "AMOUNT",
    "validation_score": 95,
    "comments": "Numeric to NUMBER mapping correct; minor length difference (12 source vs 10 target)."
  },
  {
    "source_element": "Principal diagnosis",
    "target_column": "DIAGNOSIS_CODE",
    "validation_score": 95,
    "comments": "Target length (10) greater than source max length (8), good casting."
  },
  {
    "source_element": "CPT/CPT II/HCPCS/HIPPS Procedure code",
    "target_column": "PROCEDURE_CODE",
    "validation_score": 95,
    "comments": "Target length (10) greater than source max length (5), casting correct."
  },
  {
    "source_element": "Admission date",
    "target_column": "HOSPITALIZATION_ID",
    "validation_score": 90,
    "comments": "Casting Date to VARCHAR2 may lose date semantics; length is sufficient."
  },
  {
    "source_element": "Payer type",
    "target_column": "ELIGIBILITY_STATUS",
    "validation_score": 90,
    "comments": "Similar to SOURCE; lookup usage appropriate."
  },
  {
    "source_element": "Patient name",
    "target_column": "PATIENT_NAME",
    "validation_score": 100,
    "comments": "Perfect match in data type and length."
  },
  {
    "source_element": "Pharmacy ID",
    "target_column": "PHARMACY_ID",
    "validation_score": 100,
    "comments": "Exact length and compatible types."
  },
  {
    "source_element": "Claim status",
    "target_column": "STATUS",
    "validation_score": 95,
    "comments": "Source max length (1) fits well within target length (20); casting appropriate."
  },
  {
    "source_element": "Audit date",
    "target_column": "AUDIT_DATE",
    "validation_score": 100,
    "comments": "Date to Date casting exact and appropriate."
  },
  {
    "source_element": "Miscellaneous data",
    "target_column": "MISC_DATA",
    "validation_score": 100,
    "comments": "Full length and type compatibility; transformation is correct."
  }
]
