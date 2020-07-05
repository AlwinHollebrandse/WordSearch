export interface Result {
  sliderArray: [
    {'img': string, 'alt': string, 'text': string }
  ];

  wordList: [string];
  wordSearch: [[[string]]];
  wordSearchDepth: number;
  wordSearchHeight: number;
  wordSearchWidth: number;
  

  // wordSearch: [
  //   {'wordList': [string], 'wordSearch': [[[string]]], 'wordSearchDepth': number, 'wordSearchHeight': number, 'wordSearchWidth': number}
  // ];
}


