"""
Security Vulnerability Detection Tool
Tracks information flows from sources to sinks through sanitizers
"""

class Pattern:
    """
    Represents a vulnerability pattern with sources, sanitizers, and sinks.
    """
    
    def __init__(self, name, sources, sanitizers, sinks):
        """
        Constructor for a Pattern object.
        
        Args:
            name (str): The name of the vulnerability pattern
            sources (list): List of source function/variable names
            sanitizers (list): List of sanitizer function names
            sinks (list): List of sink function/variable names
        """
        self._name = name
        self._sources = set(sources) if sources else set()
        self._sanitizers = set(sanitizers) if sanitizers else set()
        self._sinks = set(sinks) if sinks else set()
    
    # Selectors
    def get_name(self):
        """Returns the vulnerability pattern name."""
        return self._name
    
    def get_sources(self):
        """Returns the set of source names."""
        return self._sources.copy()
    
    def get_sanitizers(self):
        """Returns the set of sanitizer names."""
        return self._sanitizers.copy()
    
    def get_sinks(self):
        """Returns the set of sink names."""
        return self._sinks.copy()
    
    # Tests
    def is_source(self, name):
        """
        Check if a given name is a source for this pattern.
        
        Args:
            name (str): The name to check
            
        Returns:
            bool: True if name is a source, False otherwise
        """
        return name in self._sources
    
    def is_sanitizer(self, name):
        """
        Check if a given name is a sanitizer for this pattern.
        
        Args:
            name (str): The name to check
            
        Returns:
            bool: True if name is a sanitizer, False otherwise
        """
        return name in self._sanitizers
    
    def is_sink(self, name):
        """
        Check if a given name is a sink for this pattern.
        
        Args:
            name (str): The name to check
            
        Returns:
            bool: True if name is a sink, False otherwise
        """
        return name in self._sinks
    
    def __repr__(self):
        return f"Pattern(name={self._name}, sources={self._sources}, sanitizers={self._sanitizers}, sinks={self._sinks})"


class Label:
    """
    Represents the integrity label of information in a resource.
    Tracks sources that influenced the information and sanitizers that intercepted flows.
    
    Label structure: A dictionary mapping each source to a set of sanitizers that have
    processed the flow from that source. This allows tracking different flows from the
    same source independently.
    
    Example: {source1: {san1, san2}, source2: {san1}}
    This means information from source1 was sanitized by san1 and san2,
    while information from source2 was only sanitized by san1.
    """
    
    def __init__(self, source_flows=None):
        """
        Constructor for a Label object.
        
        Args:
            source_flows (dict): Dictionary mapping sources to sets of sanitizers.
                                If None, creates an empty label.
        """
        if source_flows is None:
            self._source_flows = {}
        else:
            # Deep copy to ensure independence
            self._source_flows = {
                source: sanitizers.copy() 
                for source, sanitizers in source_flows.items()
            }
    
    def add_source(self, source):
        """
        Add a source to the label (without any sanitizers initially).
        
        Args:
            source (str): The source name to add
        """
        if source not in self._source_flows:
            self._source_flows[source] = set()
    
    def add_sanitizer(self, sanitizer):
        """
        Add a sanitizer that intercepts flows from all current sources.
        
        Args:
            sanitizer (str): The sanitizer name to add
        """
        for source in self._source_flows:
            self._source_flows[source].add(sanitizer)
    
    def add_sanitizer_for_source(self, source, sanitizer):
        """
        Add a sanitizer for a specific source flow.
        
        Args:
            source (str): The source name
            sanitizer (str): The sanitizer name to add for this source
        """
        if source in self._source_flows:
            self._source_flows[source].add(sanitizer)
    
    # Selectors
    def get_sources(self):
        """
        Returns the set of all sources in this label.
        
        Returns:
            set: Set of source names
        """
        return set(self._source_flows.keys())
    
    def get_sanitizers_for_source(self, source):
        """
        Returns the set of sanitizers for a specific source.
        
        Args:
            source (str): The source name
            
        Returns:
            set: Set of sanitizer names for this source, or empty set if source not present
        """
        return self._source_flows.get(source, set()).copy()
    
    def get_all_sanitizers(self):
        """
        Returns the set of all sanitizers across all sources.
        
        Returns:
            set: Set of all sanitizer names
        """
        all_sanitizers = set()
        for sanitizers in self._source_flows.values():
            all_sanitizers.update(sanitizers)
        return all_sanitizers
    
    def get_source_flows(self):
        """
        Returns a copy of the complete source flows dictionary.
        
        Returns:
            dict: Dictionary mapping sources to sets of sanitizers
        """
        return {source: sanitizers.copy() for source, sanitizers in self._source_flows.items()}
    
    def is_empty(self):
        """
        Check if the label has no sources.
        
        Returns:
            bool: True if label has no sources, False otherwise
        """
        return len(self._source_flows) == 0
    
    # Combinor
    def combine(self, other):
        """
        Combine this label with another label to create a new independent label.
        The resulting label contains all sources from both labels with their respective sanitizers.
        
        Args:
            other (Label): Another Label object to combine with
            
        Returns:
            Label: A new Label object representing the combined information
        """
        # Create a new dictionary for the combined flows
        combined_flows = {}
        
        # Add all flows from self
        for source, sanitizers in self._source_flows.items():
            combined_flows[source] = sanitizers.copy()
        
        # Add all flows from other
        for source, sanitizers in other._source_flows.items():
            if source in combined_flows:
                # If source exists in both, union the sanitizers
                combined_flows[source] = combined_flows[source].union(sanitizers)
            else:
                combined_flows[source] = sanitizers.copy()
        
        # Return a new independent Label
        return Label(combined_flows)
    
    def __repr__(self):
        return f"Label({self._source_flows})"
    
    def __eq__(self, other):
        if not isinstance(other, Label):
            return False
        return self._source_flows == other._source_flows


