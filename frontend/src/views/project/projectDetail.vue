<template>
    <el-row style="width: 100%; height: 100%">
        <el-row style="width: 50%; height: 100%;padding: 15px 20px 15px 20px; flex-direction: column;justify-content: space-between; align-items: center">
            <el-row style="width: 100%; height: 80%; border-radius: 10px;" class="card-eff">
                <el-row style="width: 100%; height: 100%;flex-direction: column; justify-content: center; align-items: center; flex-wrap: nowrap; padding: 10px 20px 10px 20px">
                    <el-row  style="width: 100%; " class="fuzz_stat_header">
                        <el-row style="width: 50%;">
                            <el-descriptions  title="process timing" :column="1" style="height: fit-content; width: 100%" size="small">
                                <el-descriptions-item  label="run time">{{fuzz_stat.run_time}}</el-descriptions-item>
                                <el-descriptions-item  label="last new path">{{fuzz_stat.last_new_path}}</el-descriptions-item>
                                <el-descriptions-item  label="last uniq crash">{{fuzz_stat.last_uniq_crash}}</el-descriptions-item>
                                <el-descriptions-item  label="last uniq hang">{{fuzz_stat.last_uniq_hang}}</el-descriptions-item>
                            </el-descriptions>
                        </el-row>
                        <el-row style="width: 50%">
                            <el-descriptions  title="overall results" :column="1" style="height: fit-content; width: 100%" size="small">
                                <el-descriptions-item  label="cycles done">{{fuzz_stat.cycles_done}}</el-descriptions-item>
                                <el-descriptions-item  label="total paths">{{fuzz_stat.total_path}}</el-descriptions-item>
                                <el-descriptions-item  label="uniq crashes">{{fuzz_stat.uniq_crashes}}</el-descriptions-item>
                                <el-descriptions-item  label="uniq hangs">{{fuzz_stat.uniq_hangs}}</el-descriptions-item>
                            </el-descriptions>
                        </el-row>
                    </el-row>
                    <el-row  style="width: 100%; " class="fuzz_stat_header">
                        <el-row style="width: 50%">
                            <el-descriptions  title="cycle progress" :column="1" style="height: fit-content; width: 100%" size="small">
                                <el-descriptions-item  label="now processing">{{fuzz_stat.now_processing}}</el-descriptions-item>
                                <el-descriptions-item  label="paths timed out">{{fuzz_stat.paths_timed_out}}</el-descriptions-item>
                            </el-descriptions>
                        </el-row>
                        <el-row style="width: 50%">
                            <el-descriptions  title="map coverage" :column="1" style="height: fit-content; width: 100%" size="small">
                                <el-descriptions-item  label="map density">{{fuzz_stat.map_density}}</el-descriptions-item>
                                <el-descriptions-item  label="count coverage">{{fuzz_stat.count_coverage}}</el-descriptions-item>
                            </el-descriptions>
                        </el-row>
                    </el-row>
                    <el-row style="width: 100%; " class="fuzz_stat_header">
                        <el-row style="width: 50%">
                            <el-descriptions  title="stage progress" :column="1"  style="height: fit-content; width: 100%" size="small">
                                <el-descriptions-item  label="now trying">{{fuzz_stat.now_trying}}</el-descriptions-item>
                                <el-descriptions-item  label="stage execs">{{fuzz_stat.stage_execs}}</el-descriptions-item>
                                <el-descriptions-item  label="total execs">{{fuzz_stat.total_execs}}</el-descriptions-item>
                                <el-descriptions-item  label="exec speed">{{fuzz_stat.exec_speed}}</el-descriptions-item>
                            </el-descriptions>
                        </el-row>
                        <el-row style="width: 50%">
                            <el-descriptions  title="findings in depth" :column="1" style="height: fit-content; width: 100%" size="small">
                                <el-descriptions-item  label="favored paths">{{fuzz_stat.favored_paths}}</el-descriptions-item>
                                <el-descriptions-item  label="new edges on">{{fuzz_stat.new_edges_on}}</el-descriptions-item>
                                <el-descriptions-item  label="total crashes">{{fuzz_stat.total_crashes}}</el-descriptions-item>
                                <el-descriptions-item  label="total tmouts">{{fuzz_stat.total_tmouts}}</el-descriptions-item>
                            </el-descriptions>
                        </el-row>
                    </el-row>
                    <el-row style="width: 100%; " class="fuzz_stat_header">
                        <el-row style="width: 50%;">
                            <el-descriptions  title="fuzzing strategy yields" :column="1" style="height: fit-content; width: 100%" size="small">
                                <el-descriptions-item  label="bit flips">{{fuzz_stat.bit_flips}}</el-descriptions-item>
                                <el-descriptions-item  label="byte flips">{{fuzz_stat.byte_flips}}</el-descriptions-item>
                                <el-descriptions-item  label="arithmetics">{{fuzz_stat.arithmetics}}</el-descriptions-item>
                                <el-descriptions-item  label="known ints">{{fuzz_stat.known_inis}}</el-descriptions-item>
                                <el-descriptions-item  label="dictionary">{{fuzz_stat.dictionary}}</el-descriptions-item>
                                <el-descriptions-item  label="havoc">{{fuzz_stat.havoc}}</el-descriptions-item>
                                <el-descriptions-item  label="trim">{{fuzz_stat.trim}}</el-descriptions-item>
                            </el-descriptions>
                        </el-row>
                        <el-row style="width: 50%">
                            <el-descriptions  title="path geometry" :column="1" style="height: fit-content; width: 100%" size="small">
                                <el-descriptions-item  label="levels">{{fuzz_stat.levels}}</el-descriptions-item>
                                <el-descriptions-item  label="pending">{{fuzz_stat.pending}}</el-descriptions-item>
                                <el-descriptions-item  label="pend fav">{{fuzz_stat.pend_fav}}</el-descriptions-item>
                                <el-descriptions-item  label="own finds">{{fuzz_stat.own_finds}}</el-descriptions-item>
                                <el-descriptions-item  label="imported">{{fuzz_stat.imported}}</el-descriptions-item>
                                <el-descriptions-item  label="stability">{{fuzz_stat.stability}}</el-descriptions-item>
                                <el-descriptions-item  label="cpu">{{fuzz_stat.cpu}}</el-descriptions-item>
                            </el-descriptions>
                        </el-row>
                    </el-row>
                </el-row>
            </el-row>
            <el-row style="width: 100%; height: 18%;  border-radius: 10px;" class="card-eff">
                <el-row style="width: 100%; height: 100%;">
                    <el-row style="width: 100%; height: 100%; flex-direction: column; justify-content: space-evenly; align-items: center;">
                        <el-row style="">
                            <el-button :disabled="project_info.status != 'running'" type="success" size="large" plain @click="resume_fuzz"><el-icon><VideoPlay /></el-icon>恢复Fuzz</el-button>
                            <el-button :disabled="project_info.status != 'running'" type="danger" size="large" plain @click="pause_fuzz"><el-icon><VideoPause /></el-icon>暂停Fuzz</el-button>
                            <el-button :disabled="project_info.status != 'running'" type="warning" size="large" plain @click="onClickSkipCurCaseBtn"><el-icon><DArrowRight /></el-icon>跳过当前种子</el-button>
                        </el-row>
                        <el-row>
                            <el-button :disabled="project_info.status == 'running'" type="primary" size="large" @click="onClickStartFuzzerBtn"><el-icon><Link /></el-icon>连接Fuzz</el-button>
                            <el-button :disabled="project_info.status != 'running'" type="danger" size="large" @click="onClickStopFuzzerBtn"><el-icon><VideoPause /></el-icon>停止Fuzz</el-button>
                            <el-button :disabled="project_info.status == 'running'" type="info" size="large" @click="onClickConfigProjectBtn"><el-icon><Setting /></el-icon>配置Fuzz</el-button>
                        </el-row>
                    </el-row>
                </el-row>
            </el-row>
        </el-row>
        <el-row style="width: 50%; height: 100%; padding: 15px 20px 15px 20px; flex-direction: column; justify-content: space-between; align-items: center">
            <el-row style="width: 100%; height: 28%; border-radius: 10px;" class="card-eff">
                <el-row style="width: 100%;height: 100%;flex-direction: column;justify-content: start; align-items: center; padding: 10px 20px 10px 20px">
                    <el-row style="width: 100%; height: 10%; justify-content: end;">
                        <el-button  type="success" size="small" @click="onClickEditQueueCurBtn" ><el-icon><EditPen /></el-icon>修改</el-button>
                        <el-button  type="primary" size="small" @click="get_queue_cur_info" ><el-icon><Refresh /></el-icon>刷新</el-button>
                    </el-row>
                    <el-row style="width: 100% ; height: 10%">
                        <span>fname: </span><span>{{ queue_cur.fname }}</span>
                    </el-row>
                    <el-row style="width: 100%; height: 80%">
                        <el-descriptions title="当前种子信息" style="height: fit-content; width: 100%" size="small">
                            <el-descriptions-item  label="cal_failed">{{queue_cur.cal_failed}}</el-descriptions-item>
                            <el-descriptions-item  label="trim_done">{{queue_cur.trim_done}}</el-descriptions-item>
                            <el-descriptions-item  label="was_fuzzed">{{queue_cur.was_fuzzed}}</el-descriptions-item>
                            <el-descriptions-item  label="passed_det">{{queue_cur.passed_det}}</el-descriptions-item>
                            <el-descriptions-item  label="has_new_cov">{{queue_cur.has_new_cov}}</el-descriptions-item>
                            <el-descriptions-item  label="favored">{{queue_cur.favored}}</el-descriptions-item>
                            <el-descriptions-item  label="fs_redundant">{{queue_cur.fs_redundant}}</el-descriptions-item>
                            <el-descriptions-item  label="exec_us">{{queue_cur.exec_us}}</el-descriptions-item>
                            <el-descriptions-item  label="handicap">{{queue_cur.handicap}}</el-descriptions-item>
                            <el-descriptions-item  label="depth">{{queue_cur.depth}}</el-descriptions-item>
                            <el-descriptions-item  label="distance">{{queue_cur.distance}}</el-descriptions-item>
                            <el-descriptions-item  label="perf_score">{{queue_cur.perf_score}}</el-descriptions-item>
                            <el-descriptions-item  label="user_set_perf_score">{{queue_cur.user_set_perf_score}}</el-descriptions-item>
                            <el-descriptions-item  label="target_coverage_score">{{queue_cur.target_coverage_score}}</el-descriptions-item>
                        </el-descriptions>
                    </el-row>
                </el-row>
            </el-row>
            <el-row style="width: 100%; height: 70%;   border-radius: 10px;" class="card-eff">
                <el-row style="width: 100%;height: 100%;flex-direction: column;justify-content: start; align-items: center">
                    <el-row style="width: 100%; height: 10%; justify-content: end;padding: 10px 10px 0 0">
                        <el-button size="small" type="primary" @click="get_queue_info"><el-icon><Refresh /></el-icon>刷新</el-button>
                    </el-row>
                    <el-row style="width: 100%; height: 90%; padding: 10px 20px 10px 20px">
                        <el-table
                            :data="queue_table_data"
                            style="width: 100%; height: 100%"
                            border
                            strip
                        >
                            <el-table-column sortable min-width="450" prop="fname" label="fname"/>
                            <el-table-column min-width="100" prop="favored" label="favored"/>
                            <el-table-column min-width="120" prop="was_fuzzed" label="was_fuzzed"/>
                            <el-table-column sortable min-width="200" prop="distance" label="distance"/>
                            <el-table-column sortable min-width="100" prop="target_coverage_score" label="target_cov"/>
                            <el-table-column sortable min-width="100" prop="perf_score" label="perf_score"/>
                            <el-table-column sortable min-width="180" prop="user_set_perf_score" label="user_set_perf_score"/>
                            <el-table-column min-width="60" prop="len" label="len"/>
                            <el-table-column min-width="100" prop="cal_failed" label="cal_failed"/>
                            <el-table-column min-width="100" prop="trim_done" label="trim_done"/>
                            <el-table-column min-width="120" prop="passed_det" label="passed_det"/>
                            <el-table-column min-width="150" prop="has_new_cov" label="has_new_cov"/>
                            <el-table-column min-width="120" prop="fs_redundant" label="fs_redundant"/>
                            <el-table-column min-width="100" prop="exec_us" label="exec_us"/>
                            <el-table-column min-width="100" prop="handicap" label="handicap"/>
                            <el-table-column min-width="100" prop="depth" label="depth"/>
                            <el-table-column fixed="right" label="Operation" width="120">
                                <template #default="scope">
                                    <el-row style="width: 100%; flex-direction: column; justify-content: center; align-items: center">
                                        <el-button
                                            link
                                            type="primary"
                                            size="small"
                                            @click.prevent="onClickEditQueueEntryBtn(scope.$index, scope.row)">
                                            修改
                                        </el-button>
                                        <el-button
                                            link
                                            type="success"
                                            size="small"
                                            @click.prevent="onClickFuzzTargetBtn(scope.row.queue_idx)">
                                            fuzz该种子
                                        </el-button>
                                    </el-row>
                                </template>
                            </el-table-column>
                        </el-table>
                    </el-row>
                </el-row>
            </el-row>
        </el-row>
    </el-row>

    <el-dialog
        v-model='configFuzzerDialogVisible'
        title='配置Fuzzer'
        width='40%'>

        <el-row style='width: 100%'>
            <el-form
                :model='configForm'
                label-width='200px'
            >
                <el-form-item label='fuzzer初始种子目录绝对路径' prop='input_path'>
                    <el-input v-model='configForm!.input_path' placeholder='/share/in' clearable />
                </el-form-item>

                <el-form-item label='fuzzer输出目录绝对路径' prop='output_path'>
                    <el-input v-model='configForm!.output_path' placeholder='/share/out' clearable />
                </el-form-item>

                <el-form-item label='待测试的二进制绝对路径' prop='binary_path'>
                    <el-input v-model='configForm!.binary_path' placeholder='/share/xmllint' clearable />
                </el-form-item>

                <el-form-item label='覆盖率插桩的二进制绝对路径' prop='binary_cov_path'>
                    <el-input v-model='configForm!.binary_cov_path' placeholder='/share/xmllint-cov' clearable />
                </el-form-item>

                <el-form-item label='待测程序命令行参数' prop='binary_args'>
                    <el-input v-model='configForm!.binary_args' placeholder='--valid @@' clearable />
                </el-form-item>
            </el-form>

        </el-row>

        <template #footer>
          <span class="dialog-footer">
            <el-button @click="ConfigOnClickCancelBtn">取消</el-button>
            <el-button type="primary" @click="ConfigOnClickCommitBtn">确认</el-button>
          </span>
        </template>
    </el-dialog>

    <el-dialog
        v-model='EditQueueEntryDialogVisible'
        title='设置种子属性'
        width='40%'>

        <el-row style='width: 100%'>
            <el-form
                style="width: 100%"
                :model='queueEditForm'
                label-width='140px'
            >
                <el-form-item label='种子名' prop='fname'>
                    <el-input disabled v-model='queueEditForm.fname' />
                </el-form-item>

                <el-form-item label='是否感兴趣' prop='favored'>
                    <el-switch v-model='queueEditForm.favored' inline-prompt active-text="是" inactive-text="否" :active-value="1" :inactive-value="0" />
                </el-form-item>

                <el-form-item label='是否已经被fuzz' prop='was_fuzzed'>
                    <el-switch v-model='queueEditForm.was_fuzzed' inline-prompt active-text="是" inactive-text="否" :active-value="1" :inactive-value="0" />
                </el-form-item>

                <el-form-item label='种子目标距离' prop='distance'>
                    <el-input-number v-model='queueEditForm.distance' :precision="2" :step="0.01"/>
                </el-form-item>

                <el-form-item label='用户设定种子分数' prop='distance'>
                    <el-input-number  v-model='queueEditForm.user_set_perf_score' />
                </el-form-item>
            </el-form>

        </el-row>

        <template #footer>
          <span class="dialog-footer">
            <el-button @click="EditOnClickCancelBtn">取消</el-button>
            <el-button type="primary" @click="EditOnClickCommitBtn">确认</el-button>
          </span>
        </template>
    </el-dialog>

