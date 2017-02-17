<template>
  <div>
    <h1>{{ msg }}</h1>
        <div v-for="item in datalist">
        {{ item.desc }}
      </div>
  </div>
</template>

<script>
export default {
  name: 'gank',
  data () {
    return {
      msg: 'api test',
      datalist: []
    }
  },
  mounted: function() {
    this.$http.get('http://gank.io/api/random/data/all/20')
      .then((response) => {
        this.datalist = response.data.result
      })
      .catch((response) => {
        console.log(response)
      })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>