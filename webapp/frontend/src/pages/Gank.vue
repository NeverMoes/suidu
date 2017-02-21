<template>
  <div>
    <el-table :data="tableData" border style="width: 100%" @row-click="openUrl">
        <el-table-column prop="desc" label="标题"></el-table-column>
        <el-table-column prop="publishedAt" label="时间"></el-table-column>
        <el-table-column prop="type" label="类型"></el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  name: 'Gank',
  data () {
    return {
        tableData: []
    }
  },
  methods: {
    openUrl(row, event, column) {
        window.open(row.url)
    }
  },
  mounted: function() {
    axios.get('http://gank.io/api/random/data/all/20')
      .then(response => this.tableData = response.data.results)
      .catch(error => console.log(error));
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>