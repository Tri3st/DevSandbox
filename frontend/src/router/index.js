import {createRouter, createWebHistory} from "vue-router";
import HomeView from "@/views/HomeView.vue";
import PortfolioView from "@/views/PortfolioView.vue";
import AboutmeView from "@/views/AboutmeView.vue";
import LinksView from "@/views/LinksView.vue";

const routes = [
    {
        path: '/',
        name: 'home',
        component: HomeView
    },
    {
        path: '/portfolio',
        name: 'portfolio',
        component: PortfolioView
    },
    {
        path: '/links',
        name: 'links',
        component: LinksView
    },
    {
        path: '/aboutme',
        name: 'aboutme',
        component: AboutmeView
    }

];

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router;