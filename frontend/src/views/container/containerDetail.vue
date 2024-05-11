<template>
    <el-row style="width: 100%; height: 100%; justify-content: space-around; align-items: center; padding: 30px 50px 30px 50px">
        <el-row class="card-eff" style="width: fit-content; height: fit-content; border-radius: 10px; background: #293c4b">
            <el-row style="margin: 20px" class="terminal">
                <div ref="xterm" class="xterm"></div>
            </el-row>
        </el-row>
        <el-row style="justify-content: center; align-items: center; flex-direction: column;">
            <el-row v-if="container_info" class="card-eff" style="border-radius: 10px; background: #ffffff;">
                <el-row style="margin: 10px 15px 10px 15px;">
                    <el-descriptions title="容器信息" :column="1" size="large">
                        <el-descriptions-item label="容器名">{{container_info.name}}</el-descriptions-item>
                        <el-descriptions-item label="容器id">{{container_info.container_id.substring(0,10)}}</el-descriptions-item>
                        <el-descriptions-item label="websocket">{{container_info.ws_host}}:{{container_info.ws_port}}</el-descriptions-item>
                        <el-descriptions-item label="ssh">{{container_info.ssh_host}}:{{container_info.ssh_port}}</el-descriptions-item>
                        <el-descriptions-item label="创建时间">{{container_info.create_time}}</el-descriptions-item>
                    </el-descriptions>
                </el-row>
            </el-row>
        </el-row>
    </el-row>
</template>

<script setup lang='ts'>
import { useRoute, useRouter } from 'vue-router'
import request from '@/utils/request'
import { onMounted, reactive, ref, toRef, computed } from 'vue'
import { ContainerType } from '@/types'
import {getContainer} from '@/api/container'
import 'xterm/css/xterm.css'
import 'xterm/lib/xterm.js'
import { Terminal } from 'xterm'
// xterm.js的插件，使终端的尺寸适合包含元素。
import { FitAddon } from 'xterm-addon-fit'
// xterm.js的附加组件，用于附加到Web Socket
import { AttachAddon } from 'xterm-addon-attach'

const router = useRouter()
const route = useRoute()
const container_id = route.query.container_id! as string

// console.log(`container_id = ${container_id}`) c
const container_info = ref<ContainerType>()
const xterm = ref()

const getContainerInfo = () => {
    return getContainer(container_id)
        .then((res) => {
            container_info.value = res.data
        })
}

const initTerm = (tHost: string) => {
    const term = new Terminal({
        fontSize: 14,
        cursorBlink: true, //光标闪烁
        theme: {
            foreground: '#FABD2F', //字体
            background: '#293c4b' //背景色
        }
    })
    const socket = new WebSocket(tHost)
    const attachAddon = new AttachAddon(socket)
    const fitAddon = new FitAddon()
    term.loadAddon(attachAddon)
    term.loadAddon(fitAddon)
    term.open(xterm.value)
    fitAddon.fit()
    term.focus()
}


onMounted(() => {
    getContainerInfo()
        .then(() => {
            initTerm(`ws://${container_info.value?.ws_host}:${container_info.value?.ws_port}/ws`)
        })
})

</script>

<style scoped lang='scss'>
.xterm {
    width: 700px;
    height: 500px;
    //height: 100%;
}

.card-eff{
    box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19)
}
</style>