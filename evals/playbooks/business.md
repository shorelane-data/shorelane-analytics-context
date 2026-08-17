# Learned playbook — Shorelane executive dashboard ("business")

Static Plotly page on GitHub Pages (shipped playbook: `plotly-static`, Variant C).
Learned live 2026-08-17.

- Public page, no login. Freshness stamp "as of YYYY-MM-DD" in the header block
  (body text), not a footer.
- Four pre-rendered period panels co-exist in the DOM (Last 6 / 12 / 24 Months,
  All Time; buttons `button.pbtn`, active = `.pbtn.active`, default **Last 12
  Months**). Every panel repeats the same six widgets — scope reads to the
  visible panel (`offsetParent !== null`) or tag values by panel.
- Widgets per panel: KPI row (`.kpi-card` → `.kpi-label`/`.kpi-value`/`.kpi-sub`/
  `.kpi-delta`; display-rounded) + five Plotly figures. Figure titles are NOT in
  `layout.title` — read the enclosing `.chart-card` heading: "Recognized Revenue
  by Month", "Revenue by Channel" (pie → `t.labels`/`t.values`), "Customer
  Growth", "Orders & Average Order Value", "Recognized Revenue vs Collected Cash".
- All traces SVG-rendered; figure arrays use plotly bdata encoding — use the
  decode helper (`plotly.md#decode`).
- Window anchors to data-end (last fully-elapsed month), not the as_of date.
- **GMV is never charted monthly.** Exact monthly GMV = orders × AOV from the
  "Orders & Average Order Value" figure (the KPI defines AOV = GMV ÷ orders).
  The GMV KPI tile is display-rounded.
- **No billed_revenue widget exists** on this page (despite older descriptions
  naming a "billed vs collected" view — drift noted 2026-08-17).

```yaml
replay:
  tool: plotly-static
  completion_condition:
    selector_visible: ".js-plotly-plot"
  steps:
    - step: 1
      action: navigate
      args: { url: "https://shorelane-data.github.io/shorelane/business/" }
      expect: "title 'Shorelane Commerce — Executive Dashboard'; completion condition met"
    - step: 2
      action: evaluate-js
      args: { script: "() => document.body.innerText.match(/as of[^\\n]*/i)?.[0]" }
      expect: "'as of YYYY-MM-DD' freshness stamp"
    - step: 3
      action: evaluate-js
      args: { script: "() => [...document.querySelectorAll('button.pbtn')].map(b => ({label: b.innerText.trim(), active: b.className.includes('active')}))" }
      expect: "4 period options; exactly one active (filter_state.period)"
    - step: 4
      action: evaluate-js
      args: { script_ref: "plotly.md#decode" }
      expect: "per visible .chart-card: heading + decoded traces (x dates, y values); pie uses labels/values"
    - step: 5
      action: evaluate-js
      args: { script: "() => [...document.querySelectorAll('.kpi-card')].filter(k => k.offsetParent !== null).map(k => k.innerText)" }
      expect: "6 KPI tiles (Revenue, GMV, Active Customers, New Customers, AOV, Refund Rate) — display precision"
  notes: "Read state, don't click: all period panels are already in the DOM."
```
