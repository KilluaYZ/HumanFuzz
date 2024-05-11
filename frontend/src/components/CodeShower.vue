<template>
    <div style='width: 100%'>
        <highlightjs :autodetect="language === undefined"  :language='language'  :code='code'></highlightjs>
    </div>
</template>

<script setup lang='ts'>

const props = defineProps({
    code:{
        required: true,
        type: String
    },
    language:{
        required: false,
        type: String
    }
})

</script>

<style scoped>

</style>