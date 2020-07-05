import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
 providedIn: 'root'
})
export class DataService {

 constructor(private http: HttpClient) {
 }

 generateWordSearch() {
  const URL = 'http://localhost:5000/generateWordSearch';//'../assets/data.json';

  const headerDict = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Allow-Origin': 'http://localhost:5000/generateWordSearch',//'*',
  }
  
  const requestOptions = {                                                                                                                                                                                 
    headers: new HttpHeaders(headerDict),
    withCredentials: false,
  };

  return this.http.get(URL, requestOptions);
 }

 getHelloWorld() {
  const URL = 'http://localhost:5000/';

  const headerDict = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Allow-Origin': 'http://localhost:5000/',//'*',
  }
  
  const requestOptions = {                                                                                                                                                                                 
    headers: new HttpHeaders(headerDict),
    withCredentials: false,
  };

  return this.http.get(URL, requestOptions);
 }
}
