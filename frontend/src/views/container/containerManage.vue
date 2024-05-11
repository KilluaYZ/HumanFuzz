<template>

    <el-row>
        <el-card shadow='hover' style='width: 100%'>
            <template #header>
                <h1>容器概览</h1>
            </template>
            <el-row style='width: 100%' justify='start'>
                <el-col span=20>
                    <el-button type='success' @click='onClickAddContainerBtn'>新建容器</el-button>
                </el-col>
            </el-row>
        </el-card>
    </el-row>

    <el-row justify='space-evenly'>
        <ContainerCard
            v-for='item in data'
            :id='item._id'
            :name='item.name'
            :stage='item.status'
            :create_time='item.create_time'
            :delete-func='onClickDelBtn'
            :container_id="item.container_id"
            :ssh_port="item.ssh_port"
            :ws_port="item.ws_port"
        />
    </el-row>

    <el-dialog
        v-model='dialogVisible'
        title='新建容器'
        width='40%'>
        <el-row style='width: 100%'>
            <el-form
                :model='form'
                label-width='120px'
            >
                <el-form-item label='容器名' prop='name'>
                    <el-input v-model='form.name' placeholder='请输入容器名' clearable />
                </el-form-item>
            </el-form>
        </el-row>

        <template #footer>
          <span class="dialog-footer">
            <el-button @click="onClickCancelBtn">取消</el-button>
            <el-button type="primary" @click="onClickCommitBtn">确认</el-button>
          </span>
        </template>
    </el-dialog>
</template>

<script setup lang='ts'>
import { onMounted, ref } from 'vue'
import ProjectCard  from '@/components/ProjectCard.vue'
import { ElLoading, ElMessage} from 'element-plus'
import { types } from 'sass'
import { runContainer, removeContainer, listContainer, startContainer, stopContainer } from '@/api/container'
import {ContainerType} from '@/types'

const dialogVisible = ref(false);

const onClickAddContainerBtn = () => {
    dialogVisible.value = true;
}

const form = ref({
    name: "",
})

const resetForm = () => {
    form.value.name = "";
}


const data = ref<ContainerType[]>([])


const onClickCancelBtn = () => {
    resetForm();
}

const onClickCommitBtn = () => {
    // 先检验一下
    if(form.value.name === undefined || form.value.name.length === 0){
        ElMessage({
            type: 'error',
            message: '请填写项目名称'
        })
        return ;
    }
    const tLoading = ElLoading.service({
        lock: true,
        text: '正在新建',
        background: 'rgba(0, 0, 0, 0.7)'
    });

    runContainer(form.value.name)
        .then((res) => {
            ElMessage({
                type: 'success',
                message: `新建成功！容器id为:${res.data.container_id}`
            })
            getList()
            tLoading.close()
            dialogVisible.value =  false;
        })
        .catch(() => {
            tLoading.close()
        })
}

const getList = () => {
    listContainer().then(res => {
        data.value = res.data;
        console.log(data.value)
    })
}

const onClickDelBtn = (container_id: string) => {
    const delProjectLoading = ElLoading.service({
        lock: true,
        text: '正在删除',
        background: 'rgba(0, 0, 0, 0.7)'
    });
    removeContainer(container_id).then(res => {
        getList();
        delProjectLoading.close()
    }).catch(() => {
        delProjectLoading.close()
    })
}

onMounted(getList)

</script>


<style scoped>
.text-red{
    color: red;
}
</style>