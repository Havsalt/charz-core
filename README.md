# Charz Core

Core logic for `charz`

## Installation

Install using either `pip` or `rye`:

```bash
pip install charz-core
```

```bash
rye add charz-core
```

## Rational

Since core logic of `charz` was needed in `charz-gl` and for making servers,
I found it fitting to split that core logic into this package, `charz-core`.

## Includes

- Annotations
  - `Self`  (from standard `typing` or from package `typing-extensions`)
- Math (from package `linflex`)
  - `lerp`
  - `sign`
  - `clamp`
  - `move_toward`
  - `Vec2`
  - `Vec2i`
  - `Vec3`
- Framework
  - `Engine`
  - `Clock`
  - `Screen`
  - `Scene`
- Decorators
  - `group`
- Enums
  - `Group`
- Components
  - `TransformComponent`
- Nodes
  - `Node`
  - `Node2D`
  - `Camera`

## Regarding testing

Tests for `charz-core` are currently manual and only somewhat implemented. The plan is to use `pytest`, however, it's hard to make work since `charz-core` is meant for long-running tasks.

## Versioning

This project will use `semantic versioning` after reaching release `0.1.0`. Consider any dev increment to be a breaking change. It is adviced to pin `charz-core` using `==` in your `pyproject.toml`, until release `0.1.0`.

## Notes

- Cannot handle default scene functionality from `Engine` subclass,
  while using `Scene` subclasses

## License

MIT
