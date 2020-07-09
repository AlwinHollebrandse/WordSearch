<template>
    <div>
        <header>{{ title }}</header>

        <section v-if='errored'>
            <p>We're sorry, we're not able to retrieve this information at the moment, please try back later</p>
        </section>

        <section v-else>
            <div v-if='loading'>Loading...</div>

            <section v-else class='WordSearch'>
                <div>wordList: {{ wordList }}</div> <!--move to a diff componet and pass to api call-->
                <div>{{ wordSearch }}</div>
                <div>{{ wordSearch[0] }}</div>
                <div>{{ wordSearch[1] }}</div>
                <div>wordSearchDepth: {{ wordSearchDepth }}</div>
                <div>wordSearchHeight: {{ wordSearchHeight }}</div>
                <div>wordSearchWidth: {{ wordSearchWidth }}</div>
            </section>
        </section>

        <vue-glide type='carousel'>
            <vue-glide-slide v-for='(page, index) in wordSearch' :key='page'>
                <div id='layer'>
                    Layer {{index}}
                    <table id='wordSearchTable'>
                        <tr v-for='row in page' :key='row'>
                            <td v-for='col in row' :key='col'>{{ col }}</td>
                        </tr>
                    </table>
                </div>
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