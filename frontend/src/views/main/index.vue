<template>
    <div class="card">
        <el-text style='font-size: 30px'>CodeCheck是用于可视化代码检测结果的平台，项目正在开发，敬请期待....</el-text><br>
        <a style='font-size: 20px; color: #0056b3' href='https://github.com/KilluaYZ/CodeCheck'>源码地址</a>
    </div>

<!--    <div class="list">-->
<!--        <div class="item" v-for="i in 8" :key="i">模块{{ i }}</div>-->
<!--    </div>-->

    <div class="middle flex">
        <div class="dependence common">
            <div class="flex title">
                <h4>基本信息：</h4>
                <p>部署时间：2023/11/6</p>
            </div>
            <el-divider />
            <div class="plr">内容</div>
            <div class="plr">前端：vite</div>
            <div class="plr">后端：flask</div>

        </div>
        <div class="logs common">
            <div class="title">更新日志</div>
            <el-divider />
            <div class="plr">
                <el-timeline>
                    <el-timeline-item
                        v-for="(activity, index) in activities"
                        :key="index"
                        :icon="activity.icon"
                        :type="activity.type"
                        :color="activity.color"
                        :size="activity.size"
                        :hollow="activity.hollow"
                        :timestamp="activity.timestamp"
                    >
                        {{ activity.content }}
                    </el-timeline-item>
                </el-timeline>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
const activities = [
    {
        content: '前后端联调优化，开发中...',
        timestamp: '2023-11-06',
        size: 'large',
        type: 'primary',
        icon: 'MoreFilled',
    },
    {
        content: '前端搭建初步完成',
        timestamp: '2023-11-03',
        type: 'success',
    },
    {
        content: '开始搭建前端',
        timestamp: '2023-11-01',
        type: 'success',
    },
    {
        content: '后端搭建初步完成',
        timestamp: '2023-10-30',
        type: 'primary',
        hollow: true,
    },
    {
        content: '项目启动',
        timestamp: '2023-10-26',
        type: 'primary',
        hollow: true,
    },
]
</script>

<style scoped lang="scss">
$white: #fff;
.card {
    width: 100%;
    padding: 40px 20px;
    font-size: 12px;
    border: 1px solid #ebeef5;
    margin-bottom: 20px;
    background-color: #fff;
    color: #959595;
}
.list {
    display: flex;
    flex-wrap: wrap;
    .item {
        width: 23.5%;
        margin: 0 2% 2% 0;
        height: 10vh;
        background-color: #fff;
        &:nth-child(4n) {
            margin-right: 0;
        }
    }
}

.middle {
    .common {
        background-color: $white;
        width: 49%;
        .title {
            padding: 20px 20px 0 20px;
        }
        .plr {
            padding: 0 40px;
        }
    }
    .dependence {
    }
    .logs {
    }
}
.flex {
    @include flex(false, space-between);
}
</style>
