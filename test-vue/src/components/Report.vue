<template>
    <div>
        <template>
            <v-tabs :value="3" background-color="primary">
                <!-- @click=""中可以直接写方法 和在methods中写的区别是不用写this. -->
                <v-tab @click="$router.push({name:'Case'})">用例管理</v-tab>
                <v-tab @click="$router.push({name:'Task'})">任务管理</v-tab>
                <v-tab @click="$router.push({name:'Jenkins'})">Jenkins管理</v-tab>
                <v-tab @click="$router.push({name:'Report'})">报告管理</v-tab>
            </v-tabs>
        </template>
        <!-- style设定的宽和高是画布的范围 -->
        <div id="main" style="width:500px;height:500px"></div>
        report
    </div>
</template>

<script>
export default {
    data(){
        
    },
    methods(){

    },
    // mounted是vue的声明周期  所有dom元素加载后执行 要获取getElementById画图的地方
    // 所以不能用created或update里
    mounted(){
        // 引用echarts
        var echarts = require('echarts');
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('main'))
        // 绘制图表
        myChart.setOption({
            title:{
                text:'ECharts 入门示例'
            },
            tooltip:{},
            xAxis:{
                data:['大大','喵喵','欢欢','云梦','华山']
            },
            yAxis:{},
            series:[{
                name:'攻击力',
                type:'bar',
                data:[70,50,10,90,200]
            }]
        })
    },
}
</script>

<style scoped>
    
</style>