<template>
  <ul class="app-grid list">
    <svg id='appIllustrations' version="1.1" xmlns="http://www.w3.org/2000/svg">
    </svg>
    <li v-for="(letter, idx) in letters" class="grid-letter" :key='idx'> {{letter}}</li>
  </ul>
</template>

<script>
import Utility from './utility'
import Puzzler from './puzzler'

let mouseDown = false;
let puzzle;

export default {

    data: function () {
        return {
            letters: ``,
            words: [],
            selword: ''
        }
    },
    mounted: function () {
        //
        let _this = this;
        var paper = Snap('#appIllustrations');
        let p1, p2, lp1, lp2, cp2, line;

        $(".app-grid").on("mousedown", ".grid-letter", function (ev) {
            mouseDown = true;
            let idx = $(this).index(".grid-letter")
            p1 = $(this).position();
            lp1 = {
                y: Math.floor(idx / 15),
                x: ((idx % 15))
            }
            line = paper.line(p1.left + 12, p1.top + 12, p1.left + 12, p1.top + 12);
            line.attr({
                class: "line-1"
            });
        });
        $(".app-grid").on("mouseenter", ".grid-letter", function (ev) {
            if (mouseDown) {
                p2 = $(this).position();
                let idx = $(this).index(".grid-letter")
                cp2 = {
                    y: Math.floor(idx / 15),
                    x: ((idx % 15))
                }
                if (Utility.isValidMove(Utility.Math.getAngle(lp1.x, lp1.y, cp2.x, cp2.y))) {
                    line.attr({
                        x2: p2.left + 12,
                        y2: p2.top + 12
                    });
                    let selWord = _this.getSelectedWord(Utility.lettersBetween(lp1.x, lp1.y, cp2.x, cp2.y));
                    _this.$emit("word-select", selWord);
                }

            }
        })
        $(".app-grid").on("mouseup", ".grid-letter", function (ev) {
            mouseDown = false;
            let idx = $(this).index(".grid-letter");
            lp2 = {
                y: Math.floor(idx / 15),
                x: ((idx % 15))
            }
            let selWord = _this.getSelectedWord(Utility.lettersBetween(lp1.x, lp1.y, lp2.x, lp2.y));
            let matchedIndex = _this.words.findIndex((word) => {
                 return (!word.done && (word.word == selWord))
             });
            
            if (matchedIndex == -1) {
                $(line.node).fadeOut("slow", function () {
                    $(this).remove();
                });
            } else {
                _this.$emit("word-match", matchedIndex);
            }
            _this.$emit("word-select", "");
        })

        $(".viewport").mouseup(function(ev) {
            if(mouseDown) {
                $(line.node).fadeOut("slow", function () {
                    $(this).remove();
                });
                _this.$emit("word-select", "");
            }
        });
    },
    methods: {
        initPuzzle(words) {
            this.words = words;
            puzzle = Puzzler.generatePuzzle(this.words.map((word) => { return word.word }), 15, 15);
            var lttrs = "";
            puzzle.forEach((row) => {
                lttrs += row.join("");
            });
            this.letters = lttrs;
        },
        getSelectedWord(data) {
            let word = "";
            data.indices.forEach((idx) => {
                word += this.letters[idx]
            })
            return word;
        },

        reset() {
            $('#appIllustrations line').remove();
        }
    }
}
</script>
<style lang="less" scoped>
@import "./variables.less";
.app-grid {
    width: 100%;
    min-height: 100px;
    box-sizing: border-box;
    padding: 5px;
    background-color: #fff;
    position: relative;
    .grid-letter {
        position: relative;
        list-style-type: none;
        transition: 0.3s ease all;
        display: inline-block;
        font-size: @font-xs;
        user-select: none;
        width: 6.6%;
        text-align: center;
        box-sizing: border-box;
        padding: 5px 10px;
        color: @grey-color;
        text-transform: uppercase;
        .text-shadow();
        cursor: pointer;
        // &:before {
        //     content: '';
        //     display: inline-block;
        //     position: absolute;
        //     height: 100%;
        //     left: 100%;
        //     border-right: 1px solid #eee;
        // }
        &:hover {
            opacity: 0.6;
        }
    }
}
#appIllustrations {
    display: block;
    position: absolute;
    left: 0;
    top:0;
    height: 100%;
    width: 100%;
    pointer-events: none;
    .line-1 {
        stroke-linecap: round;
        stroke-width: 15;
        stroke-opacity: 0.5;
        stroke: #C3F1FE;
    }
}
</style>