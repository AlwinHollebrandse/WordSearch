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
                <div>{{ wordSearch }}</div>
                <div>wordSearchDepth: {{ wordSearchDepth }}</div>
                <div>wordSearchHeight: {{ wordSearchHeight }}</div>
                <div>wordSearchWidth: {{ wordSearchWidth }}</div>
            </section>
        </section>

        <!-- <table id='wordSearchTable'>
            <tr v-for='row in wordSearch[0]' :key='row'>{{ row }}</tr>
        </table>



        <table id="secondTable">
        <thead>
            <tr>
                <th v-for="col in columns" :key='col'>{{col}}</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="row in wordSearch[0]" :key='row'>
                <td v-for="col in columns" :key='col'>{{row[col]}}</td>
            </tr>
        </tbody>
        </table> -->



        <vue-glide type=carousel>
            <!-- <vue-glide-slide v-for='(page, index) in wordSearch' :key="`page-${index}`"> -->
            <vue-glide-slide v-for='page in wordSearch' :key='page'>
                <!-- Layer {{ page }} TODO add "layer {{index}}" -->
                <table id='wordSearchTable'>
                    <tr v-for='row in wordSearch[0]' :key='row'>{{ row }}</tr>
                </table>
            </vue-glide-slide>
            <template slot='control' v-if='wordSearchDepth>1'>
                <button data-glide-dir='<'>prev</button>
                <button data-glide-dir='>'>next</button>
            </template>
        </vue-glide>
    </div>
</template>

<script>
import axios from 'axios';
import { Glide, GlideSlide } from 'vue-glide-js'

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
    // props: [wordSearch],
    mounted () {
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
}
</script>