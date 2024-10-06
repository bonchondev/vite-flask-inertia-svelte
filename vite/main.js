//@ts-ignore
import { createInertiaApp } from "@inertiajs/svelte";
import Layout from "./src/layouts/Layout.svelte";
import "./app.css";

createInertiaApp({
  //@ts-ignore
  resolve: (name) => {
    const allPages = import.meta.glob('./src/**/*.svelte', { eager: true })
    const page = allPages[`./src/pages/${name}.svelte`];
    const layout = page.layout
      ? (Array.isArray(page.layout) ? [Layout, ...page.layout] : [Layout, page.layout])
      : [Layout]
    return { default: page.default, layout: page.layout || layout }
  },

  //@ts-ignore
  setup({ el, App, props }) {
    new App({ target: el, props });
  },
});