class MultiLabel:
    """
    Represents multiple labels for tracking different vulnerability patterns simultaneously.
    Each pattern has its own associated label.
    """
    
    def __init__(self, patterns=None):
        """
        Constructor for a MultiLabel object.
        
        Args:
            patterns (list): List of Pattern objects to track.
                           If None, creates an empty MultiLabel.
        """
        self._patterns = {}  # Maps pattern name to Pattern object
        self._labels = {}    # Maps pattern name to Label object
        
        if patterns:
            for pattern in patterns:
                self._patterns[pattern.get_name()] = pattern
                self._labels[pattern.get_name()] = Label()
    
    def add_pattern(self, pattern):
        """
        Add a new pattern to track.
        
        Args:
            pattern (Pattern): The Pattern object to add
        """
        pattern_name = pattern.get_name()
        if pattern_name not in self._patterns:
            self._patterns[pattern_name] = pattern
            self._labels[pattern_name] = Label()
    
    def add_source(self, source_name):
        """
        Add a source to all patterns for which this name is a source.
        
        Args:
            source_name (str): The source name to add
        """
        for pattern_name, pattern in self._patterns.items():
            if pattern.is_source(source_name):
                self._labels[pattern_name].add_source(source_name)
    
    def add_sanitizer(self, sanitizer_name):
        """
        Add a sanitizer to all patterns for which this name is a sanitizer.
        The sanitizer is applied to all current sources in those patterns.
        
        Args:
            sanitizer_name (str): The sanitizer name to add
        """
        for pattern_name, pattern in self._patterns.items():
            if pattern.is_sanitizer(sanitizer_name):
                self._labels[pattern_name].add_sanitizer(sanitizer_name)
    
    # Selectors
    def get_patterns(self):
        """
        Returns the list of all pattern names being tracked.
        
        Returns:
            list: List of pattern names
        """
        return list(self._patterns.keys())
    
    def get_pattern(self, pattern_name):
        """
        Returns a specific Pattern object.
        
        Args:
            pattern_name (str): The name of the pattern
            
        Returns:
            Pattern: The Pattern object, or None if not found
        """
        return self._patterns.get(pattern_name)
    
    def get_label(self, pattern_name):
        """
        Returns the label for a specific pattern.
        
        Args:
            pattern_name (str): The name of the pattern
            
        Returns:
            Label: The Label object for this pattern, or None if pattern not found
        """
        return self._labels.get(pattern_name)
    
    def get_all_labels(self):
        """
        Returns a copy of all labels.
        
        Returns:
            dict: Dictionary mapping pattern names to Label objects
        """
        return self._labels.copy()
    
    # Combinor
    def combine(self, other):
        """
        Combine this MultiLabel with another MultiLabel.
        For each pattern present in both, combine their labels.
        
        Args:
            other (MultiLabel): Another MultiLabel object to combine with
            
        Returns:
            MultiLabel: A new independent MultiLabel object
        """
        # Create a new MultiLabel with all patterns from both
        combined = MultiLabel()
        
        # Add all patterns from self
        for pattern_name, pattern in self._patterns.items():
            combined._patterns[pattern_name] = pattern
            combined._labels[pattern_name] = Label(self._labels[pattern_name].get_source_flows())
        
        # Combine or add patterns from other
        for pattern_name, pattern in other._patterns.items():
            if pattern_name in combined._patterns:
                # Pattern exists in both - combine the labels
                combined._labels[pattern_name] = combined._labels[pattern_name].combine(
                    other._labels[pattern_name]
                )
            else:
                # Pattern only in other - add it
                combined._patterns[pattern_name] = pattern
                combined._labels[pattern_name] = Label(other._labels[pattern_name].get_source_flows())
        
        return combined
    
    def __repr__(self):
        result = "MultiLabel(\n"
        for pattern_name in self._patterns:
            result += f"  {pattern_name}: {self._labels[pattern_name]}\n"
        result += ")"
        return result
    
    def __eq__(self, other):
        if not isinstance(other, MultiLabel):
            return False
        return (self._patterns.keys() == other._patterns.keys() and
                all(self._labels[name] == other._labels[name] 
                    for name in self._patterns.keys()))


