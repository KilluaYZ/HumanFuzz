import { Storage } from '@/utils/cache'
import { UserInfo } from '@/types'

function logout(){
    Storage.removeItem('userInfo')
    // Storage.removeItem('token')
    removeUserInfo();
    removeToken();
    location.reload();
}

function setUserInfo(userInfo: any){
    Storage.setItem('userInfo', userInfo);
}

function getUserInfo(): UserInfo{
    return Storage.getItem('userInfo');
}

function removeUserInfo(){
    Storage.removeItem('userInfo');
}

function getToken(): string{
    let token: string = Storage.getItem("token");
    return token;
}

function setToken(token: string){
    Storage.setItem('token', token);
}

function removeToken(){
    Storage.removeItem('token');
}

export {
    logout, getToken, setToken, removeToken, setUserInfo, getUserInfo, removeUserInfo
}