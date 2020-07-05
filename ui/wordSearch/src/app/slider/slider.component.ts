import { DataService } from './../data-service/data.service';
import { Component, OnInit} from '@angular/core';
import {Result} from './result';

@Component({
  selector: 'app-slider',
  templateUrl: './slider.component.html',
  styleUrls: ['./slider.component.scss'],
})

export class SliderComponent implements OnInit {
  wordList: [string];
  wordSearch: [[[string]]];
  wordSearchDepth: number;
  wordSearchHeight: number;
  wordSearchWidth: number;

  sliderArray: object[];
  transform: number;
  selectedIndex = 0;
 
  constructor(private data: DataService) {
    this.wordList = ['temp'];
    this.wordSearch = [[['temp']]];
    this.wordSearchDepth = 1;
    this.wordSearchHeight = 1;
    this.wordSearchWidth = 1;

    this.sliderArray = [];
    this.selectedIndex = 0;
    this.transform = 100;
  }

  ngOnInit() {
    this.data.generateWordSearch().subscribe((result: Result) => {
      console.log('HERE:', result)
      this.wordList = result.wordList;
      this.wordSearch = result.wordSearch;
      this.wordSearchDepth = result.wordSearchDepth;
      this.wordSearchHeight = result.wordSearchHeight;
      this.wordSearchWidth = result.wordSearchWidth;

      this.sliderArray = result.sliderArray;
      console.log('HERE sliderArray:', this.sliderArray);
    });
  }

  selected(x) {
    this.downSelected(x);
    this.selectedIndex = x;
   }

   keySelected(x) {
    this.downSelected(x);
    this.selectedIndex = x;
  }

   downSelected(i) {
   this.transform =  100 - (i) * 50;
     this.selectedIndex = this.selectedIndex + 1;
     if (this.selectedIndex > 4) {
       this.selectedIndex = 0;
     }
   }

}
