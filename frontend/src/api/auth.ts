import request from '@/utils/request'
export function login(email: string, password: string){
    const data = {
        email,
        password
    }
    return request({
        url: 'user/login',
        headers: {
            isToken: false
        },
        method: 'post',
        data: data
    })
}

export function register(userName: string, email: string, password: string, checkCode: string, sessionKey: string){
    let data = {
        userName,
        email,
        password,
        checkCode,
        sessionKey
    }
    return request({
        url: 'user/register',
        headers: {
            isToken: false
        },
        method: 'post',
        data: data
    })
}

export function updatePwd(email: string, password: string, checkCode: string, sessionKey: string){
    let data = {
        email,
        password,
        checkCode,
        sessionKey
    }
    return request({
        url: 'user/updatePwd',
        headers: {
            isToken: false
        },
        method: 'post',
        data: data
    })
}

export function getRegisterSessionKeyCheckCode(userName: string, email: string){
    let data = {
        userName, email,
        "type":"register"
    }
    return request({
        url: 'user/getSessionKeyCheckCode',
        headers: {
            isToken: false
        },
        method: 'post',
        data: data
    })
}

export function getChangePwdSessionKeyCheckCode(email: string){
    let data = {
        email,
        "type":"changePasswd"
    }
    return request({
        url: 'user/getSessionKeyCheckCode',
        headers: {
            isToken: false
        },
        method: 'post',
        data: data
    })
}

export function checkIfEmailIsRegisted(email: string){
    let data = {
        email
    }
    return request({
        url: 'user/register/check',
        headers:{
            isToken: false
        },
        method: 'post',
        data: data
    })
}

export function userProfile(){
    return request({
        url: 'user/profile/get',
        method: 'post'
    })
}

export function changeUserProfile(data: any){
    const payload = {
        "userName": data.userName,
        "signature": data.signature,
        "sex": data.sex ? 'male' : 'female'
    }
    return request({
        url: 'user/profile/change',
        method: 'post',
        data: payload
    })
}

export function getAvatarListAPI(){
    const data = {}
    return request({
        url: 'user/avatar/list',
        method: 'post',
        data: data
    })
}

export function updateAvatarListAPI(fileId: string){
    const data = {
        fileId
    }
    return request({
        url: 'user/avatar/update',
        method: 'post',
        data: data
    })
}
