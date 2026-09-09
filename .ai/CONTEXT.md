# AI Context Route

```yaml
schema_version: 1
context_repo: https://github.com/madebycli/master-context
project_id: gt-app
source_repo: https://github.com/madebycli/gt-app
context_root: projects/gt-app/
entrypoint: projects/gt-app/INDEX.md
```

## Mandatory AI behavior

Use this exact route. Validate against `REGISTRY.yaml`, read the declared entrypoint first, do not scan sibling project folders, reconcile durable context with verified repository reality before declaring work complete, and archive reusable prompts/plans/handoffs under `prompts/gt-app/` when possible.