</template>

<script setup lang="ts">

import { onMounted, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { FuzzStatType, ProjectType, QueueEntryType } from '@/types'
import { getProjectDetail, configProject, fuzz_start_fuzzer, fuzz_write_by_id, fuzz_write_cur, fuzz_read_cur, fuzz_read_stat, fuzz_read_queue, fuzz_add_fuzzer, fuzz_resume_fuzzer, fuzz_pause_fuzzer, fuzz_stop_fuzzer, fuzz_skip_cur_case, fuzz_target_case_by_id } from '@/api/project'
import { DArrowRight, EditPen, Link, Refresh, Setting, VideoPause, VideoPlay } from '@element-plus/icons-vue'
import { ElMessage } from 'element-plus'

const router = useRouter();
const route  = useRoute();
const projectId = route.query.projectId as string
const project_info = ref<ProjectType>({
    _id: '',
    name: '',
    status: '',
    create_time: '',
    crash_num: 0,
    seed_num: 0,
    container_id: '',
    user_id: '',
    binary_path: '',
    binary_cov_path: '',
    output_path: '',
    input_path: '',
    binary_args: '',
    target_path: ''
});
const fuzz_stat = ref<FuzzStatType>({
    run_time: "",
    last_new_path: "",
    last_uniq_crash: "",
    last_uniq_hang: "",
    cycles_done: "",
    total_path: "",
    uniq_crashes: "",
    uniq_hangs: "",
    now_processing: "",
    paths_timed_out: "",
    map_density: "",
    count_coverage: "",
    now_trying: "",
    stage_execs: "",
    total_execs: "",
    exec_speed: "",
    favored_paths: "",
    new_edges_on: "",
    total_crashes: "",
    total_tmouts: "",
    bit_flips: "",
    byte_flips: "",
    arithmetics: "",
    known_inis: "",
    dictionary: "",
    havoc: "",
    trim: "",
    levels: "",
    pending: "",
    pend_fav: "",
    own_finds: "",
    imported: "",
    stability: "",
    cpu: ""
});

const queue_cur = ref<QueueEntryType>({
    fname: '',
    len: 0,
    cal_failed: 0,
    trim_done: 0,
    was_fuzzed: 0,
    passed_det: 0,
    has_new_cov: 0,
    favored: 0,
    fs_redundant: 0,
    exec_us: 0,
    handicap: 0,
    depth: 0,
    distance: 0,
    perf_score: 0,
    user_set_perf_score: 0,
    target_coverage_score: 0,
    queue_idx: 0
});

const queue_table_data = ref<QueueEntryType[]>([])

const configFuzzerDialogVisible = ref(false)
const configForm = ref<ProjectType>({
    _id: '',
    name: '',
    status: '',
    create_time: '',
    crash_num: 0,
    seed_num: 0,
    container_id: '',
    user_id: '',
    binary_path: '',
    binary_cov_path: '',
    output_path: '',
    input_path: '',
    binary_args: '',
    target_path: ''
})

const queueEditForm = ref<QueueEntryType>({
    fname: '',
    len: 0,
    cal_failed: 0,
    trim_done: 0,
    was_fuzzed: 0,
    passed_det: 0,
    has_new_cov: 0,
    favored: 0,
    fs_redundant: 0,
    exec_us: 0,
    handicap: 0,
    depth: 0,
    distance: 0,
    perf_score: 0,
    user_set_perf_score: 0,
    target_coverage_score: 0,
    queue_idx: 0
})

const EditQueueEntryDialogVisible = ref(false)
const isEditQueueCur = ref(false)

const resetForm = () => {
    configForm.value!.binary_path = "";
    configForm.value!.binary_cov_path = "";
    configForm.value!.output_path = "";
    configForm.value!.input_path = "";
    configForm.value!.binary_args = "";

    queueEditForm.value.was_fuzzed = 0;
    queueEditForm.value.favored = 0;
    queueEditForm.value.distance = 0;
    queueEditForm.value.user_set_perf_score = 0;
}

const get_project_info = () => {
    return getProjectDetail(projectId)
        .then(res => {
            project_info.value = res.data;
        })
}

const get_fuzz_stat = () => {
    fuzz_read_stat(projectId)
        .then(res => {
            fuzz_stat.value = res.data;
        })
}

const resume_fuzz = () => {
    fuzz_resume_fuzzer(projectId)
        .then((res) => {
            ElMessage({
                type: "success",
                message: res.msg
            })
        })
}

const pause_fuzz = () => {
    fuzz_pause_fuzzer(projectId)
        .then((res) => {
            ElMessage({
                type: "success",
                message: res.msg
            })
        })
}

const get_queue_cur_info = () => {
    fuzz_read_cur(projectId)
        .then(res => {
            queue_cur.value = res.data;
        })
}

const get_queue_info = () => {
    fuzz_read_queue(projectId)
        .then(res => {
            queue_table_data.value = res.data;
            for(let i = 0;i < queue_table_data.value.length; i++){
                queue_table_data.value[i].queue_idx = i;
            }
        })
}

const ConfigOnClickCommitBtn = () => {
    if(
        configForm.value?.binary_path == null || configForm.value?.binary_path.length <= 0
        || configForm.value?.output_path == null || configForm.value?.output_path.length <= 0
        || configForm.value?.binary_cov_path == null || configForm.value?.binary_cov_path.length <= 0
        || configForm.value?.input_path == null || configForm.value?.input_path.length <= 0
        || configForm.value?.binary_args == null || configForm.value?.binary_args.length <= 0
    ){
        ElMessage({
            type: 'error',
            message: "请将信息填写完整！"
        })
        return;
    }
    configProject(projectId, configForm.value!)
        .then(res => {
            ElMessage({
                type: "success",
                message: res.msg
            })
            configFuzzerDialogVisible.value = false;
            resetForm();
        })
}

const ConfigOnClickCancelBtn = () => {
    resetForm();
    configFuzzerDialogVisible.value = false;
}

const onClickConfigProjectBtn = () => {
    get_project_info().then(() => {
        configForm.value!.binary_path = project_info.value!.binary_path;
        configForm.value!.binary_cov_path = project_info.value!.binary_cov_path;
        configForm.value!.output_path = project_info.value!.output_path;
        configForm.value!.input_path = project_info.value!.input_path;
        configForm.value!.binary_args = project_info.value!.binary_args;
        configFuzzerDialogVisible.value = true;
    })
}


const onClickStartFuzzerBtn= () => {
    fuzz_start_fuzzer(projectId)
        .then(res => {
            setTimeout(() => {
                fuzz_add_fuzzer(projectId).then(res => {
                    ElMessage({
                        type: "success",
                        message: res.msg
                    })
                    start_interval()
                    project_info.value.status = 'running'
                })
            }, 3000)
        })
}

const start_interval = () => {
    setInterval(get_fuzz_stat, 1000)
}

onMounted(() =>  {
    get_project_info().then(() => {
        if(project_info.value.status === 'running'){
            fuzz_add_fuzzer(projectId).then(res => {
                ElMessage({
                    type: "success",
                    message: res.msg
                })
                start_interval()

                get_queue_cur_info()
                get_queue_info()
            })
        }
    })
})

const modify_queue_entry_idx = ref(0);


const onClickEditQueueEntryBtn = (idx: number, queue_entry: QueueEntryType) => {
    queueEditForm.value.fname = queue_entry.fname;
    queueEditForm.value.distance = queue_entry.distance;
    queueEditForm.value.was_fuzzed = queue_entry.was_fuzzed;
    queueEditForm.value.favored = queue_entry.favored;
    queueEditForm.value.user_set_perf_score = queue_entry.user_set_perf_score;
    isEditQueueCur.value = false;
    EditQueueEntryDialogVisible.value = true;
    modify_queue_entry_idx.value = idx;
}

const onClickEditQueueCurBtn = () => {
    queueEditForm.value.fname = queue_cur.value.fname;
    queueEditForm.value.distance = queue_cur.value.distance;
    queueEditForm.value.was_fuzzed = queue_cur.value.was_fuzzed;
    queueEditForm.value.favored = queue_cur.value.favored;
    queueEditForm.value.user_set_perf_score = queue_cur.value.user_set_perf_score;
    isEditQueueCur.value = true;
    EditQueueEntryDialogVisible.value = true;
}


const EditOnClickCancelBtn = () => {
    resetForm();
    EditQueueEntryDialogVisible.value = false;
}


const EditOnClickCommitBtn = () => {
    if(isEditQueueCur.value){
        fuzz_write_cur(projectId, queueEditForm.value)
            .then(res => {
                ElMessage({
                    type: "success",
                    message: res.msg
                })
                get_queue_cur_info();
                EditQueueEntryDialogVisible.value  = false;
            })
    }else{
        fuzz_write_by_id(projectId, modify_queue_entry_idx.value, queueEditForm.value)
            .then(res => {
                ElMessage({
                    type: "success",
                    message: res.msg
                })
                get_queue_info();
                EditQueueEntryDialogVisible.value  = false;
            })
    }
}

const onClickStopFuzzerBtn = () =>{
    fuzz_stop_fuzzer(projectId)
        .then(res => {
            ElMessage({
                type: "success",
                message: res.msg
            })
            get_project_info()
        })
}

const onClickSkipCurCaseBtn = () =>{
    fuzz_skip_cur_case(projectId)
        .then(res => {
            ElMessage({
                type: "success",
                message: res.msg
            })
        })
}

const onClickFuzzTargetBtn = (target_queue_entry_idx: number) => {
    fuzz_target_case_by_id(projectId, target_queue_entry_idx)
        .then(res => {
            ElMessage({
                type: "success",
                message: res.msg
            })
        })
}

</script>

<style>
.card-eff{
    box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);
    background: #ffffff;
}

.el-descriptions--small .el-descriptions__body .el-descriptions__table:not(.is-bordered) .el-descriptions__cell{
    padding: 0;
}

.fuzz_stat_header{
    background: #dbdbdb;
}
</style>