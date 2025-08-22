"""
Rules module - contains example medical rules for demo purposes.
You can edit or replace these with your own.
"""

# Example rules (replace/add as needed)
RULES = [
    {
        'name': 'influenza_rule',
        'if': ['fever', 'cough', 'fatigue'],
        'then': 'Influenza (flu)',
        'confidence': 0.8
    },
    {
        'name': 'common_cold_rule',
        'if': ['cough', 'sneezing'],
        'then': 'Common Cold',
        'confidence': 0.5
    },
    {
        'name': 'migraine_rule',
        'if': ['headache', 'nausea'],
        'then': 'Migraine',
        'confidence': 0.7
    },
]

def forward_chain(facts):
    """
    Simple forward chaining: checks all rules whose 'if' set is
    fully contained in the provided facts.
    """
    facts_set = set(facts)
    inferred = []
    for rule in RULES:
        required = set(rule.get('if', []))
        if required.issubset(facts_set):
            inferred.append({
                'diagnosis': rule.get('then'),
                'rule_name': rule.get('name'),
                'confidence': rule.get('confidence', 0.0),
                'matched_symptoms': list(required),
            })
    return inferred

def backward_chain_wizard(goal, facts):
    """
    Simple backward chaining wizard:
    Checks if the goal diagnosis can be supported by the provided facts.
    Returns (is_supported, info_dict).
    """
    facts_set = set(facts)
    for rule in RULES:
        if rule.get('then', '').lower() == (goal or '').lower():
            required = set(rule.get('if', []))
            missing = sorted(list(required - facts_set))
            info = {
                'rule_name': rule.get('name'),
                'required': sorted(list(required)),
                'missing': missing,
                'confidence': rule.get('confidence', 0.0)
            }
            return required.issubset(facts_set), info
    return False, None
