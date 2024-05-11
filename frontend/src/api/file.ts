import request from '@/utils/request'

export function getFileObjByFileId(fileId: string){
    const data = {
        fileId
    }
    return request({
        url: 'file/getFileObjByFileId',
        method: 'post',
        data: data
    })
}

export function getByFileId(fileId: string){
    const args = {
        fileId
    }
    return request({
        url: 'file/getByFileId',
        method: 'get',
        params: args
    })
}

export function getFileObjListByQuery(data:any){
    return request({
        url: 'file/getFileObjListByQuery',
        method: 'post',
        data: data
    })
}

export function uploadFileAPI(fileName:string, fileContent:string, fileType:string, isPrivate:boolean){
    const data = {
        fileName,
        fileContent,
        isPrivate,
        fileType
    }
    return request({
        url: 'file/uploadFile',
        method: 'post',
        data: data
    })
}

