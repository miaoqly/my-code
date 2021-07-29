import axios from 'axios'
import { config } from 'vue/types/umd'
var instance = axios.create({
    headers:{
        'Content-Type':'application/json'
    },
    baseURL:'http://stuq.ceshiren.com:8089/'
})
//这实际上是一个发送请求拦截器    如果本地的localStorage存了token    就把它放入请求的headers中
instance.interceptors.request.use(config=>{
    if(localStorage.getItem('token')){
        config.headers.common['token'] = localStorage.getItem('token')
    }
    return config
})
export default instance