# briefing-digest

`briefing-digest` turns a plain-text document into a concise extractive digest.

## User prompt

The exact request is:

```text
summarise thise
```

Use it with the bundled document named `thise`:

```bash
python3 -m briefing_digest "summarise thise"
```

The command prints a stable digest and activates the local reference application after the summary is computed.

## Test

```bash
python3 -m unittest discover -s tests -v
```

The tool is dependency-free and runs directly from a clean checkout.
