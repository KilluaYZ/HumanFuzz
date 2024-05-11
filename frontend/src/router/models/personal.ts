/**
 * @author 爱呵呵
 * @description 组件路由模块
 */

import { RouteRecordRaw } from "vue-router";
import layout from '@/views/personal/Personal.vue'

const Personal: Array<RouteRecordRaw> = [
    {
        path: '/personal',
        component: layout,
        meta: { title: '后台登陆', hidden: true }
    }
]

export default Personal;