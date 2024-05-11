<template>
    <el-card
        :style='{fontSize: fontSize + "px"}'
        style='margin: 10px; width: 100%; height: fit-content;'
    >
        <template #header>
            <el-row justify='space-between' align='middle' style='width: 100%;  align-items: center'>
                <el-col span=20>
                    <el-row align='middle'>
                        <el-text :style='{fontSize: fontSize + "px", marginRight: 10 + "px"}'>问题(ID:{{problemId}})</el-text>
                        <el-tag v-if='problemSeverity === "ERROR"' type='danger' size='large'>严重</el-tag>
                        <el-tag v-else-if='problemSeverity === "WARNING"' type='warning' size='large'>警告</el-tag>
                        <el-tag v-else type='info' size='large'>未知</el-tag>
                    </el-row>
                </el-col>
                <el-col span=20>
                    <el-button type='primary' plain @click='goToLine(problemDetail.file, problemDetail.line)'>跳转</el-button>
                </el-col>
            </el-row>
        </template>
        <el-row>
            <el-descriptions title='问题信息' :column='1' >
                <template v-for='dItem in displayItems'>
                    <el-descriptions-item v-if='dItem.value' :label='dItem.key'>{{dItem.value}}</el-descriptions-item>
                </template>
                <el-descriptions-item >
                    <el-collapse>
                        <el-collapse-item title='执行路径' name='1'>
                            <el-row style='flex-direction: column' align='middle'>
                                <el-card v-for='item in trace' style='width: 90%; margin: 5px'>
                                    <template #header>
                                        <el-row style='width: 100%' justify='end'>
                                            <el-button text @click='goToLine(item.file, item.line)' type='primary'>跳转</el-button>
                                        </el-row>
                                    </template>
                                    <el-descriptions :column='1' label-class-name="my-label" class-name="my-content">
                                        <el-descriptions-item label='行号'>
                                            {{item.line}}
                                        </el-descriptions-item>
                                        <el-descriptions-item label='起止列号'>
                                            {{item.col}}:{{item.end_col}}
                                        </el-descriptions-item>
                                        <el-descriptions-item label='类型'>
                                            {{item.kind}}
                                        </el-descriptions-item>
                                        <el-descriptions-item label='文件'>
                                            {{item.file}}
                                        </el-descriptions-item>
                                        <el-descriptions-item label='描述'>
                                            {{item.desc}}
                                        </el-descriptions-item>
                                    </el-descriptions>
                                </el-card>
                            </el-row>
                        </el-collapse-item>
                    </el-collapse>
                </el-descriptions-item>
            </el-descriptions>
        </el-row>

    </el-card>
</template>

<script setup lang='ts'>
import { onMounted, ref } from 'vue'

const props = defineProps({
    id:{
      required: true,
      type: Number
    },
    problemId: {
        required: true,
        type: Number
    },
    filePath:{
        required: true,
        type: String
    },
    problemClassName:{
        required: true,
        type: String
    },
    problemSeverity:{
        required: true,
        type: String
    },
    problemDetailJsonString:{
        required: true,
        type: String
    },
    fontSize:{
        required: false,
        type: Number,
        default: 18
    },
    goToLine:{
        required: true,
        type: Function
    }
})
interface DisplayItemsType {
    key: string,
    value: string
}

type ProblemCalssType = {
    name: string,
    profile: string,
    severity: string,
    inspection_name: string
}
type ProblemDetailType = {
    file: string,
    function: string,
    code_snippet: string,
    line: number,
    offset: number,
    length: number,
    language: string,
    description: string,
    reason: string,
    source: string,
    sourceClean: string,
    problem_class: ProblemCalssType
}

const displayItems = ref<DisplayItemsType[]>([])

const problemDetail = ref<ProblemDetailType>()
const trace = ref([])

const initInfo = () => {
    problemDetail.value = JSON.parse(props.problemDetailJsonString);
    trace.value = problemDetail.value.trace;
    // console.log(trace.value)
    // console.log(problemDetail.value)

    displayItems.value = [
        {
            key:"问题类型",
            value: problemDetail.value.problem_class.name
        },
        {
            key:"文件",
            value: problemDetail.value.file
        },
        {
            key:"函数",
            value: problemDetail.value.function
        },
        {
            key:"代码片段",
            value: problemDetail.value.code_snippet
        },
        {
            key:"行号",
            value: problemDetail.value.line
        },
        {
            key:"偏移量",
            value: problemDetail.value.offset
        },
        {
            key:"长度",
            value: problemDetail.value.length
        },
        {
            key:"语言",
            value: problemDetail.value.language
        },
        {
            key:"描述",
            value: problemDetail.value.description
        },

        {
            key:"原因",
            value: problemDetail.value.reason
        },
        {
            key:"问题类别概况",
            value: problemDetail.value.problem_class.profile
        },
        {
            key:"问题严重性",
            value: problemDetail.value.problem_class.severity
        },
        {
            key:"问题类别检查名",
            value: problemDetail.value.problem_class.inspection_name
        },
        {
            key:"source",
            value: problemDetail.value.source
        },
        {
            key:"sourceClean",
            value: problemDetail.value.sourceClean
        },
    ]

}

onMounted(initInfo)

</script>

<style scoped>
:deep(.my-label){
    color: #232323;
    font-weight: bold;
}

:deep(.my-content){
    color: #2309a4;
}
</style>