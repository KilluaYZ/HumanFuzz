<template>
    <el-card shadow='hover' style='width: fit-content; min-width: 30%; max-width: 60%; margin: 10px'>
        <template #header>
           <el-row justify='space-between' align='middle' style='width: 100%;  align-items: center'>
               <el-col span=20>
                   <el-row align='middle'>
                       <span style='font-size: 24px;margin-right: 10px'>{{name}}</span>
                       <el-tag v-if='stage==="stop"' type='info'>未运行</el-tag>
                       <el-tag v-else-if='stage==="exited"' type='info' >已结束</el-tag>
                       <el-tag v-else-if='stage==="running"' type='success' >正在运行</el-tag>
                       <el-tag v-else type='info'>未知状态</el-tag>
                   </el-row>
               </el-col>
               <el-col span=20>
                   <el-button type='primary' :disabled="stage !== 'running'" round @click='onClickEnterProjectBtn'>进入</el-button>
                   <el-button v-if="stage === 'running'" :icon="VideoPause" circle type="danger" @click="onClickStopContainer"></el-button>
                   <el-button v-else :icon="VideoPlay" circle type="success"  @click="onClickStartContainer"></el-button>
               </el-col>
           </el-row>
        </template>
        <el-row style='width: 100%'>
            <el-row style="flex-direction: column">
                <el-statistic group-separator="" title="ssh端口号" :value="ssh_port" />
                <el-statistic group-separator="" title="ws端口号" :value="ws_port" />
                <el-statistic title="id" :value="id.substring(0,10)" />
                <el-statistic title="容器id" :value="container_id.substring(0,10)" />
            </el-row>
        </el-row>
        <el-divider />
        <el-row style='width: 100%;' justify='space-between' align='middle'>
            <el-col span=20>
                <el-row>
                    <el-popover :visible="visible" placement="top" :width="160">
                        <p style='color: orangered;'>你确定要删除该容器吗？</p>
                        <div style="text-align: right; margin: 0">
                            <el-button size="small" text @click="visible = false">取消</el-button>
                            <el-button size="small" type="primary" @click="deleteFunc(container_id);visible = false">确定</el-button>
                        </div>
                        <template #reference>
                            <el-button @click='visible = true;' :disabled="!(stage == 'stop' || stage == 'exited')" style='margin: 5px; margin-right: 10px;' circle :icon='Delete' type='danger'></el-button>
                        </template>
                    </el-popover>
                    <el-text>{{create_time}}</el-text>
                </el-row>
            </el-col>
        </el-row>
    </el-card>
</template>

<script setup lang='ts'>
import { ref, defineProps } from 'vue';
import { Delete, CaretRight, VideoPause, VideoPlay } from '@element-plus/icons-vue'
import router from '@/router'
const visible = ref(false)
import { runContainer, startContainer, stopContainer } from '@/api/container'
import { ElLoading, ElMessage } from 'element-plus'
import { start } from 'nprogress'

const props = defineProps({
    id: {
      required: true,
      type: String
    },
    name: {
        required: true,
        type: String
    },
    stage:{
        required: false,
        type: String,
        default: 'unknown'
    },
    create_time:{
        required: false,
        type: String,
        default: ''
    },
    deleteFunc:{
        required: true,
        type: Function
    },
    container_id:{
        required: true,
        type: String,
        default: ''
    },
    ssh_port:{
        required: true,
        type: Number,
        default: 0
    },
    ws_port:{
        required: true,
        type: Number,
        default: 0
    },
})

const onClickEnterProjectBtn = () => {
    let routeUrl = router.resolve({
        path:"/container/detail",
        query: {container_id: props.container_id}
    });
    window.open(routeUrl.href, '_blank')
}

const onClickStartContainer = () => {
    const tLoading = ElLoading.service({
        lock: true,
        text: '正在启动容器',
        background: 'rgba(0, 0, 0, 0.7)'
    });

    startContainer(props.container_id)
        .then((res) => {
            ElMessage({
                type: 'success',
                message: res.msg
            })
            tLoading.close()
            window.location.reload()
        })
        .catch(() => {
            tLoading.close()
        })
}

const onClickStopContainer = () => {
    const tLoading = ElLoading.service({
        lock: true,
        text: '正在停止容器',
        background: 'rgba(0, 0, 0, 0.7)'
    });

    stopContainer(props.container_id)
        .then((res) => {
            ElMessage({
                type: 'success',
                message: res.msg
            })
            tLoading.close()
            window.location.reload()
        })
        .catch(() => {
            tLoading.close()
        })
}
</script>

<style scoped>

</style>