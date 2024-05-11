import { createApp } from 'vue'
import App from './App.vue'

import ElementPlus from 'element-plus'
import './style.css'
import 'element-plus/dist/index.css'
import zhCn from 'element-plus/es/locale/lang/zh-cn'
import * as ElementPlusIconsVue from '@element-plus/icons-vue'
import router from './router'
import { createPinia } from 'pinia'
import 'highlight.js/styles/stackoverflow-light.css'
import 'highlight.js/lib/common'
import hljsVuePlugin from '@highlightjs/vue-plugin'
import '@/styles/global.scss'
import { Splitpanes, Pane } from 'splitpanes'
import 'splitpanes/dist/splitpanes.css'

import VueVirtualScroller from 'vue-virtual-scroller'
import 'vue-virtual-scroller/dist/vue-virtual-scroller.css'

import VMdPreview from '@kangc/v-md-editor/lib/preview';
import '@kangc/v-md-editor/lib/style/preview.css';
import githubTheme from '@kangc/v-md-editor/lib/theme/github.js';
import '@kangc/v-md-editor/lib/theme/style/github.css';
// highlightjs
import hljs from 'highlight.js';
VMdPreview.use(githubTheme, {
	Hljs: hljs,
});

const pinia = createPinia()
const app = createApp(App)

for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
	app.component(key, component)
}
app.component("splitpanes", Splitpanes);
app.component("pane", Pane);
// app.component("vue-markdown", VueMarkdown);
// app.component("split-pane", splitPane)
app.use(router)
	.use(pinia)
	.use(ElementPlus, { locale: zhCn })
	.use(hljsVuePlugin)
	.use(VueVirtualScroller)
	.use(VMdPreview)
	.mount('#app')
