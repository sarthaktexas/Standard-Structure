![Vue](https://img.shields.io/static/v1?label=Framework&message=Vue&color=4FC08D&logo=vue.js&logoColor=white&style=for-the-badge)
## Basic Vue App

```
├── src/
│   ├── components/
│   ├── assets/
│   ├── main.js
│   └── App.vue
├── public/
│   └── index.html
└── package.json
```

### `src/components/`
Here, you store Vue components to be used elsewhere in your app.

### `src/assets/`
Store static assets here, like images.

### `src/App.vue`
The root Vue component.

### `src/main.js`
This is the entrypoint to your Vue app. Create your Vue instance here.

#### Example

```js
import Vue from 'vue'
import App from './App.vue'

new Vue({
  render: h => h(App)
}).$mount('#app')
```

### `public/`
You generally place `index.html` here.