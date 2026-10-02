# Marketing dashboard capture

Simulation test artifact. Recipe only; values stay in local captures. Use the existing local Chrome MCP, never remote browser services. If the selected tab is closed, open the named dashboard in a new local tab.

```yaml
replay:
  tool: plotly-static
  completion_condition:
    selector_visible: .js-plotly-plot
  steps:
  - step: 1
    action: navigate
    args:
      url: https://shorelane-data.github.io/shorelane/marketing/
    expect: Marketing Dashboard and visible Plotly figures
  - step: 2
    action: evaluate-js
    args:
      script: "() => ({active:[...document.querySelectorAll('button.active')].map(b=>b.innerText),text:document.body.innerText})"
    expect: Active period, resolved window, freshness stamp and visible promotion table
  - step: 3
    action: evaluate-js
    args:
      script_ref: plotly.md#decode
      selector: .js-plotly-plot
      visibility: offsetParent !== null
    expect: Chart titles and decoded visible x/y/labels/values arrays tagged tier 1.5
  - step: 4
    action: evaluate-js
    args:
      script: "() => [...document.querySelectorAll('.kpi-value')].filter(p=>p.offsetParent!==null).map(p=>({display:p.innerText,text:p.parentElement.innerText}))"
    expect: Integer counts exact; currency and percentage tiles retain display precision, tier 2
```

Read chart titles from `.chart-card`; avoid generated plot IDs. Whole-period AOV and CAC are ratios of aggregate components, never sums or averages of monthly ratios. Distinguish all-channel headline GMV from consumer AOV. A promotions table with no rows in the active window does not establish that the source has no promotion history. Check warehouse date scope and eligibility before accepting a numeric match. Dashboard-only arithmetic is not independent verification.
