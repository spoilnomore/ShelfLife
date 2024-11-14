module.exports = {
    configureWebpack: {
        entry: "./src/main.js",
        devServer: {
            hot: true,
            port: 8080,
            host: '0.0.0.0',
            allowedHosts: 'all', // Allows all hosts
        },
        watch: true,
        watchOptions: {
            ignored: /node_modules/,
            poll: 1000,
        },
    },
    transpileDependencies: true,
};
