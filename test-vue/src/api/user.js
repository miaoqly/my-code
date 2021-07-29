// 引用http.js配置的axios
import axios from './http'

// 定义变量user 
const user ={
    // user要调用的方法 参数要写在括号里
    signIn(params){
        // 用axios调用接口方法  post方法就.post
        // 参数一个是接口请求地址   一个是调用接口的传参
        return axios.post('/user/login',params)
    },
    signUp(params){
        return axios.post('/user/register',params)
    }
    
}
// 把方法暴露出去   方便其他js文件调用
export default user