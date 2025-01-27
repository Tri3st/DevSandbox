import { defineStore } from 'pinia';
import {ref} from "vue";

export const useNavStore = defineStore('nav', () => {
    const count = ref(0);

    const increment = () => {
        count.value++;
    }
    return { count, increment };
})