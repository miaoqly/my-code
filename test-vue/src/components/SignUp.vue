<template>
    <div class="register-form">
        <h1>注册</h1>
        <v-text-field v-model="username" label="用户名"></v-text-field>
        <v-text-field v-model="password" label="密码" type="password"></v-text-field>
        <v-text-field v-model="email" label="邮箱"></v-text-field>
        <v-btn class="ma-2" color="primary" @click="register()" >注册</v-btn>
        <v-btn class="ma-2" color="secondary" @click="signIn()" text>登录</v-btn>
    </div>
</template>

<script>
export default {
    data() {
        return {
            username: '',
            password: '',
            email: ''
        }
    },
    methods: {
        signIn() {
            // 先打印一句话 看是否调用了这个方法
            console.log('miao要跳转到登录')
            // 通过signIn的name跳转
            this.$router.push({name:'SignIn'})
        },
        register(){
            // 先打印一句话 看是否调用了这个方法
            console.log('miao要注册啦')
            // 把参数保存在变量中
            let post_data = {
                username : this.username,
                password : this.password,
                email : this.email
            }
            // 通过$api调用服务器注册接口传参 到signUp其实已经调用完成
            // 为了查看数据 调用then方法 then方法的参数是固定写法
            this.$api.user.signUp(post_data).then(res=>{
                console.log(res)
            })
        }
    },    
}
</script>

<style scoped>
     .register-form{
        /* 宽度 */
        width: 500px;
        /* 居中 */
        margin: 0 auto;
        /* 登录居中 */
        text-align: center;
    }   
</style>