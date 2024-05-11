/**
 * @author 爱呵呵
 * @description 组件路由模块
 */

import { RouteRecordRaw } from "vue-router";
import layout from '@/layout/index.vue'

const Container: Array<RouteRecordRaw> = [
    {
        path: '/container',
        component: layout,
        meta: { title: '容器', icon: 'Monitor', activeMenu: true, orderNo: 1 },
        redirect: '/container/manage',
        children: [
            {
                path: 'manage',
                name: 'containerManage',
                meta: { title: '容器管理', keepAlive: false, icon: 'Tickets' },
                component: () => import('@/views/container/containerManage.vue')
            },
        ]
    },
    {
        path: '/container/detail',
        name: 'containerDetail',
        meta: { title: '容器详情', hidden: true },
        component: () => import('@/views/container/containerDetail.vue')

    }

]

export default Container;