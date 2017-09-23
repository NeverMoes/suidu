import NotFound from './pages/404.vue'
import Home from './pages/Home.vue'
import Hello from './pages/Hello.vue'
import Gank from './pages/Gank.vue'
//import Github from './pages/Github.vue'
import Hackernews from './pages/Hackernews.vue'
// import Daily from './pages/Daily.vue'
// import About from './pages/About.vue'

let routes = [
    {
        path: '/',
        redirect: '/home'
    },
    {
        path: '/home',
        component: Home,
        name: 'Home',
        children: [
            { path: '/hello', component: Hello, name: 'Hello' },
            { path: '/gank', component: Gank, name: 'Gank' },
            // { path: '/daily', component: Daily, name: 'Daily'},
            // { path: '/github', component: Github, name: 'Github'},
            { path: '/hackernews', component: Hackernews, name: 'Hackernews'},
            // { path: '/about', component: About, name: 'About'}
        ]
    },
    {
        path: '/404',
        component: NotFound,
        name: '',
        hidden: true
    },
    {
        path: '*',
        hidden: true,
        redirect: { path: '/404' }
    }
];

export default routes;