# Example usage and testing
if __name__ == "__main__":
    print("=== Testing Pattern Class ===")
    sql_pattern = Pattern(
        name="SQL Injection",
        sources=["input", "request.get", "request.post"],
        sanitizers=["escape_sql", "parameterize"],
        sinks=["execute_query", "db.query"]
    )
    
    print(f"Pattern: {sql_pattern.get_name()}")
    print(f"Is 'input' a source? {sql_pattern.is_source('input')}")
    print(f"Is 'escape_sql' a sanitizer? {sql_pattern.is_sanitizer('escape_sql')}")
    print(f"Is 'execute_query' a sink? {sql_pattern.is_sink('execute_query')}")
    print(f"Is 'random_func' a source? {sql_pattern.is_source('random_func')}")
    print()
    
    print("=== Testing Label Class ===")
    label1 = Label()
    label1.add_source("input")
    label1.add_source("request.get")
    print(f"Label1 after adding sources: {label1}")
    
    label1.add_sanitizer("escape_sql")
    print(f"Label1 after adding sanitizer: {label1}")
    
    label2 = Label()
    label2.add_source("request.post")
    label2.add_sanitizer("parameterize")
    print(f"Label2: {label2}")
    
    combined = label1.combine(label2)
    print(f"Combined label: {combined}")
    print(f"Original label1 unchanged: {label1}")
    print(f"Sources in combined: {combined.get_sources()}")
    print()
    
    print("=== Testing MultiLabel Class ===")
    xss_pattern = Pattern(
        name="XSS",
        sources=["input", "request.get"],
        sanitizers=["html_escape", "sanitize_html"],
        sinks=["render", "innerHTML"]
    )
    
    multi = MultiLabel([sql_pattern, xss_pattern])
    print(f"MultiLabel patterns: {multi.get_patterns()}")
    
    multi.add_source("input")  # Adds to both patterns
    print(f"After adding 'input' source:\n{multi}")
    
    multi.add_sanitizer("escape_sql")  # Only adds to SQL pattern
    print(f"After adding 'escape_sql' sanitizer:\n{multi}")
    
    multi.add_sanitizer("html_escape")  # Only adds to XSS pattern
    print(f"After adding 'html_escape' sanitizer:\n{multi}")
    
    multi2 = MultiLabel([sql_pattern])
    multi2.add_source("request.post")
    multi2.add_sanitizer("parameterize")
    
    combined_multi = multi.combine(multi2)
    print(f"Combined MultiLabel:\n{combined_multi}")
