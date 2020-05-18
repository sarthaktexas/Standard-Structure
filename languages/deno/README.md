# 🦕 [Deno](https://deno.land)

Deno has no required package structure, but the following structure is used by Deno's standard library and is recommend in the Deno manual.

**You can view a full Deno package example [here](example/).**

## Files

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

You can optionally import your external dependencies in a `deps.ts` file

#### Example
```ts
export * from "https://deno.land/std/http/mod.ts";
export * from "https://deno.land/x/oak/mod.ts";
```
Then, import your dependencies:
```ts
import { serve, Application } from "./deps.ts";
```