import NotFound from './pages/404.vue'
import Home from './pages/Home.vue'
import Hello from './pages/Hello.vue'
import Gank from './pages/Gank.vue'

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
            { path: '/gank', component: Gank, name: 'Gank' }
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