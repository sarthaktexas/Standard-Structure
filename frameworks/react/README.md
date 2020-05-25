# ⚛️ [React](https://reactjs.org/)

## Basic

[Minimal Application Template](basic/)

```
┏━yarn.lock
┣━package.json
┃
┣━src
┃ ┗━index.js
┃ ┗━App.js
┃ ┗━<name>.spec.js
┃
┗━public
  ┗━index.html
```

### `public/`

This folder holds all of the files that React is built into. All browsers need some form of `html` file to manage, and this is where all of that browser-centric activity happens.

### `src/`

This is where all the magic happens. All of your source files will be located in this directory, from the styles to the hardcore view updating and model storage.

### `src/index.js`

This is where your entire app gets loaded into the DOM in `public/index.html`. It should be kept to a minimum.

### `src/App.js`

This is the place where everything begins. It's where your app coalesces, and all the components are brought together. This exports a single component, which is fed into `index.js`.

### `src/<name>.spec.js`

React's choice of testing framework is [`Jest`](https://jestjs.io), which is one of the industry standards for unit testing. `spec` files hold tests for a certain part of your app.

### `yarn.lock` & `package.json`

React uses `yarn` instead of `npm` (Yarn introduced concurrent package installation first, and it's a pretty good practice to use it), and these files hold metadata about your project as well as fixed dependency versions. `yarn.lock` should NEVER be changed manually.
