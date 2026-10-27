# Subscriptions dashboard capture

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
      url: https://shorelane-data.github.io/shorelane/subscriptions/
    expect: Subscriptions Dashboard and visible Plotly figures
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

Read chart titles from `.chart-card`; scope to visible panels. Capture Last 12 Months resolved dates and freshness independently. Subscriber stock and ACV use window end, starts use term start, renewal/churn use ending-term decisions. Chart grandfathered share may be absent in the visible layout: do not invent a displayed tile. Calendar-quarter churn buckets may be clipped by selected window. ACV per seat is a whole-window ratio of sums, never average monthly ratios. DOM currency/percentage tiles are rounded; embedded Plotly arrays retain exact available precision.

Human-selected mapping: monthly Renewals bars use renewal term starts; renewal rate uses decided predecessor term endings. Reconcile each against its own cohort; different totals at window boundaries are expected.
