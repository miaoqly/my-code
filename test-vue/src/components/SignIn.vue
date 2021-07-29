<template>
    <div class="login-form">
        <h1>登录</h1>
        <v-text-field v-model="username" label="用户名"></v-text-field>
        <v-text-field v-model="password" label="密码" type="password"></v-text-field>
        <v-btn class="ma-2" color="primary" @click="login()">登录</v-btn>
        <v-btn class="ma-2" color="secondary" text @click="signUp()">注册</v-btn>
    </div>
</template>

<script>
export default {
    data() {
        return {
            username: '',
            password: ''
        }
    },
    methods: {
        signUp() {
            // 先打印一句话 看是否调用了这个方法
            console.log('miao要跳转到注册')
            // 通过signUp的name跳转
            this.$router.push({name:'SignUp'})
        },
        login(){
            // 先打印一句话 看是否调用了这个方法
            console.log('miao要登录啦')
            let post_data = {
                username : this.username,
                password : this.password
            }
            this.$api.user.signIn(post_data).then(res=>{
                console.log(res)
                //存储token用localStorage方法    在调用登录接口后执行存储
                localStorage.setItem('token',res.data.data.token)
                localStorage.setItem('username',this.username)
                //登录后把Case.vue作为主页
                this,$router.push({name:'Case'})                
            })
        }
    },
}
</script>

<style scoped>
    .login-form{
        /* 宽度 */
        width: 500px;
        /* 居中 */
        margin: 0 auto;
        /* 登录居中 */
        text-align: center;
    }
</style>