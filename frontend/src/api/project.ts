import request from '@/utils/request'
import { ProjectType, QueueEntryType } from '@/types'
export function addProject(projectName: string, containerId: string){
    const data = {
        name: projectName,
        container_id: containerId
    }
    return request({
        url: 'project/add',
        method: 'post',
        data: data
    })
}

export function configProject(project_id: string, configForm: ProjectType){
    const data = {
        project_id: project_id,
        binary_path: configForm.binary_path,
        output_path: configForm.output_path,
        binary_cov_path: configForm.binary_cov_path,
        input_path: configForm.input_path,
        binary_args: configForm.binary_args,
    }
    return request({
        url: 'project/config',
        method: 'post',
        data: data
    })
}

export function getProjectDetail(projectId: string){
    const data = {
        project_id: projectId
    }
    return request({
        url: 'project/get',
        method: 'post',
        data: data
    })
}

export function getProjectList(){
    return request({
        url: 'project/list',
        method: 'post'
    })
}

export function delProject(projectId: string){
    let data = {
        project_id: projectId
    }

    return request({
        url: 'project/del',
        method: 'post',
        data: data
    })
}

export function fuzz_add_fuzzer(projectId: string){
    let data = {
        project_id: projectId
    }

    return request({
        url: 'project/fuzz/add',
        method: 'post',
        data: data
    })
}

export function fuzz_start_fuzzer(projectId: string){
    let data = {
        project_id: projectId
    }

    return request({
        url: 'project/fuzz/start',
        method: 'post',
        data: data
    })
}

export function fuzz_resume_fuzzer(projectId: string){
    let data = {
        project_id: projectId
    }

    return request({
        url: 'project/fuzz/resume',
        method: 'post',
        data: data
    })
}

export function fuzz_pause_fuzzer(projectId: string){
    let data = {
        project_id: projectId
    }

    return request({
        url: 'project/fuzz/pause',
        method: 'post',
        data: data
    })
}

export function fuzz_stop_fuzzer(projectId: string){
    let data = {
        project_id: projectId
    }

    return request({
        url: 'project/fuzz/stop',
        method: 'post',
        data: data
    })
}

export function fuzz_skip_cur_case(projectId: string){
    let data = {
        project_id: projectId
    }

    return request({
        url: 'project/fuzz/skip',
        method: 'post',
        data: data
    })
}

export function fuzz_read_cur(projectId: string){
    let data = {
        project_id: projectId
    }

    return request({
        url: 'project/fuzz/read/cur',
        method: 'post',
        data: data
    })
}

export function fuzz_read_queue(projectId: string){
    let data = {
        project_id: projectId
    }

    return request({
        url: 'project/fuzz/read/queue',
        method: 'post',
        data: data
    })
}

export function fuzz_read_stat(projectId: string){
    let data = {
        project_id: projectId
    }

    return request({
        url: 'project/fuzz/read/stat',
        method: 'post',
        data: data
    })
}

export function fuzz_write_cur(projectId: string, queue_cur: QueueEntryType){
    let data = {
        project_id: projectId,
        queue_cur: queue_cur
    }

    return request({
        url: 'project/fuzz/write/cur',
        method: 'post',
        data: data
    })
}

export function fuzz_write_by_id(projectId: string, modify_queue_entry_idx: number, modify_queue_entry: QueueEntryType){
    let data = {
        project_id: projectId,
        modify_queue_entry_idx: modify_queue_entry_idx,
        modify_queue_entry: modify_queue_entry
    }

    return request({
        url: 'project/fuzz/write/byid',
        method: 'post',
        data: data
    })
}

export function fuzz_target_case_by_id(projectId: string, target_queue_entry_idx: number){
    let data = {
        project_id: projectId,
        target_queue_entry_idx: target_queue_entry_idx
    }

    return request({
        url: 'project/fuzz/fuzzbyid',
        method: 'post',
        data: data
    })
}