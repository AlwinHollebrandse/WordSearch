<template>
    <div>
        <header>{{ title }}</header>

        <section v-if='errored'>
            <p>We're sorry, we're not able to retrieve this information at the moment, please try back later</p>
        </section>

        <section v-else>
            <div v-if='loading'>Loading...</div>

            <section v-else class='WordSearch'>
                <div>wordList: {{ wordList }}</div>
                <div v-for='(page, index) in wordSearch' :key='page'>
                    <h2 class='header'> Layer {{ index }} </h2>
                    <table class='wordSearchTable'>
                        <tr v-for='row in page' :key='row'>
                            <td v-on:click='highlight' v-for='col in row' :key='col'>{{ col }}</td>
                        </tr>
                    </table>
                </div>
                <div>wordSearchDepth: {{ wordSearchDepth }}</div>
            </section>
        </section>

        <!-- <div id='wordSearchPage'>
            <vue-glide startAt=5>
                <vue-glide-slide v-for='(page, index) in wordSearch' :key='page'>
                    <h2 class='header'> Layer {{ index }} </h2>
                    <table class='wordSearchTable'>
                        <tr v-for='row in page' :key='row'>
                            <td v-on:click='highlight' v-for='col in row' :key='col'>{{ col }}</td>
                        </tr>
                    </table>
                </vue-glide-slide>

                <vue-glide-slide v-for="i in 10" :key="i">
                    Slide {{ i }}
                </vue-glide-slide>

                <template slot='control' v-if='wordSearchDepth>1'>
                    <button data-glide-dir='<'>prev</button>
                    <button data-glide-dir='>'>next</button>
                </template>
            </vue-glide>
        </div> -->
    </div>
</template>

<script>
import axios from 'axios';
import { Glide, GlideSlide } from 'vue-glide-js'
import mockData from '../assets/mock_response.json'//'..assets/mock_response.JSON'

let useMockData = true

export default {
    name: 'WordSearch',
    data () {
        return {
            title: 'WordSearch',
            wordList: null,
            wordSearch: null,
            wordSearchDepth: null,
            wordSearchHeight: null,
            wordSearchWidth: null,
            loading: true,
            errored: false,
            [Glide.name]: Glide,
            [GlideSlide.name]: GlideSlide
        }
    },
    mounted () {
        if (useMockData) {
            this.wordList = mockData.wordList,
            this.wordSearch = mockData.wordSearch,
            this.wordSearchDepth = mockData.wordSearchDepth,
            this.wordSearchHeight = mockData.wordSearchHeight,
            this.wordSearchWidth = mockData.wordSearchWidth,
            this.loading = false
        } else {
            axios
                .get('http://0.0.0.0:5000/generateWordSearch')
                .then(response => {
                    this.wordList = response.data.wordList,
                    this.wordSearch = response.data.wordSearch,
                    this.wordSearchDepth = response.data.wordSearchDepth,
                    this.wordSearchHeight = response.data.wordSearchHeight,
                    this.wordSearchWidth = response.data.wordSearchWidth
                })
                .catch(error => {
                    console.log(error)
                    this.errored = true
                })
                .finally(() => this.loading = false)
        }
    },
    methods: {
        highlight: function () {
            console.log('highlight')
            this.wordSearch.forEach(page => {
                console.log(page)
            });
        }
    }
}
</script>

<style scoped>
    .header {
        text-align: left;
        left: 100px;
        color: rgb(15, 199, 15);
    }

    /* .glide--slide {
        table-layout: fixed;
    } */
    
    /* .layer {
        text-align: center;
    } */

    .wordSearchTable {
        /* text-align: center; */
        /* padding: 100px; */
        table-layout: fixed;
        /* width: 100%; */
        /* height: 100%; */
    }
</style>