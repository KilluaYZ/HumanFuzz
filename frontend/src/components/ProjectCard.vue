<template>
    <el-card shadow='hover' style='width: fit-content; min-width: 30%; max-width: 60%; margin: 10px'>
        <template #header>
           <el-row justify='space-between' align='middle' style='width: 100%;  align-items: center'>
               <el-col span=20>
                   <el-row align='middle'>
                       <span style='font-size: 24px;margin-right: 10px'>{{name}}</span>
                       <el-tag v-if='stage==="stop"' type='info'>未运行</el-tag>
                       <el-tag v-else-if='stage==="error"' type='danger' >出现错误</el-tag>
                       <el-tag v-else-if='stage==="running"' type='success' >正在运行</el-tag>
                       <el-tag v-else type='info'>未知状态</el-tag>
                   </el-row>
               </el-col>
               <el-col span=20>
                   <el-button type='success'  round @click='onClickEnterProjectBtn'>进入</el-button>
               </el-col>
           </el-row>
        </template>
        <el-row style='width: 100%'>
            <el-row style="flex-direction: column">
                <el-statistic title="崩溃种子数" :value="crashNum" />
                <el-statistic title="当前种子数" :value="seedNum" />
                <el-statistic v-if="stage === 'running'" title="运行时间" :value="runTime" />
            </el-row>
        </el-row>
        <el-divider />
        <el-row style='width: 100%;' justify='space-between' align='middle'>
            <el-col span=20>
                <el-row>
                    <el-popover :visible="visible" placement="top" :width="160">
                        <p style='color: orangered;'>你确定要删除该项目吗？</p>
                        <div style="text-align: right; margin: 0">
                            <el-button size="small" text @click="visible = false">取消</el-button>
                            <el-button size="small" type="primary" @click="deleteFunc(id);visible = false">确定</el-button>
                        </div>
                        <template #reference>
                            <el-button @click='visible = true;' style='margin: 5px; margin-right: 10px;' circle :icon='Delete' type='danger'></el-button>
                        </template>
                    </el-popover>
                    <el-text>{{createTime}}</el-text>
                </el-row>
            </el-col>
        </el-row>
    </el-card>
</template>

<script setup lang='ts'>
import { ref, defineProps } from 'vue';
import { delProject } from '@/api/project'
import { Delete, CaretRight } from '@element-plus/icons-vue'
import router from '@/router'
import { ElMessage } from 'element-plus'
const visible = ref(false)
const submitBtnIsDisabled = ref(false)
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
    createTime:{
        required: false,
        type: String,
        default: ''
    },
    deleteFunc:{
        required: true,
        type: Function
    },
    crashNum:{
        required: false,
        type: Number,
        default: 0
    },
    seedNum:{
        required: false,
        type: Number,
        default: 0
    },
})

const runTime = ref("")

const onClickDeleteBtn = () => {
    let projectId = props.id;
    props.deleteFunc(projectId);
}

const onClickEnterProjectBtn = () => {
    let routeUrl = router.resolve({
        path:"/project/detail",
        query: {projectId: props.id}
    });
    window.open(routeUrl.href, '_blank')
}

</script>

<style scoped>

</style>