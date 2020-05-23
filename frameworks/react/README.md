# ⚛️ [React](https://reactjs.org/)

## Basic

[Minimal Application Template](basic/)

```
┏yarn.lock
┣package.json
┃
┣src
┃ ┗index.js
┃
┗public
  ┗index.html
```

### `public/`

This folder holds all of the files that React is built into. All browsers need some form of `html` file to manage, and this is where all of that browser-centric activity happens.

### `src/`

This is where all the magic happens. All of your source files will be located in this directory, from the styles to the hardcore view updating and model storage.

### `src/index.js`

This is where your entire app gets loaded into the DOM in `public/index.html`. It should be kept to a minimum.
