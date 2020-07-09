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

    </div>
</template>

<script>
import axios from 'axios';

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
            errored: false
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