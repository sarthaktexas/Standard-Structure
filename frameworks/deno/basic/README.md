![Deno](https://img.shields.io/static/v1?label=Framework&message=Deno&color=black&logo=deno&logoColor=white&style=for-the-badge)
## Basic Package Structure

```
├── mod.ts
│
└── deps.ts
```

### `mod.ts`

This file is the entrypoint to your package. Here, you can import classes and functions from other files, or you can write the program entirely in `mod.ts`.

#### Examples
```ts
export * from "addition.ts";
export * from "subtraction.ts";
```
\- or -
```ts
export function add(one: number, two: number){
    return one + two;
}
```

### `deps.ts`

You can optionally save your external dependencies in a `deps.ts` file.

#### Example
```ts
export * from "https://deno.land/std/http/mod.ts";
export * from "https://deno.land/x/oak/mod.ts";
```
Then, import your dependencies elsewhere:
```ts
import { serve, Application } from "./deps.ts";
```