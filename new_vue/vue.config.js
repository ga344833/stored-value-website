const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true
})
module.exports = {
  devServer: {
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:5000', // 將請求代理到的目標服務器的地址
        changeOrigin: true,
        // pathRewrite: {
        //   '^/api': '', // 如果 API 的路徑需要重寫，可以在這裡配置
        // },
      },
    },
  },
};