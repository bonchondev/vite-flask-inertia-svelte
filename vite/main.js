//@ts-ignore
import { createInertiaApp } from '@inertiajs/svelte'
import "./app.css"

function importPageComponent(name, pages) {
  // eslint-disable-next-line no-restricted-syntax
  for (const path in pages) {
    if (path.endsWith(`${name.replaceAll(".", "/")}.svelte`)) {
      return typeof pages[path] === "function" ? pages[path]() : pages[path];
    }
  }

  throw new Error(`Page not found: ${name}`);
}

createInertiaApp({
  //@ts-ignore
  resolve: (name) =>
    importPageComponent(name, import.meta.glob("./src/**/*.svelte")),
  //@ts-ignore
  setup({ el, App, props }) {
    new App({ target: el, props })
  },
})