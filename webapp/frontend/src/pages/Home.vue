<template>
	<el-row class="container">
		<el-col :span="24" class="main">
			<aside>
        <el-menu default-active="$route.path" theme="dark" @select="handleselect" unique-opened router>
          <el-menu-item index="/hello"><i class="el-icon-menu"></i>主页</el-menu-item>
          <el-menu-item index="/gank"><i class="el-icon-message"></i>技术干货</el-menu-item>
          <el-menu-item index="/about"><i class="el-icon-setting"></i>关于</el-menu-item>
        </el-menu>
			</aside>
			<section class="content">
				<transition>
					<router-view></router-view>
				</transition>
			</section>
		</el-col>
	</el-row>
</template>
<script>
	export default {
		data() {
			return {
      }
		},

		methods: {
            handleselect: function (index, index_path){

            }
		}
	}

</script>

<style scoped lang="scss">
	.container {
		position: absolute;
		top: 0px;
		bottom: 0px;
		width: 100%;
		.main {
			background: #324057;
			position: absolute;
			top: 0px;
			bottom: 0px;
			overflow: hidden;
			aside {
				width: 230px;
			}
			.content {
				background: #f1f2f7;
				position: absolute;
				right: 0px;
				top: 0px;
				bottom: 0px;
				left: 230px;
				overflow-y: scroll;
				padding: 20px;

			}
		}
	}
</style>