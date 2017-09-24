<template>
  <div>
    <el-table :data="tableData" highlight-current-row border style="width: 100%" @row-click="handRowClick">
        <el-table-column prop="title" label="标题"></el-table-column>
    </el-table>
  </div>
</template>

<script>
import {getHackernews} from '../api'

export default {
  name: 'Hackernews',
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
    }
  },
  mounted: function() {
    getHackernews()
      .then(response => this.tableData = response.data)
      .catch(error => console.log(error));
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>