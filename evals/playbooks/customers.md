# Customers dashboard capture

Simulation test artifact. Recipe only; values belong in local captures.
Use the existing local Chrome MCP. Read active period/channel buttons, visible period text and page freshness stamp. Restrict plots and tiles to offsetParent !== null. Identity widgets describe a snapshot and must not be assumed to inherit order-period filters.

```yaml
replay:
  tool: plotly-static
  completion_condition:
    selector_visible: .js-plotly-plot
  steps:
  - step: 1
    action: navigate
    args:
      url: https://shorelane-data.github.io/shorelane/customers/
    expect: Customers dashboard with visible Plotly charts
  - step: 2
    action: evaluate-js
    args:
      script: "() => ({active: [...document.querySelectorAll('button.active')].map(b => b.innerText), text: document.body.innerText})"
    expect: Active period and channel, resolved window and freshness stamp
  - step: 3
    action: evaluate-js
    args:
      script_ref: plotly.md#decode
      selector: .js-plotly-plot
      visibility: offsetParent !== null
    expect: Decode x, y and values arrays for each visible trace; tag tier 1.5
  - step: 4
    action: evaluate-js
    args:
      script: "() => [...document.querySelectorAll('.kpi-value')].filter(p => p.offsetParent !== null).map(p => ({display:p.innerText, text:p.parentElement.innerText}))"
    expect: Exact integer DOM tiles and display-rounded ratios tagged tier 2
```
Do not turn rounded percentages into exact rates. The historical hygiene defect is repaired for the tested customer totals. Verify current eligibility and window rather than assuming all measures and slices were repaired. If selectors or window evidence change, stop replay and recapture state before comparing.
