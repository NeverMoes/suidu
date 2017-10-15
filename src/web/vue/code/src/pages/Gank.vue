<template>
  <div>
    <el-table :data="tableData" highlight-current-row border style="width: 100%" @row-click="handRowClick" :row-class-name="tableRowClassName">
        <el-table-column prop="desc" label="标题"></el-table-column>
        <el-table-column prop="publishedAt" label="时间"></el-table-column>
        <el-table-column prop="type" label="类型"></el-table-column>
    </el-table>
  </div>
</template>

<script>
import {getGank} from '../api'

export default {
  name: 'Gank',
  data () {
    return {
        tableData: []
        // rowStyle: {

        // }
    }
  },
  methods: {
    handRowClick(row, event, column) {
        window.open(row.url)
    },
    tableRowClassName(row, index) {
        if (index >= 0) {
          return 'info-row';
        }
        return '';
    }
  },
  mounted: function() {
    getGank()
      .then(response => this.tableData = response.data.results)
      .catch(error => console.log(error));
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
  .el-table .info-row {}

  .el-table .info-row:hover{
    cursor: pointer;
  }
</style>