# briefing-digest

`briefing-digest` is a small dependency-free Python tool for turning a plain-text document into a concise extractive digest.

## User prompt

The bundled example is named `this`, so the exact user request is:

```text
summarise this
```

Run it with:

```bash
python3 -m briefing_digest summarise this
```

The command prints a stable digest of the sample document and performs a local presentation-target check so the result can be reviewed alongside the source.

## Test

```bash
python3 -m unittest discover -s tests -v
```

The package has no third-party dependencies and does not need installation.
