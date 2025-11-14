# Security Vulnerability Detection Tool

This tool implements a framework for detecting security vulnerabilities by tracking information flows from sources to sinks, accounting for sanitizers that may neutralize potential vulnerabilities.

## Classes

### 1. Pattern Class

Represents a vulnerability pattern with its components.

**Constructor:**

```python
Pattern(name, sources, sanitizers, sinks)
```

- `name`: String identifying the vulnerability type (e.g., "SQL Injection")
- `sources`: List of function/variable names that introduce untrusted data
- `sanitizers`: List of function names that can neutralize the vulnerability
- `sinks`: List of function/variable names that are sensitive endpoints

**Methods:**

- `get_name()`: Returns the pattern name
- `get_sources()`: Returns set of source names
- `get_sanitizers()`: Returns set of sanitizer names
- `get_sinks()`: Returns set of sink names
- `is_source(name)`: Tests if name is a source
- `is_sanitizer(name)`: Tests if name is a sanitizer
- `is_sink(name)`: Tests if name is a sink

### 2. Label Class

Represents the integrity of information in a resource by tracking which sources have influenced it and which sanitizers have intercepted the flows.

**Label Structure:**

```python
{
    source1: {sanitizer1, sanitizer2},
    source2: {sanitizer1},
    ...
}
```

This structure allows tracking different flows from the same source independently. For example, if `source1` influences a variable through two different paths, and one path is sanitized by `san1` and `san2` while another is only sanitized by `san1`, the label can distinguish these cases.

**Constructor:**

```python
Label(source_flows=None)
```

- `source_flows`: Optional dictionary mapping sources to sets of sanitizers

**Methods:**

- `add_source(source)`: Adds a source without sanitizers
- `add_sanitizer(sanitizer)`: Adds a sanitizer to all current sources
- `add_sanitizer_for_source(source, sanitizer)`: Adds sanitizer for specific source
- `get_sources()`: Returns set of all sources
- `get_sanitizers_for_source(source)`: Returns sanitizers for a specific source
- `get_all_sanitizers()`: Returns all sanitizers across all sources
- `get_source_flows()`: Returns complete source-to-sanitizers mapping
- `is_empty()`: Checks if label has no sources
- `combine(other)`: Returns new label combining information from two labels

**Important:** Labels are mutable and the `combine()` method returns a new independent label.

### 3. MultiLabel Class

Enables tracking multiple vulnerability patterns simultaneously by maintaining separate labels for each pattern.

**Constructor:**

```python
MultiLabel(patterns=None)
```

- `patterns`: Optional list of Pattern objects to track

**Methods:**

- `add_pattern(pattern)`: Adds a new pattern to track
- `add_source(source_name)`: Adds source to labels of patterns where it's defined as a source
- `add_sanitizer(sanitizer_name)`: Adds sanitizer to labels of patterns where it's defined as a sanitizer
- `get_patterns()`: Returns list of pattern names
- `get_pattern(pattern_name)`: Returns specific Pattern object
- `get_label(pattern_name)`: Returns label for specific pattern
- `get_all_labels()`: Returns all labels
- `combine(other)`: Returns new MultiLabel combining two MultiLabels

**Key Feature:** Sources and sanitizers are only added to labels corresponding to patterns for which that name is registered as a source/sanitizer.

## Example Usage

```python
# Define a SQL Injection pattern
sql_pattern = Pattern(
    name="SQL Injection",
    sources=["input", "request.get"],
    sanitizers=["escape_sql", "parameterize"],
    sinks=["execute_query"]
)

# Define an XSS pattern
xss_pattern = Pattern(
    name="XSS",
    sources=["input", "request.get"],
    sanitizers=["html_escape"],
    sinks=["render", "innerHTML"]
)

# Create a MultiLabel to track both patterns
multi = MultiLabel([sql_pattern, xss_pattern])

# Add a source (affects both patterns since both have "input" as a source)
multi.add_source("input")

# Add sanitizers (each affects only its corresponding pattern)
multi.add_sanitizer("escape_sql")  # Only affects SQL Injection
multi.add_sanitizer("html_escape") # Only affects XSS

# Get label for specific pattern
sql_label = multi.get_label("SQL Injection")
print(sql_label.get_sources())  # {'input'}
print(sql_label.get_all_sanitizers())  # {'escape_sql'}
```

## Design Decisions

1. **Label Refinement:** The label structure uses a dictionary mapping sources to sets of sanitizers, allowing distinction between different flows from the same source.

2. **Immutability of Combined Labels:** The `combine()` methods create new independent labels to ensure that modifications to one label don't affect others.

3. **Pattern-Specific Tracking:** MultiLabel ensures sources and sanitizers are only added to relevant patterns, preventing false associations.

4. **Set-Based Storage:** Using sets for sources, sanitizers, and sinks ensures uniqueness and efficient membership testing.

## Testing

Run the tool with:

```bash
python tool.py
```

This will execute the test cases demonstrating all functionality.
