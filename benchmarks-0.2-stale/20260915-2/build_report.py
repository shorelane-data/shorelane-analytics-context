"""Summarize frozen, blinded all-seed evaluation without modifying authored context."""
from pathlib import Path
from collections import Counter
import json, hashlib, datetime
ROOT=Path(__file__).resolve().parent
REPO=ROOT.parents[2]
OUT=REPO/'evals/captures/20260915-2'
seeds=json.loads((ROOT/'frozen-seeds.json').read_text())
mapping=json.loads((ROOT/'blind-mapping.json').read_text())
grades=json.loads((ROOT/'grades-blinded.json').read_text())['grades']
assert sorted(g['case_id'] for g in grades)==[s['case_id'] for s in seeds], 'Missing or duplicated grades'
byid={g['case_id']:g for g in grades}
rows=[]
for s in seeds:
    cid=s['case_id'];g=byid[cid]
    out={'case_id':cid,'seed_file':s['seed_file'],'question':s['seed']['question'],'domain':s['seed']['domain']}
    for label, mode in mapping[cid].items():
        judgment=g['candidates'][label]
        assert judgment['status'] in ['pass','fail'], (cid,label,judgment)
        out[mode]=judgment
    rows.append(out)
n=len(rows);off=sum(r['off']['status']=='pass' for r in rows);on=sum(r['on']['status']=='pass' for r in rows)
domains={}
for d in sorted({r['domain'] for r in rows}):
    rs=[r for r in rows if r['domain']==d]
    domains[d]={'seeds':len(rs),'off_pass':sum(r['off']['status']=='pass' for r in rs),'on_pass':sum(r['on']['status']=='pass' for r in rs)}
manifest=json.loads((ROOT/'manifest.json').read_text())
changed=[s['seed_file'] for s in seeds if hashlib.sha256((REPO/s['seed_file']).read_bytes()).hexdigest()!=s['sha256']]
changed_context=[p for p,h in manifest['source_hashes'].items() if hashlib.sha256((REPO/p).read_bytes()).hexdigest()!=h]
assert not changed and not changed_context, ('Inputs changed',changed,changed_context)
assert hashlib.sha256((REPO/'.codex/config.toml').read_bytes()).hexdigest()==manifest['config_sha256'],'Config changed'
audit=json.loads((ROOT/'answer-audit.json').read_text())
summary={'label':'20260915-2','simulation_only':True,'completed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'seeds_evaluated':n,'answers_evaluated':2*n,'skipped':0,'off_pass':off,'on_pass':on,'off_percent':100*off/n,'on_percent':100*on/n,'delta_percentage_points':100*(on-off)/n,'improvements':[r['case_id'] for r in rows if r['off']['status']=='fail' and r['on']['status']=='pass'],'regressions':[r['case_id'] for r in rows if r['off']['status']=='pass' and r['on']['status']=='fail'],'both_fail':[r['case_id'] for r in rows if r['off']['status']=='fail' and r['on']['status']=='fail'],'by_domain':domains,'input_hashes_unchanged':True,'rows':rows}
(OUT/'results.json').write_text(json.dumps(summary,indent=2)+'\n')
lines=['# All-seed context evaluation — 20260915-2','','Simulation benchmark against the frozen draft seed requirements; not a human-certified accuracy score.','',f'**Coverage:** {n}/{n} seeds, {2*n}/{2*n} answers graded, zero skipped. One answering agent per condition, one sample per seed.','', '| Condition | Passed | Pass rate |','|---|---:|---:|',f'| Context off | {off}/{n} | {100*off/n:.1f}% |',f'| Context on | {on}/{n} | {100*on/n:.1f}% |','',f'**Delta: {100*(on-off)/n:+.1f} percentage points** ({on-off:+d} passed seeds).','', '## By domain','','| Domain | Seeds | Off passed | On passed |','|---|---:|---:|---:|']
for d,v in domains.items():lines.append(f"| {d} | {v['seeds']} | {v['off_pass']} | {v['on_pass']} |")
lines+=['','## What changed','',f"- Improved: {', '.join(summary['improvements']) or 'none'}.",f"- Regressed: {', '.join(summary['regressions']) or 'none'}.",f"- Failed both: {', '.join(summary['both_fail']) or 'none'}.",'','## Every seed','','| ID | Seed | Off | On | Grader explanation |','|---|---|---|---|---|']
def clean(x):return str(x).replace('|','/').replace('\n',' ')
for r in rows:
    why='On: '+r['on'].get('reason','')
    if r['off']['status']!=r['on']['status'] or r['off']['status']=='fail':why='Off: '+r['off'].get('reason','')+' '+why
    slug=Path(r['seed_file']).name.replace('.seed.yaml','')
    lines.append(f"| {r['case_id']} | {slug} | {r['off']['status']} | {r['on']['status']} | {clean(why)} |")
lines+=['','## Method and practical limits','','- Questions and seed expectations were frozen before the run; neither answering agent saw seeds, intent, IR or expected answers. Context-on received only the authored company/domain/entity context snapshot; context-off used warehouse evidence.','- A separate grader saw A/B candidates shuffled independently per seed, with no condition mapping. Grading tests semantic compliance, not keyword matching or dashboard-number equality. Correct governed marts count as encapsulating their filters.','- All seeds are `sql_shape`. Numeric requests used live read-only BigQuery SQL; conceptual questions were graded on their rule/query reasoning. No fresh dashboard capture or numeric answer key was required.',f"- SQL execution coverage: off {len(audit['off']['cases_with_executed_sql'])}/{n} cases; on {len(audit['on']['cases_with_executed_sql'])}/{n} cases. Some cases reuse an executed query, disclosed in traces. All 23 cases remain independently scored against their own rubric.",'- Date anchor was 2026-09-15 for both conditions. Relative-period interpretation was part of each answer. Results are current-table observations, not immutable warehouse time-travel snapshots.','- One batch per condition allows within-batch carryover. Duplicate/overlapping questions reduce independence. This single run supports no significance or generalization claim.','- The context and seeds came from the same simulated interview, and some expected fields are broader than their questions. Rubric caveats below identify these weaknesses.','- Warehouse metadata incidentally exposed view definitions: off saw int_customer_identity/stg_invoices; on saw stg_refunds/stg_revenue_recognition. Detailed reliance notes are in the answer artifacts. Neither condition read dbt source or the analyst brief.','- Authored context, all seed files and `.codex/config.toml` hashes are unchanged. No commits or pushes.','', '## Rubric caveats','']
caveats=[]
for r in rows:
    for mode in ['off','on']:
        for note in r[mode].get('rubric_caveats',[]):
            text=f"{r['case_id']}: {note}"
            if text not in caveats:caveats.append(text)
lines+=['- '+c for c in caveats] or ['- None flagged by the grader.']
lines+=['','## Artifacts','','- [Machine-readable results](results.json)', '- [Illustrative answer differences](answer-differences.json)', '- [Grading input audit](../../runs/20260915-2/grading-audit.md)','- [Frozen run manifest](../../runs/20260915-2/manifest.json)','- [Context-off answers and exact SQL](../../runs/20260915-2/off-answers.json)','- [Context-on answers and exact SQL](../../runs/20260915-2/on-answers.json)','- [Blinded grades](../../runs/20260915-2/grades-blinded.json)','- [Grading policy](../../runs/20260915-2/grading-policy.md)','']
(OUT/'report.md').write_text('\n'.join(lines))
print(json.dumps({k:v for k,v in summary.items() if k!='rows'},indent=2))
