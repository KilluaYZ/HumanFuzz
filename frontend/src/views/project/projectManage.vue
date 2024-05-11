<template>

    <el-row>
        <el-card shadow='hover' style='width: 100%'>
            <template #header>
                <h1>项目概览</h1>
            </template>
            <el-row style='width: 100%' justify='start'>
                <el-col span=20>
                    <el-button type='success' @click='onClickAddProjectBtn'>新建项目</el-button>
                </el-col>
            </el-row>
        </el-card>
    </el-row>

    <el-row justify='space-evenly'>
        <ProjectCard
            v-for='item in data'
            :id='item._id'
            :name='item.name'
            :stage='item.status'
            :create-time='item.create_time'
            :delete-func='onClickDelBtn'
            :crash-num='item.crash_num'
            :seed-num='item.seed_num'
        />
    </el-row>

    <el-dialog
        v-model='dialogVisible'
        title='新建项目'
        width='40%'>

        <el-row style='width: 100%'>
            <el-form
                :model='form'
                label-width='120px'
            >
                <el-form-item label='项目名' prop='name'>
                    <el-input v-model='form.name' placeholder='请输入项目名' clearable />
                </el-form-item>

                <el-form-item label='容器' prop='container_id'>
                    <el-select
                        v-model="form.container_id"
                        placeholder="请选择容器"
                    >
                        <el-option
                            v-for="item in ContainerList"
                            :key="item.container_id"
                            :label="item.name"
                            :value="item.container_id"
                        />
                    </el-select>
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
import { addProject, delProject, getProjectList } from '@/api/project'
import { ContainerType, ProjectType } from '@/types'
import { listContainer } from '@/api/container'

const dialogVisible = ref(false);

const onClickAddProjectBtn = () => {
    listContainer().then((res) => {
        ContainerList.value = Array();
        res.data.forEach((item:ContainerType) => {
            if(item.status === 'running'){
                ContainerList.value!.push(item)
            }
        })
        dialogVisible.value = true;
    })
}

const ContainerList = ref<ContainerType[]>()

const form = ref({
    name: "",
    container_id: ""
})

const resetForm = () => {
    form.value.name = ""
    form.value.container_id = ""
}


const data = ref<ProjectType[]>([])


const onClickCancelBtn = () => {
    resetForm();
    dialogVisible.value = false;
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
    addProject(form.value.name, form.value.container_id)
        .then((res) => {
            ElMessage({
                type: 'success',
                message: res.msg
            })
            getList();
            dialogVisible.value = false;
        })
}

const getList = () => {
    getProjectList().then(res => {
        data.value = res.data;
    }).catch(() => {

    })
}

const onClickDelBtn = (projectId: string) => {
    const delProjectLoading = ElLoading.service({
        lock: true,
        text: '正在删除',
        background: 'rgba(0, 0, 0, 0.7)'
    });
    delProject(projectId).then(res => {
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