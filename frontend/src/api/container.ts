import request from '@/utils/request'
export function runContainer(name: string){
    const data = {
        name: name,
    }
    return request({
        url: 'container/run',
        method: 'post',
        data: data
    })
}

export function removeContainer(container_id: string){
    const data = {
        container_id: container_id
    }
    return request({
        url: 'container/remove',
        method: 'post',
        data: data
    })
}

export function startContainer(container_id: string){
    const data = {
        container_id: container_id
    }
    return request({
        url: 'container/start',
        method: 'post',
        data: data
    })
}

export function stopContainer(container_id: string){
    const data = {
        container_id: container_id
    }
    return request({
        url: 'container/stop',
        method: 'post',
        data: data
    })
}

export function listContainer(){
    return request({
        url: 'container/list',
        method: 'post',
    })
}


export function getContainer(container_id: string){
    const data = {
        container_id: container_id
    }
    return request({
        url: 'container/get',
        method: 'post',
        data: data
    })
}
