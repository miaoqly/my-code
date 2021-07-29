<template>
    <div>
        <template>
            <v-tabs :value="1" background-color="primary">
                <!-- @click=""中可以直接写方法 和在methods中写的区别是不用写this. -->
                <v-tab @click="$router.push({name:'Case'})">用例管理</v-tab>
                <v-tab @click="$router.push({name:'Task'})">任务管理</v-tab>
                <v-tab @click="$router.push({name:'Jenkins'})">Jenkins管理</v-tab>
                <v-tab @click="$router.push({name:'Report'})">报告管理</v-tab>
            </v-tabs>
        </template>
    </div>
</template>

<script>
export default {
    
}
</script>

<style scoped>
    
</style>