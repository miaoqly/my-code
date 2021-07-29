import axios from './http'
const cases ={
    getList(params){
        return axios.get('/testCase/list',params)
    }, 
    createCaseByText(params){
        return axios.post('/testCase/text',params)
    },
    createCaseByFile(params){
        return axios.post('/testCase/file',{
            methods:'post',
            data:params,
            headers:{'Content-type':'multipart/form-data'}
        })
    },
    deleteCase(params){
        // 这里需要拼接caseId
        return axios.delete('/testCase/'+params.caseId,params)
    },
    editCase(params){
        return axios.put('/testCase/',params)
    },
    createTask(params){
        return axios.post('/task/',params)
    }
}
export default cases