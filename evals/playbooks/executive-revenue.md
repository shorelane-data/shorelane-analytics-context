# Executive Revenue dashboard capture

Simulation-run recipe; contains no captured values. The hosted static page renders all period panels. Scope reads to visible plots and tiles. Read the active period and freshness stamp before extracting. Plotly numeric arrays may use base64 `bdata`; decode using the full dtype map in the installed dashboard-verify Plotly playbook. Chart headings live in `.chart-card`; figures have `.js-plotly-plot`. Do not rely on generated plot UUIDs. KPI currency and rate displays remain rounded.

```yaml
replay:
  tool: plotly-static
  completion_condition:
    selector_visible: ".js-plotly-plot"
  steps:
    - step: 1
      action: navigate
      args:
        url: "https://shorelane-data.github.io/shorelane/business/"
      expect: "Executive Revenue Dashboard and Plotly figures visible"
    - step: 2
      action: evaluate-js
      args:
        function: "() => ({period:document.querySelector('button.pbtn.active')?.innerText,text:document.body.innerText})"
      expect: "Active period, resolved window and as-of stamp present"
    - step: 3
      action: capture-network
      args:
        resource_types: [xhr, fetch]
      expect: "Response bodies available, or static page with no data requests; use embedded figures next"
    - step: 4
      action: evaluate-js
      args:
        script_ref: "plotly.md#decode"
        scope: ".js-plotly-plot with offsetParent !== null"
      expect: "Decoded trace x/y or labels/values arrays under each chart-card heading"
    - step: 5
      action: query-dom
      args:
        selector: ".kpi-value"
        scope: "offsetParent !== null"
      expect: "Display values, labels and definitions from each tile parent"
```
