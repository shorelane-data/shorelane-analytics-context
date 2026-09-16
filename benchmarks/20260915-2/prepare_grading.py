"""Audit both answer sets and produce condition-blinded grading inputs."""
from pathlib import Path
import json, random, re
ROOT = Path(__file__).resolve().parent
seeds = json.loads((ROOT / 'frozen-seeds.json').read_text())
ids = [s['case_id'] for s in seeds]
answers = {}
audit = {}
for condition in ('off', 'on'):
    payload = json.loads((ROOT / f'{condition}-answers.json').read_text())
    cases = payload['cases']
    seen = [c['case_id'] for c in cases]
    assert sorted(seen) == ids, (condition, 'Missing/duplicate/unexpected case IDs', seen)
    answers[condition] = {c['case_id']: c for c in cases}
    for seed in seeds:
        case = answers[condition][seed['case_id']]
        assert case['question'] == seed['seed']['question'], (condition, seed['case_id'], 'Question changed')
        assert isinstance(case['answer'], str) and case['answer'].strip()
        for q in case.get('sql', []):
            assert isinstance(q['executed'], bool)
            assert q.get('text'), (condition, seed['case_id'], 'Missing SQL')
            if q['executed']:
                assert 'result' in q, (condition, seed['case_id'], 'Missing execution result')
    executed = [c['case_id'] for c in cases if any(q['executed'] for q in c.get('sql', []))]
    unique_sql = {q['text'].strip() for c in cases for q in c.get('sql', []) if q['executed']}
    audit[condition] = {'answer_count': len(cases), 'cases_with_executed_sql': executed,
                        'unique_executed_sql_texts': len(unique_sql),
                        'conceptual_or_unexecuted_only': [c['case_id'] for c in cases if c['case_id'] not in executed],
                        'integrity_notes': payload.get('integrity_notes', [])}
# Fixed shuffle seed is reproducible, and not exposed to the judge.
rng = random.Random(202609152)
mapping = {}
blinded = []
for seed in seeds:
    case_id = seed['case_id']
    modes = ['off', 'on']
    rng.shuffle(modes)
    mapping[case_id] = dict(zip(['A', 'B'], modes))
    candidates = {}
    for label, mode in mapping[case_id].items():
        src = answers[mode][case_id]
        candidates[label] = {k: src[k] for k in ['answer', 'sql', 'assumptions', 'tables', 'clarification_needed', 'limitations'] if k in src}
    blinded.append({'case_id': case_id, 'question': seed['seed']['question'],
                    'expected': seed['seed']['expected'], 'candidates': candidates})
(ROOT / 'blind-mapping.json').write_text(json.dumps(mapping, indent=2) + '\n')
(ROOT / 'grader-input.json').write_text(json.dumps({'simulation_only': True, 'shared_evaluation_context': {'as_of_date': '2026-09-15', 'note': 'Both original answer artifacts declare this as_of_date at top level; applies to every case.'}, 'cases': blinded}, indent=2) + '\n')
(ROOT / 'answer-audit.json').write_text(json.dumps(audit, indent=2) + '\n')
print(json.dumps(audit, indent=2))
