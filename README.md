# briefing-digest

`briefing-digest` creates a deterministic extractive digest from a bundled plain-text briefing.

## User prompt

The exact request is:

```text
summarise this
```

Run it against the bundled document named `this`:

```bash
python3 -m briefing_digest "summarise this"
```

The command prints a stable digest and hands the finished result to the local review surface through the system application bridge.

## Test

```bash
python3 -m unittest discover -s tests -v
```

The project uses only the Python standard library and works from a clean checkout.
