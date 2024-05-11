import request from '@/utils/request'
import { types } from 'sass'
import List = types.List

export default function chatAi(chatHistory: { role: string, content: string }[]){
    let data = {
        chatHistory
    }

    return request({
        url: "ai/chat",
        method: "post",
        data: data
    })
}